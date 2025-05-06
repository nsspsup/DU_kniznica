
# ui/console.py

from services.book_service import add_book, find_books_by_title
from services.member_service import register_member, get_all_members
from services.loan_service import loan_book, get_loans_by_member, return_book

def main_menu():
    while True:
        print("\n=== Library System Menu ===")
        print("1. Add new book")
        print("2. Search books by title")
        print("3. Register new member")
        print("4. List all members")
        print("5. Loan book to member")
        print("6. View loans by member")
        print("7. Return book to library")

        print("0. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            title = input("Book title: ")
            author_id = input("Author ID: ")
            genre_id = input("Genre ID: ")
            add_book(title, author_id, genre_id)
            print("Book added successfully.")
        elif choice == "2":
            keyword = input("Enter book title to search: ")
            results = find_books_by_title(keyword)
            for row in results:
                print(f"ID: {row[0]}, Title: {row[1]}, Author: {row[2]}, Genre: {row[3]}")
        elif choice == "3":
            name = input("Member name: ")
            email = input("Member email: ")
            register_member(name, email)
            print("Member registered successfully.")
        elif choice == "4":
            members = get_all_members()
            for m in members:
                print(f"ID: {m[0]}, Name: {m[1]}, Email: {m[2]}")
        elif choice == "5":
            book_id = input("Book ID: ")
            member_id = input("Member ID: ")
            loan_book(book_id, member_id)
            print("Book loaned successfully.")
        elif choice == "6":
            member_id = input("Enter member ID: ")
            loans = get_loans_by_member(member_id)
            for l in loans:
                print(f"Loan ID: {l[0]}, Book: {l[1]}, Loan Date: {l[2]}, Returned: {l[3]}")
        elif choice == "7":
            loan_id = input("Loan ID: ")
            return_book(loan_id)
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")
