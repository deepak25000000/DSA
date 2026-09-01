import os

def count_files(directory):
    if not os.path.exists(directory):
        return 0
    # count .py files
    return len([f for f in os.listdir(directory) if f.endswith('.py')])

def main():
    base_dir = "."
    
    directories = {
        "Simple_Operations": count_files(os.path.join(base_dir, "Simple_Operations")),
        "List_array": count_files(os.path.join(base_dir, "List_array")),
        "Sorting": count_files(os.path.join(base_dir, "Sorting")),
        "OOPS": count_files(os.path.join(base_dir, "OOPS")),
    }
    
    total = sum(directories.values())
    
    def get_status(count):
        if count == 0:
            return "⏳ Not Started"
        elif count < 5:
            return "🌱 Started"
        else:
            return "🔥 Active"

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
| 🧮 **[Simple Maths / Operations](./Simple_Operations)** | <kbd> {directories['Simple_Operations']} </kbd> | {get_status(directories['Simple_Operations'])} |
| 📋 **[Arrays / Lists](./List_array)** | <kbd> {directories['List_array']} </kbd> | {get_status(directories['List_array'])} |
| 🔄 **[Sorting](./Sorting)** | <kbd> {directories['Sorting']} </kbd> | {get_status(directories['Sorting'])} |
| 🏗️ **[Object-Oriented Programming (OOPS)](./OOPS)** | <kbd> {directories['OOPS']} </kbd> | {get_status(directories['OOPS'])} |
| **🏆 Total Solved** | <kbd> {total} </kbd> | 🚀 Keep Going! |

</details>

---

## 📂 Directory Structure

Here's a quick overview of what you will find in this repository:

> **Note**: Each folder contains python files with my solutions and approaches to various problems.

* 📁 **`List_array/`** — *Contains solutions for Array and List-based problems (e.g., searching, modifying arrays, moving zeros, finding missing numbers).*
* 📁 **`Simple_Operations/`** — *Basic math operations, digit manipulation, palindromes, and introductory logic problems.*
* 📁 **`Sorting/`** — *Implementations and problems related to popular sorting algorithms like Merge Sort.*
* 📁 **`OOPS/`** — *Concepts and problems related to Object-Oriented Programming in Python (classes, inheritance, etc).*

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

if __name__ == "__main__":
    main()
