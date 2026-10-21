"""Comprobaciones públicas. No contiene la clave privada de evaluación."""
import argparse
import json
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]


def run(*args):
    return subprocess.run(["docker", "compose", *args], cwd=ROOT,
                          capture_output=True, text=True)


def validate_answers():
    try:
        data = json.loads((ROOT / "RESPUESTAS.json").read_text())
        for q in ("P1", "P2", "P3", "P4"):
            row = data[q]
            if not all(isinstance(row.get(k), str) for k in
                       ("opcion", "evidencia", "justificacion", "comando")):
                raise ValueError(f"{q}: conserva los cuatro campos de texto")
        if not isinstance(data["resumen"], str) or not isinstance(data["uso_ia"], str):
            raise ValueError("resumen y uso_ia deben ser texto")
        print("Formato válido. Esto no califica las respuestas.")
        return 0
    except (OSError, ValueError, KeyError, TypeError) as exc:
        print(f"Formato inválido: {exc}")
        return 1


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("action", choices=["start", "check", "capture", "answers"])
    args = parser.parse_args()
    if args.action == "answers":
        return validate_answers()
    if args.action == "start":
        result = run("up", "-d", "--no-build")
        print(result.stdout, end="")
        print(result.stderr, end="", file=sys.stderr)
        return result.returncode
    if args.action == "check":
        result = run("exec", "-T", "delivery", "python", "/lab/app/service.py", "check")
        print(result.stdout, end="")
        print(result.stderr, end="", file=sys.stderr)
        return result.returncode
    # Preserva el primer fallo y el resultado final como evidencia revisable.
    evidence = ROOT / "evidence"
    evidence.mkdir(exist_ok=True)
    commands = {
        "logs.txt": ("logs", "--no-color", "--tail", "60"),
        "status.txt": ("ps", "-a"),
        "receipt.json": ("exec", "-T", "delivery", "cat", "/lab/artifacts/receipt.json"),
    }
    ok = True
    for name, command in commands.items():
        result = run(*command)
        if result.returncode:
            print(result.stderr, file=sys.stderr)
            ok = False
            continue
        (evidence / name).write_text(result.stdout)
        if name == "receipt.json":
            try:
                if json.loads(result.stdout).get("status") == "AccessDenied":
                    target = evidence / "initial-receipt.json"
                    if not target.exists():
                        target.write_text(result.stdout)
            except ValueError:
                ok = False
    print("Evidencia guardada en evidence/. Revisa su contenido antes del commit.")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
