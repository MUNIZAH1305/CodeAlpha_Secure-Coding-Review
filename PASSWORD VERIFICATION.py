def login_user(username, password):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    cursor.execute("SELECT password FROM users WHERE username = ?", (username,))
    result = cursor.fetchone()

    conn.close()

    # Verify hashed password
    if result and bcrypt.checkpw(password.encode('utf-8'), result[0]):
        print("Login successful!")
    else:
        print("Invalid username or password.")
