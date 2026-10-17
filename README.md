# Exception-and-File-Handling
# Personal Journal Manager

A robust command-line application built in Python for maintaining a personal journal. This project demonstrates core Python programming concepts, including Object-Oriented Programming (OOP), file handling operations, and comprehensive exception handling.

---

## Project Overview

The **Personal Journal Manager** allows users to securely record daily thoughts, review past entries, search for specific notes by keywords or timestamps, and manage storage using text files (`.txt`). 

---

## Learning Objectives & Features

- **Object-Oriented Programming (OOP):** Encapsulates core logic within the `JournalManager` class using instance methods and clean separation of concerns.
- **File Handling Operations:** Demonstrates the use of different file modes:
  - Append mode (`'a'`) for adding new journal entries without overwriting existing ones.
  - Read mode (`'r'`) for viewing and searching records.
  - File deletion handling via the `os` module for clearing records.
- **Exception Handling:** Robustly catches common file I/O errors such as `FileNotFoundError` and `PermissionError` to ensure the program never crashes unexpectedly.
- **Interactive User Interface (UI):** A menu-driven console interface guiding user actions smoothly.

---

## Project Requirements

- Python 3.x installed on your system.
- Standard libraries used (`os`, `datetime`), requiring **no external packages or dependencies**.

---

## Example Console Interaction

```text
========================================
Welcome to Personal Journal Manager!
Please select an option:
========================================
1. Add a New Entry
2. View All Entries
3. Search for an Entry
4. Delete All Entries
5. Exit

User Input:
> 1

Enter your journal entry:
> Today was a productive day. I learned about file handling in Python.

Entry added successfully!
