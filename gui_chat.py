import tkinter as tk
from tkinter import scrolledtext
from file_agent import process_user_query

class FileBotGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("💬 FileBot")
        self.root.geometry("600x600")
        self.root.resizable(False, False)

        self.chat_window = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, font=("Helvetica", 12))
        self.chat_window.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
        self.chat_window.insert(tk.END, "📁 FileBot is ready! Ask me about your files.\n\n")
        self.chat_window.config(state=tk.DISABLED)

        self.entry_field = tk.Entry(self.root, font=("Helvetica", 12))
        self.entry_field.pack(padx=10, pady=(0, 10), fill=tk.X)
        self.entry_field.bind("<Return>", self.send_message)

    def send_message(self, event=None):
        user_input = self.entry_field.get().strip()
        if not user_input:
            return
        self.entry_field.delete(0, tk.END)

        self.display_message("You", user_input)

        try:
            response = process_user_query(user_input)
        except Exception as e:
            response = f"[Error] {str(e)}"

        self.display_message("Bot", response)

    def display_message(self, sender, message):
        self.chat_window.config(state=tk.NORMAL)
        self.chat_window.insert(tk.END, f"{sender}: {message}\n\n")
        self.chat_window.config(state=tk.DISABLED)
        self.chat_window.see(tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = FileBotGUI(root)
    root.mainloop()
