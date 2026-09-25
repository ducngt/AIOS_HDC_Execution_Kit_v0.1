#!/usr/bin/env python3
import json, os, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TASKS = ROOT / "tasks"
STATE = ROOT / "hdc" / "state.json"


def load_json(p):
    return json.loads(Path(p).read_text(encoding="utf-8"))


def save_json(p, obj):
    Path(p).write_text(json.dumps(obj, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def task_dirs():
    return sorted([p for p in TASKS.iterdir() if p.is_dir() and p.name.startswith("T")])


def get_task(tid):
    p = TASKS / tid / "task.json"
    if not p.exists():
        raise SystemExit(f"Unknown task: {tid}")
    return load_json(p)


def cmd_status():
    st = load_json(STATE)
    print(json.dumps(st, ensure_ascii=False, indent=2))


def cmd_next():
    st = load_json(STATE)
    completed = set(st.get("completed", []))
    for d in task_dirs():
        t = load_json(d / "task.json")
        if t["id"] in completed:
            continue
        if all(dep in completed for dep in t.get("depends_on", [])):
            print(t["id"], "-", t["title"])
            return
    print("No ready task. Either all tasks are completed or dependencies are unresolved.")


def cmd_prompt(tid):
    p = TASKS / tid / "PROMPT.md"
    if not p.exists():
        raise SystemExit(f"Prompt not found for {tid}")
    print(p.read_text(encoding="utf-8"))


def cmd_task(tid):
    print(json.dumps(get_task(tid), ensure_ascii=False, indent=2))


def cmd_complete(tid):
    st = load_json(STATE)
    t = get_task(tid)
    missing = [d for d in t.get("depends_on", []) if d not in st.get("completed", [])]
    if missing:
        raise SystemExit("Dependencies incomplete: " + ", ".join(missing))
    if tid not in st["completed"]:
        st["completed"].append(tid)
    st["current_task"] = None
    save_json(STATE, st)
    print(f"Marked {tid} completed. Human acceptance is tracked separately.")


def cmd_accept(tid):
    st = load_json(STATE)
    if tid not in st.get("completed", []):
        raise SystemExit("Task must be completed before acceptance.")
    if tid not in st["accepted"]:
        st["accepted"].append(tid)
    save_json(STATE, st)
    print(f"Human acceptance recorded for {tid}.")


def usage():
    print("Usage: python hdc/hdc.py status|next|prompt <Txx>|task <Txx>|complete <Txx>|accept <Txx>")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        usage(); raise SystemExit(2)
    cmd = sys.argv[1]
    if cmd == "status": cmd_status()
    elif cmd == "next": cmd_next()
    elif cmd == "prompt" and len(sys.argv) == 3: cmd_prompt(sys.argv[2])
    elif cmd == "task" and len(sys.argv) == 3: cmd_task(sys.argv[2])
    elif cmd == "complete" and len(sys.argv) == 3: cmd_complete(sys.argv[2])
    elif cmd == "accept" and len(sys.argv) == 3: cmd_accept(sys.argv[2])
    else:
        usage(); raise SystemExit(2)
