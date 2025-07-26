#!/usr/bin/env python3
import os
import rumps
import subprocess
from file_agent import process_user_query

def ask_user(prompt: str, default: str) -> str:
    osa = (
        f'display dialog "{prompt}" default answer "{default}" '
        f'buttons {{"Ask","Cancel"}} default button "Ask"'
    )
    proc = subprocess.run(["osascript", "-e", osa], capture_output=True, text=True)
    if proc.returncode != 0 or not proc.stdout:
        return None
    for part in proc.stdout.split(","):
        if part.strip().startswith("text returned:"):
            return part.split("text returned:")[1]
    return None

class FileBotApp(rumps.App):
    def __init__(self):
        super().__init__("🧠 FileBot", quit_button="Quit")
        self.menu = ["Ask"]

    @rumps.clicked("Ask")
    def ask(self, _):
        query = ask_user("Enter your question about local files:", "Where is resume.pdf?")
        if not query:
            return
        try:
            raw = process_user_query(query.strip())
        except Exception as e:
            raw = f"Error: {e}"
        # number each non‑empty line
        lines = [ln for ln in raw.splitlines() if ln.strip()]
        msg = "\n".join(f"{i}. {ln}" for i, ln in enumerate(lines, 1))
        rumps.alert(title="FileBot", message=msg or "No response.")

if __name__ == "__main__":
    print(f"🐢 Launching FileBot (Python: {os.sys.executable})")
    FileBotApp().run()
