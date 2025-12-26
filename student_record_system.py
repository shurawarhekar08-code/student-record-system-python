import sqlite3
import webbrowser
import os

# ---------------- DATABASE SETUP ----------------
conn = sqlite3.connect("students.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    roll TEXT,
    course TEXT
)
""")
conn.commit()

# ---------------- ADD STUDENT ----------------
def add_student():
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")
    course = input("Enter course: ")

    cursor.execute(
        "INSERT INTO students (name, roll, course) VALUES (?, ?, ?)",
        (name, roll, course)
    )
    conn.commit()
    print("✅ Student added successfully!")

# ---------------- GENERATE HTML ----------------
def generate_html():
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()

    html_content = """
    <html>
    <head>
        <title>Student Records</title>
        <style>
            body { font-family: Arial; margin: 40px; }
            table { border-collapse: collapse; width: 60%; }
            th, td { border: 1px solid black; padding: 8px; text-align: center; }
            th { background-color: #f2f2f2; }
        </style>
    </head>
    <body>
        <h2>Student Record Management System</h2>
        <table>
            <tr>
                <th>ID</th>
                <th>Name</th>
                <th>Roll</th>
                <th>Course</th>
            </tr>
    """

    for s in students:
        html_content += f"""
        <tr>
            <td>{s[0]}</td>
            <td>{s[1]}</td>
            <td>{s[2]}</td>
            <td>{s[3]}</td>
        </tr>
        """

    html_content += """
        </table>
    </body>
    </html>
    """

    with open("students.html", "w", encoding="utf-8") as file:
        file.write(html_content)

    webbrowser.open("file://" + os.path.realpath("students.html"))

# ---------------- MAIN MENU ----------------
while True:
    print("\n--- Student Record System ---")
    print("1. Add Student")
    print("2. View Students (HTML)")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        generate_html()
    elif choice == "3":
        print("👋 Exiting program")
        break
    else:
        print("❌ Invalid choice")

conn.close()
