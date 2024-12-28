import sqlite3
import hashlib

# Database setup
def initialize_db():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT)''')
    conn.commit()
    conn.close()

# User registration
def register_user(username, password):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    # Vulnerable: Directly stores the password without hashing
    cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
    conn.commit()
    conn.close()
    print(f"User '{username}' registered successfully.")

# User login
def login_user(username, password):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    # Vulnerable: Plain-text password comparison
    cursor.execute("SELECT password FROM users WHERE username = ?", (username,))
    result = cursor.fetchone()

    conn.close()

    if result and result[0] == password:
        print("Login successful!")
    else:
        print("Invalid username or password.")

# Main program
def main():
    initialize_db()
    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            username = input("Enter a username: ")
            password = input("Enter a password: ")
            register_user(username, password)
        elif choice == "2":
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            login_user(username, password)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
