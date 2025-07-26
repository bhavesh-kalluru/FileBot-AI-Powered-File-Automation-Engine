import openai
import os
import re
from dotenv import load_dotenv
from utils import search_files, read_file

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


def extract_filename(query):
    # Clean up punctuation and extract file-like keyword
    query = re.sub(r'[^\w\s.\-]', '', query)
    words = query.split()
    for word in words:
        if '.' in word:  # likely a file
            return word
    return words[-1] if words else None


def get_response_from_gpt(prompt):
    messages = [
        {"role": "system",
         "content": "You are a helpful assistant for searching and explaining files on the user's Mac."},
        {"role": "user", "content": prompt}
    ]
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=messages,
        temperature=0.3
    )
    return response['choices'][0]['message']['content']


def process_user_query(query):
    home_dir = os.path.expanduser("~")  # Auto-detect user home path
    keyword = extract_filename(query)

    print(f"[DEBUG] User Query: {query}")
    print(f"[DEBUG] Extracted Keyword: {keyword}")
    print(f"[DEBUG] Searching in: {home_dir}")

    if "where" in query.lower() and keyword:
        results = search_files(home_dir, keyword)
        if results:
            return "\n".join(results)
        return f"No files found with keyword '{keyword}'."

    if any(cmd in query.lower() for cmd in ["read", "show", "open", "what is inside"]) and keyword:
        results = search_files(home_dir, keyword)
        if results:
            content = read_file(results[0])
            return f"**File:** {results[0]}\n\n---\n{content}"
        return f"File '{keyword}' not found."

    # Fallback to GPT
    return get_response_from_gpt(query)
