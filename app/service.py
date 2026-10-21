import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import time
import uuid

from simulator import load_case, simulate, receipt_matches


def emit(**fields):
    print(json.dumps(fields, ensure_ascii=False), flush=True)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("mode", choices=["delivery", "metrics", "check"])
    args = parser.parse_args()
    folder = Path(os.environ.get("CASE_DIR", "/lab/case"))
    output = Path(os.environ.get("OUTPUT_DIR", "/lab/artifacts"))
    session, policy, payload = load_case(folder)
    if args.mode == "check":
        try:
            receipt = json.loads((output / "receipt.json").read_text())
            delivered = (output / "object.bin").read_bytes()
            ok = (receipt_matches(receipt, session, payload)
                  and hashlib.sha256(delivered).hexdigest() == receipt["sha256"])
            print(json.dumps({"ok": ok, "receipt": receipt}, ensure_ascii=False))
            return 0 if ok else 1
        except (OSError, ValueError, KeyError) as exc:
            print(json.dumps({"ok": False, "error": str(exc)}))
            return 1
    if args.mode == "metrics":
        emit(**session["metrics_event"])
    else:
        for event in session["history"]:
            emit(**event)
        emit(service="delivery", event="INPUT_READY", client=session["client"],
             run_id=session["run_id"], timestamp=datetime.now(timezone.utc).isoformat())
        result = simulate(session, policy, payload,
                          {"S3_BUCKET": os.environ["S3_BUCKET"],
                           "S3_PREFIX": os.environ["S3_PREFIX"]})
        result.update(timestamp=datetime.now(timezone.utc).isoformat(),
                      attempt_id=str(uuid.uuid4()))
        output.mkdir(parents=True, exist_ok=True)
        (output / "object.bin").unlink(missing_ok=True)
        if result["status"] == "DELIVERED":
            (output / "object.bin").write_bytes(payload)
        (output / "receipt.json").write_text(json.dumps(result, indent=2))
        emit(service="delivery", event="PUT_OBJECT", **result)
    while True:
        time.sleep(1)


if __name__ == "__main__":
    raise SystemExit(main())
