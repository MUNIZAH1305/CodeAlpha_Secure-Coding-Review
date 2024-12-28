import bcrypt

def register_user(username, password):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    # Hash the password with bcrypt
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
    conn.commit()
    conn.close()
    print(f"User '{username}' registered successfully.")
