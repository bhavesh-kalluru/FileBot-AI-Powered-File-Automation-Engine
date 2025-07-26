#!/usr/bin/env python3
import os
import openai
import re
from dotenv import load_dotenv
from utils import search_files, read_file
from file_agent import extract_filename, get_response_from_gpt  # move these helpers into file_agent.py


def process_user_query(query: str, root_dir: str):
    keyword = extract_filename(query)

    # 1. “Where is X” → list matching paths
    if "where" in query.lower() and keyword:
        results = search_files(root_dir, keyword)
        if results:
            return "\n".join(results)
        return f"No files found with keyword '{keyword}'."

    # 2. “Read/Show/Open X” → show file contents
    if any(w in query.lower() for w in ["read", "show", "open", "inside"]) and keyword:
        results = search_files(root_dir, keyword)
        if results:
            content = read_file(results[0])
            return f"File: {results[0]}\n---\n{content}"
        return f"File '{keyword}' not found."

    # 3. Default → GPT
    return get_response_from_gpt(query)


def main():
    # ─── Setup ─────────────────────────────────────────────────────────────
    load_dotenv()
    openai.api_key = os.getenv("OPENAI_API_KEY")
    home_dir = os.path.expanduser("~")  # auto‐detect your home folder

    print("📁 FileBot CLI is ready! (type 'exit' or 'quit' to stop)\n")

    # ─── REPL Loop ────────────────────────────────────────────────────────
    while True:
        user_input = input("You: ").strip()
        if user_input.lower() in ("exit", "quit"):
            print("Bot: Goodbye!")
            break

        raw_answer = process_user_query(user_input, home_dir)

        # ─── Print answer point‑wise ─────────────────────────────
        lines = [line for line in raw_answer.split("\n") if line.strip()]
        for i, line in enumerate(lines, start=1):
            print(f"{i}. {line}")
        print()  # blank line before next prompt


if __name__ == "__main__":
    main()
