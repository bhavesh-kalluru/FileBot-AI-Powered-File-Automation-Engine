import os

def search_files(root_dir, keyword=None):
    matches = []
    for root, dirs, files in os.walk(root_dir):
        for name in files:
            if keyword is None or keyword.lower() in name.lower():
                matches.append(os.path.join(root, name))
    return matches

def read_file(filepath, max_lines=100):
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            lines = f.readlines()
            return ''.join(lines[:max_lines])
    except Exception as e:
        return f"Error reading file: {str(e)}"
