import os
import sys

# Windows consoles default to cp1252, which crashes on emoji output.
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

BASE_DIR = "."

# Folders that are never treated as DSA topics.
EXCLUDED_DIRS = {
    ".git",
    ".github",
    "__pycache__",
    ".venv",
    "venv",
    "node_modules",
}

# Curated metadata for known topic folders (displayed first, in this order).
KNOWN_TOPICS = {
    "Simple_Operations": {
        "emoji": "🧮",
        "title": "Simple Maths / Operations",
        "description": "Basic math operations, digit manipulation, palindromes, and introductory logic problems.",
    },
    "List_array": {
        "emoji": "📋",
        "title": "Arrays / Lists",
        "description": "Contains solutions for Array and List-based problems (e.g., searching, modifying arrays, moving zeros, finding missing numbers).",
    },
    "Sorting": {
        "emoji": "🔄",
        "title": "Sorting",
        "description": "Implementations and problems related to popular sorting algorithms like Merge Sort.",
    },
    "Binary_search": {
        "emoji": "🎯",
        "title": "Binary Search",
        "description": "Binary search variants on arrays — classic search, insert position, first/last occurrence, ceil/floor, and rotated sorted arrays (with and without duplicates).",
    },
    "Linked_list": {
        "emoji": "🔗",
        "title": "Linked List",
        "description": "Linked list implementations and problems, organized into `Singly_Linked_List/` and `Doubly_Linked_list/` subfolders.",
    },
    "OOPS": {
        "emoji": "🏗️",
        "title": "Object-Oriented Programming (OOPS)",
        "description": "Concepts and problems related to Object-Oriented Programming in Python (classes, inheritance, etc).",
    },
}
CURATED_ORDER = [
    "Simple_Operations",
    "List_array",
    "Sorting",
    "Binary_search",
    "Linked_list",
    "OOPS",
]

# Emojis cycled through for auto-discovered (new) topic folders.
NEW_TOPIC_EMOJIS = ["📗", "📘", "📙", "🧩", "📚", "🧠", "🗂️"]


def count_py_files(directory):
    """Recursively count .py files inside a directory (includes subfolders)."""
    if not os.path.isdir(directory):
        return 0
    count = 0
    for _, _, files in os.walk(directory):
        count += sum(1 for f in files if f.endswith(".py"))
    return count


def get_status(count):
    if count == 0:
        return "🚧 Coming Soon"
    return "🔥 Active"


def get_subfolders(directory):
    """Return sorted subfolder names of a directory (empty list if none)."""
    if not os.path.isdir(directory):
        return []
    return sorted(
        d
        for d in os.listdir(directory)
        if os.path.isdir(os.path.join(directory, d)) and d != "__pycache__"
    )


def auto_title(folder_name):
    """Turn a folder name into a display title: 'Dynamic_programming' -> 'Dynamic Programming'."""
    return folder_name.replace("_", " ").replace("-", " ").title()


def discover_topics():
    """
    Auto-detect every top-level topic folder in the repository.
    Known topics come first in curated order; any NEW folder is appended
    alphabetically with an auto-generated title, emoji, and description.
    """
    existing = {
        d
        for d in os.listdir(BASE_DIR)
        if os.path.isdir(os.path.join(BASE_DIR, d))
        and d not in EXCLUDED_DIRS
        and not d.startswith(".")
        and d != "__pycache__"
    }

    ordered_keys = [k for k in CURATED_ORDER if k in existing]
    new_keys = sorted(existing - set(ordered_keys))

    topics = []
    for key in ordered_keys:
        meta = KNOWN_TOPICS[key]
        topics.append((key, meta["emoji"], meta["title"], meta["description"]))

    for i, key in enumerate(new_keys):
        title = auto_title(key)
        emoji = NEW_TOPIC_EMOJIS[i % len(NEW_TOPIC_EMOJIS)]
        description = f"Solutions and practice problems for {title}."
        topics.append((key, emoji, title, description))

    return topics, new_keys


def build_table_rows(counts, topics):
    rows = []
    for key, emoji, title, _ in topics:
        rows.append(
            f"| {emoji} **[{title}](./{key})** "
            f"| <kbd> {counts[key]} </kbd> "
            f"| {get_status(counts[key])} |"
        )
    rows.append(
        f"| **🏆 Total Solved** | <kbd> {sum(counts.values())} </kbd> | 🚀 Keep Going! |"
    )
    return "\n".join(rows)


def build_directory_entries(topics):
    entries = []
    for key, _, _, desc in topics:
        entries.append(f"* 📁 **`{key}/`** — *{desc}*")
        for sub in get_subfolders(os.path.join(BASE_DIR, key)):
            sub_path = os.path.join(BASE_DIR, key, sub)
            n = count_py_files(sub_path)
            if n == 0:
                detail = "Empty — coming soon"
            else:
                detail = f"{n} solution file{'s' if n != 1 else ''}"
            entries.append(f"  * 📁 **`{key}/{sub}/`** — *{detail}*")
    return "\n".join(entries)


def main():
    topics, new_keys = discover_topics()
    counts = {key: count_py_files(os.path.join(BASE_DIR, key)) for key, *_ in topics}
    total = sum(counts.values())

    table_rows = build_table_rows(counts, topics)
    directory_entries = build_directory_entries(topics)

    readme_content = f"""<div align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&height=250&section=header&text=DSA%20Journey%20&fontSize=80&animation=fadeIn&fontAlignY=35&desc=Mastering%20Data%20Structures%20and%20Algorithms&descAlignY=55&descAlign=50" />

  <br>

  [![Python](https://img.shields.io/badge/Language-Python-3776AB?style=for-the-badge&logo=python&logoColor=white)]()
  [![LeetCode](https://img.shields.io/badge/-LeetCode-FFA116?style=for-the-badge&logo=LeetCode&logoColor=black)](https://leetcode.com/u/deepak_thorat_25/)
  [![Progress](https://img.shields.io/badge/Total_Solved-{total}-2ea44f?style=for-the-badge)]()
  [![Daily Coding](https://img.shields.io/badge/Status-Active_🔥-ff69b4?style=for-the-badge)]()

  <i>My personal repository for tracking Data Structures and Algorithms practice, problems, and concepts.</i>
</div>

---

## 📊 Progress Tracker

<details open>
<summary><b>Click to see topic-wise breakdown</b></summary>
<br>

| 🧩 Topic | 📝 Questions Solved | 📈 Status |
| :--- | :---: | :---: |
{table_rows}

</details>

---

## 📂 Directory Structure

Here's a quick overview of what you will find in this repository:

> **Note**: Each folder contains Python files with my solutions and approaches to various problems. This README is **auto-generated and auto-updated by GitHub Actions** — new topic folders, subfolders, and solution files are detected automatically on every push.

{directory_entries}

---

## 🚀 How I Practice

1. **Understand the Problem**: Read the prompt carefully and note constraints.
2. **Brute Force First**: Find *a* solution before finding the *best* solution.
3. **Optimize**: Look for better time and space complexities.
4. **Code & Refactor**: Write clean Pythonic code.

<br>

<div align="center">
  <i>"Consistency is the key to mastering algorithms!"</i> 💻✨
</div>
"""

    with open("README.md", "w", encoding="utf-8") as f:
        f.write(readme_content)

    print("README.md updated successfully.")
    for key, emoji, title, _ in topics:
        print(f"  {emoji} {key}: {counts[key]}")
    print(f"  TOTAL: {total}")
    if new_keys:
        print(f"  Newly auto-detected folders: {', '.join(new_keys)}")
    else:
        print("  No new topic folders detected.")


if __name__ == "__main__":
    main()
