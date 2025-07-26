#!/usr/bin/env python3
import os
import rumps
import tkinter as tk
from tkinter import simpledialog
from file_agent import process_user_query

class FileBotApp(rumps.App):
    def __init__(self):
        super(FileBotApp, self).__init__("🧠 FileBot", quit_button="Quit")
        self.menu = ["Ask"]

    @rumps.clicked("Ask")
    def ask(self, _):
        # Spawn a hidden Tkinter root to use its dialog
        root = tk.Tk()
        root.withdraw()

        # Show a standard input dialog
        query = simpledialog.askstring(
            title="Ask FileBot",
            prompt="Enter your question about local files:",
            initialvalue="  "
        )
        root.destroy()

        # If user cancels or gives empty input, do nothing
        if not query:
            return

        # Process the query
        try:
            answer = process_user_query(query.strip())
        except Exception as e:
            answer = f"Error: {e}"

        # Show the response in a native macOS alert
        rumps.alert(title="FileBot", message=answer[:2000])

if __name__ == "__main__":
    print(f"🐢 Launching FileBot (Python: {os.sys.executable})")
    FileBotApp().run()
