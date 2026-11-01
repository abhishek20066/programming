import pymysql

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="MyFee@Track#82sun"
)

cursor = connection.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS tuition_fee_db")
connection.commit()
cursor.close()
connection.close()

conn = pymysql.connect(
    host="localhost",
    user="root",
    password="MyFee@Track#82sun",
    database="tuition_fee_db"
)

cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100),
        class_name VARCHAR(50),
        monthly_fee INT
    )
""")

conn.commit()
print("Table ready")


def add_student(name, class_name, monthly_fee):
    sql = "INSERT INTO students (name, class_name, monthly_fee) VALUES (%s, %s, %s)"
    cursor.execute(sql, (name, class_name, monthly_fee))
    conn.commit()
    print("Student added successfully")


def view_students():
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()

    if rows:
        print("\nID   Name          Class          Monthly Fee")
        print("---------------------------------------------")
        for row in rows:
            print(f"{row[0]:<5}{row[1]:<14}{row[2]:<15}{row[3]}")
    else:
        print("No students found")


def search_by_class(class_name):
    cursor.execute("SELECT * FROM students WHERE class_name = %s", (class_name,))
    rows = cursor.fetchall()

    if rows:
        print("\nID   Name          Class          Monthly Fee")
        print("---------------------------------------------")
        for row in rows:
            print(f"{row[0]:<5}{row[1]:<14}{row[2]:<15}{row[3]}")
    else:
        print("No students found")


def update_fee(student_id, new_fee):
    cursor.execute(
        "UPDATE students SET monthly_fee = %s WHERE id = %s",
        (new_fee, student_id)
    )
    conn.commit()

    if cursor.rowcount == 0:
        print("No such student")
    else:
        print("Fee updated successfully")


def delete_student(student_id):
    cursor.execute(
        "DELETE FROM students WHERE id = %s",
        (student_id,)
    )
    conn.commit()

    if cursor.rowcount == 0:
        print("No such student")
    else:
        print("Student deleted successfully")


while True:
    print("\n1. Add student")
    print("2. View all students")
    print("3. Search by class")
    print("4. Update fee")
    print("5. Delete student")
    print("0. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        class_name = input("Enter class: ")
        monthly_fee = int(input("Enter monthly fee: "))
        add_student(name, class_name, monthly_fee)

    elif choice == "2":
        view_students()

    elif choice == "3":
        class_name = input("Enter class name: ")
        search_by_class(class_name)

    elif choice == "4":
        student_id = int(input("Enter student ID: "))
        new_fee = int(input("Enter new fee: "))
        update_fee(student_id, new_fee)

    elif choice == "5":
        student_id = int(input("Enter student ID: "))
        delete_student(student_id)

    elif choice == "0":
        break

    else:
        print("Invalid choice")

cursor.close()
conn.close()