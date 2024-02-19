import sqlite3

# Connect to the database
con = sqlite3.connect("ClubHub.db")
cur = con.cursor()
cur.execute("""drop table if exists users""")


# Create the users table
cur.execute("""
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    password TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    user_type TEXT NOT NULL
)
""")


cur.execute("""
CREATE TABLE IF NOT EXISTS clubs (
    club_id INTEGER PRIMARY KEY AUTOINCREMENT,
    club_name  TEXT NOT NULL UNIQUE,
    club_description  TEXT NOT NULL,
    coordinator_id INTEGER,
    club_approval BOOLEAN
)
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS members (
    club_id INTEGER,
    user_id INTEGER,
    user_approval BOOLEAN,
    is_coordinator BOOLEAN,
    FOREIGN KEY (club_id) REFERENCES clubs(club_id),
    FOREIGN KEY (user_id) REFERENCES users(user_id)
)
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS events (
    event_id INTEGER PRIMARY KEY AUTOINCREMENT,
    club_id INTEGER,
    event_title TEXT NOT NULL,
    event_description TEXT NOT NULL,
    event_venue TEXT NOT NULL,
    event_date_time TIMESTAMP NOT NULL,
    FOREIGN KEY (club_id) REFERENCES clubs(club_id)
)
""")




# Insert a sample user
#sample_user = ('john_doe', 'John', 'Doe', 'password123', 'john@example.com', 1, 0, 0)
#cur.execute("""
#INSERT INTO users (username, first_name, last_name, password, email, is_student, is_coordinator, is_admin)
#VALUES ('markSmith', 'mark', 'Smith', 'padwoord', 'email@gmail.com', 1, 0, 1)
#""")


# Commits the transaction
con.commit()
# Closes the connection
con.close()
