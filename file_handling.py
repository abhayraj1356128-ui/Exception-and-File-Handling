import os
from datetime import datetime

class JournalManager:
    """
    Encapsulates all file handling operations, exception management,
    and business logic for the Personal Journal Manager.
    """
    def __init__(self, filename="journal.txt"):
        self.filename = filename

    def add_entry(self):
        """Adds a new journal entry with a timestamp to the file using append mode ('a')."""
        print("\n----------------------------------------")
        entry_text = input("Enter your journal entry:\n> ").strip()
        
        if not entry_text:
            print("Error: Entry cannot be empty.")
            return

        timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
        formatted_entry = f"{timestamp} {entry_text}\n"

        try:
            # Using append mode ('a') to add entries without overwriting existing ones
            with open(self.filename, "a", encoding="utf-8") as file:
                file.write(formatted_entry)
            print("\nEntry added successfully!")
        except PermissionError:
            print(f"\nError: Permission denied to write to '{self.filename}'.")
        except Exception as e:
            print(f"\nAn unexpected error occurred: {e}")

    def view_entries(self):
        """Displays all journal entries from the file, handling FileNotFoundError gracefully."""
        print("\n----------------------------------------")
        try:
            # Using read mode ('r') to read entries
            with open(self.filename, "r", encoding="utf-8") as file:
                content = file.read().strip()
                if not content:
                    print("No journal entries found. Start by adding a new entry!")
                else:
                    print("Your Journal Entries:")
                    print("-" * 30)
                    print(content)
        except FileNotFoundError:
            print(f"Error: The journal file does not exist. Please add a new entry first.")
        except PermissionError:
            print(f"Error: Permission denied to read '{self.filename}'.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def search_entries(self):
        """Searches the journal file for specific keywords or dates."""
        print("\n----------------------------------------")
        query = input("Enter a keyword or date to search: ").strip()
        
        if not query:
            print("Error: Search query cannot be empty.")
            return

        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                lines = file.readlines()
                matching_lines = [line for line in lines if query.lower() in line.lower()]

                if matching_lines:
                    print("\nMatching Entries:")
                    print("-" * 30)
                    for line in matching_lines:
                        print(line.strip())
                else:
                    print(f"\nNo entries were found for the keyword: {query}.")
        except FileNotFoundError:
            print(f"Error: The journal file does not exist. Please add a new entry first.")
        except PermissionError:
            print(f"Error: Permission denied to access '{self.filename}'.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def delete_entries(self):
        """Deletes the journal file after user confirmation."""
        print("\n----------------------------------------")
        if not os.path.exists(self.filename):
            print("No journal entries to delete.")
            return

        confirmation = input("Are you sure you want to delete all entries? (yes/no): ").strip().lower()
        if confirmation == 'yes':
            try:
                os.remove(self.filename)
                print("All journal entries have been deleted.")
            except PermissionError:
                print(f"Error: Permission denied to delete '{self.filename}'.")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")
        else:
            print("Deletion cancelled.")


def main():
    manager = JournalManager()

    while True:
        print("\n========================================")
        print("Welcome to Personal Journal Manager!")
        print("Please select an option:")
        print("========================================")
        print("1. Add a New Entry")
        print("2. View All Entries")
        print("3. Search for an Entry")
        print("4. Delete All Entries")
        print("5. Exit")
        
        choice = input("\nUser Input:\n> ").strip()

        if choice == '1':
            manager.add_entry()
        elif choice == '2':
            manager.view_entries()
        elif choice == '3':
            manager.search_entries()
        elif choice == '4':
            manager.delete_entries()
        elif choice == '5':
            print("\nThank you for using Personal Journal Manager. Goodbye!")
            break
        else:
            print("\nInvalid option. Please select a valid option from the menu.")

if __name__ == "__main__":
    main()