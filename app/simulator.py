"""Simulador didáctico: NO es AWS ni un motor completo de políticas IAM."""
import hashlib
import json
from pathlib import Path


def read_config(text):
    allowed = {"S3_BUCKET", "S3_PREFIX"}
    result = {}
    for line in text.splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        key, sep, value = line.partition("=")
        if not sep or key not in allowed or key in result:
            raise ValueError("config.env admite S3_BUCKET y S3_PREFIX una vez cada una")
        if not value or any(c in value for c in "\"'$`\\\x00"):
            raise ValueError("Usa valores literales sin comillas ni expansiones")
        result[key] = value
    if set(result) != allowed:
        raise ValueError("Falta S3_BUCKET o S3_PREFIX")
    return result


def load_case(path):
    path = Path(path)
    return (json.loads((path / "session.json").read_text()),
            json.loads((path / "policy.json").read_text()),
            (path / "payload.csv").read_bytes())


def simulate(session, policy, payload, config):
    bucket = config["S3_BUCKET"]
    key = config["S3_PREFIX"] + session["filename"]
    resource = f"arn:aws:s3:::{bucket}/{key}"
    statement = policy["Statement"][0]
    pattern = statement["Resource"]
    # Único alcance soportado: Allow PutObject sobre un prefijo terminado en /*.
    authorized = (statement["Effect"] == "Allow"
                  and statement["Action"] == "s3:PutObject"
                  and pattern.endswith("/*")
                  and resource.startswith(pattern[:-1]))
    return {
        "simulated": True, "case_id": session["case_id"],
        "run_id": session["run_id"], "client": session["client"],
        "principal": session["principal"], "action": "s3:PutObject",
        "bucket": bucket, "key": key, "resource": resource,
        "status": "DELIVERED" if authorized else "AccessDenied",
        "sha256": hashlib.sha256(payload).hexdigest() if authorized else None,
    }


def receipt_matches(receipt, session, payload):
    expected = {
        "simulated": True, "case_id": session["case_id"],
        "run_id": session["run_id"], "client": session["client"],
        "bucket": session["expected_bucket"],
        "key": session["expected_prefix"] + session["filename"],
        "status": "DELIVERED", "sha256": hashlib.sha256(payload).hexdigest(),
    }
    return all(receipt.get(k) == v for k, v in expected.items())
