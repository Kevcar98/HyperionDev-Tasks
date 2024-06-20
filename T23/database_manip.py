import sqlite3

# Connects to the database (or create it if it doesn't exist)
db = sqlite3.connect("student_db.db")
cursor = db.cursor()

# Creates the table python_programming
cursor.execute('''
CREATE TABLE IF NOT EXISTS python_programming(
    id INTEGER PRIMARY KEY,
    name TEXT,
    grade INTEGER
)
''')
db.commit()

# Checks if the table is empty before inserting new rows
cursor.execute("SELECT COUNT(*) FROM python_programming")
count = cursor.fetchone()[0]

if count == 0:
    # Inserts the new rows into the python_programming table
    students = [
        (55, "Carl Davis", 61),
        (66, "Dennis Fredrickson", 88),
        (77, "Jane Richards", 78),
        (12, "Peyton Sawyer", 45),
        (2, "Lucas Brooke", 99)
    ]

    cursor.executemany('''
    INSERT INTO python_programming(id, name, grade) VALUES(?, ?, ?)
    ''', students)
    db.commit()

# Selects all records with a grade between 60 and 80
cursor.execute('''
SELECT * FROM python_programming WHERE grade BETWEEN 60 AND 80
''')
selected_students = cursor.fetchall()
print("Students with grades between 60 and 80:")
for student in selected_students:
    print(student)

# Changes Carl Davis’s grade to 65
cursor.execute('''
UPDATE python_programming SET grade = 65 WHERE name = 'Carl Davis'
''')
db.commit()

# Deletes Dennis Fredrickson’s row
cursor.execute('''
DELETE FROM python_programming WHERE name = 'Dennis Fredrickson'
''')
db.commit()

# Change the grade of all students with an id greater than 55 to a grade of 80
cursor.execute('''
UPDATE python_programming SET grade = 80 WHERE id > 55
''')
db.commit()

# Retrieve and print all records to verify changes
cursor.execute('''
SELECT * FROM python_programming
''')
all_students = cursor.fetchall()
print("All students:")
for student in all_students:
    print(student)

# Close the database connection
db.close()
