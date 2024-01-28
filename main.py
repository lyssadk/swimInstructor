import sqlite3

connection = sqlite3.connect('swim.db')
cursor = connection.cursor()

# # create tables
# cursor.execute("CREATE TABLE IF NOT EXISTS instructors (instructors_id INTEGER PRIMARY KEY NOT NULL, first_name VARCHAR(30) NOT NULL, last_name VARCHAR(30), hourlyWage DECIMAL(10,0) NOT NULL, hoursPerWeek DECIMAL(10,0) NOT NULL)")
# cursor.execute("CREATE TABLE IF NOT EXISTS students (student_id1 INTEGER PRIMARY KEY NOT NULL, first_name VARCHAR(30) NOT NULL, last_name VARCHAR(30) NOT NULL, birthday DATE NOT NULL, level VARCHAR(30) NOT NULL)")
# cursor.execute("CREATE TABLE IF NOT EXISTS specific_skills (skill_id INTEGER PRIMARY KEY NOT NULL, skill_name VARCHAR(30) NOT NULL, skill_description VARCHAR(45) NOT NULL)")
# cursor.execute("CREATE TABLE IF NOT EXISTS schedule (schedule_id INTEGER PRIMARY KEY NOT NULL, day VARCHAR(30) NOT NULL, time TIME NOT NULL, instructor_id INTEGER NOT NULL, student_id INTEGER NOT NULL, skill_id INTEGER NOT NULL, FOREIGN KEY (instructor_id) REFERENCES instructors(instructors_id), FOREIGN KEY (student_id) REFERENCES students(student_id1), FOREIGN KEY (skill_id) REFERENCES specific_skills(skill_id))")
# cursor.execute("CREATE TABLE IF NOT EXISTS student_has_skill (student_id INTEGER NOT NULL, skill_id INTEGER NOT NULL, FOREIGN KEY (student_id) REFERENCES students(student_id1), FOREIGN KEY (skill_id) REFERENCES specific_skills(skill_id))")

# # # insert student_has_skill
# cursor.execute("INSERT INTO student_has_skill (student_id, skill_id) VALUES (1, 1)")
# cursor.execute("INSERT INTO student_has_skill (student_id, skill_id) VALUES (1, 2)")
# cursor.execute("INSERT INTO student_has_skill (student_id, skill_id) VALUES (2, 1)")
# cursor.execute("INSERT INTO student_has_skill (student_id, skill_id) VALUES (2, 2)")
# cursor.execute("INSERT INTO student_has_skill (student_id, skill_id) VALUES (2, 3)")
# cursor.execute("INSERT INTO student_has_skill (student_id, skill_id) VALUES (2, 5)")
# cursor.execute("INSERT INTO student_has_skill (student_id, skill_id) VALUES (3, 3)")
# cursor.execute("INSERT INTO student_has_skill (student_id, skill_id) VALUES (3, 4)")
# cursor.execute("INSERT INTO student_has_skill (student_id, skill_id) VALUES (4, 1)")
# cursor.execute("INSERT INTO student_has_skill (student_id, skill_id) VALUES (4, 2)")

# # # insert schedule
# cursor.execute("INSERT INTO schedule (day, time, instructor_id, student_id, skill_id) VALUES ('Monday', '10:00', 1, 2, 1)")
# cursor.execute("INSERT INTO schedule (day, time, instructor_id, student_id, skill_id) VALUES ('Monday', '10:20', 1, 2, 2)")
# cursor.execute("INSERT INTO schedule (day, time, instructor_id, student_id, skill_id) VALUES ('Monday', '10:40', 1, 2, 3)")
# cursor.execute("INSERT INTO schedule (day, time, instructor_id, student_id, skill_id) VALUES ('Monday', '11:00', 1, 2, 4)")
# cursor.execute("INSERT INTO schedule (day, time, instructor_id, student_id, skill_id) VALUES ('Monday', '11:20', 1, 1, 1)")
# cursor.execute("INSERT INTO schedule (day, time, instructor_id, student_id, skill_id) VALUES ('Monday', '11:40', 1, 1, 2)")
# cursor.execute("INSERT INTO schedule (day, time, instructor_id, student_id, skill_id) VALUES ('Monday', '12:00', 1, 1, 3)")

# cursor.execute("INSERT INTO schedule (day, time, instructor_id, student_id, skill_id) VALUES ('Tuesday', '12:20', 2, 1, 4)")
# cursor.execute("INSERT INTO schedule (day, time, instructor_id, student_id, skill_id) VALUES ('Tuesday', '12:40', 2, 3, 1)")   
# cursor.execute("INSERT INTO schedule (day, time, instructor_id, student_id, skill_id) VALUES ('Tuesday', '1:00', 2, 2, 2)")
# cursor.execute("INSERT INTO schedule (day, time, instructor_id, student_id, skill_id) VALUES ('Tuesday', '1:20', 2, 1, 3)")
# cursor.execute("INSERT INTO schedule (day, time, instructor_id, student_id, skill_id) VALUES ('Tuesday', '1:40', 2, 4, 4)")    

# # # insert instructors
# cursor.execute("INSERT INTO instructors (first_name, last_name, hourlyWage, hoursPerWeek) VALUES ('Alyssa', 'Kucharyski', 15, 20)")
# cursor.execute("INSERT INTO instructors (first_name, last_name, hourlyWage, hoursPerWeek) VALUES ('Olivia', 'Black', 14, 15)")
# cursor.execute("INSERT INTO instructors (first_name, last_name, hourlyWage, hoursPerWeek) VALUES ('Megan', 'Target', 14, 15)")

# # # insert students
# cursor.execute("INSERT INTO students (first_name, last_name, birthday, level) VALUES ('Sam', 'Owens', '2020-01-01', 'Basic Safety')")
# cursor.execute("INSERT INTO students (first_name, last_name, birthday, level) VALUES ('Millie', 'Franz', '2019-01-01', 'Transition')")
# cursor.execute("INSERT INTO students (first_name, last_name, birthday, level) VALUES ('Melvian', 'Barbarian', '2022-03-03', 'Pre-Transition')")    
# cursor.execute("INSERT INTO students (first_name, last_name, birthday, level) VALUES ('Celeste', 'Teal', '2017-01-01', 'Swim Team Prep')")

# # # insert specific skills
# cursor.execute("INSERT INTO specific_skills (skill_name, skill_description) VALUES ('Front Float', 'Float on front for 5 seconds')")    
# cursor.execute("INSERT INTO specific_skills (skill_name, skill_description) VALUES ('Back Float', 'Float on back for 60 seconds')")
# cursor.execute("INSERT INTO specific_skills (skill_name, skill_description) VALUES ('Front Glide', 'Glide on front for 2 body lengths')")
# cursor.execute("INSERT INTO specific_skills (skill_name, skill_description) VALUES ('Back Glide', 'Glide on back for 2 body lengths')")
# cursor.execute("INSERT INTO specific_skills (skill_name, skill_description) VALUES ('Front Swim', 'Swim on front for 2 body lengths')")
# cursor.execute("INSERT INTO specific_skills (skill_name, skill_description) VALUES ('Back Swim', 'Swim on back for 2 body lengths')")

# connection.commit()

console_clear = lambda: print('\n' * 5)

#############################################
# Instructors
#############################################
def get_instructors(cursor): 
    console_clear()
    while True:
        print("Please select an option below:") 
        print("1. Search instructor by name")
        print("2. View ALL instructors")
        print("3. Add instructor")
        print("4. Delete instructor")
        print("5. Update instructor")
        print("6. Exit")
        choice = input("Enter your choice(1-6): ")
        if choice == "1":
            get_instructors_by_name(cursor)
        elif choice == "2":
            get_instructors_all(cursor)
        elif choice == "3":
            add_instructor(cursor)
        elif choice == "4":
            delete_instructor(cursor)
        elif choice == "5":
            update_instructor(cursor)
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")

# works
def get_instructors_all(cursor):
    cursor.execute("SELECT * FROM instructors")
    results = cursor.fetchall()
    for i in results:
        print(i[1] + " " + i[2] + " $" + str(i[3]) + " per hour | Hours:" + str(i[4]))

# works
def get_instructors_by_name(cursor):    
    instructor_statement = "SELECT * FROM instructors WHERE first_name = '%s'"
    first_name = input("Enter first name: ").capitalize()
    cursor.execute(instructor_statement % first_name)
    results = cursor.fetchall()
    for i in results:
        print(i[1] + " " + i[2] + " $" + str(i[3]) + " per hour | Hours:" + str(i[4]))

# works 
def add_instructor(cursor):
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    hourlyWage = input("Enter hourly wage: ")
    hoursPerWeek = input("Enter hours per week: ")
    cursor.execute("INSERT INTO instructors (first_name, last_name, hourlyWage, hoursPerWeek) VALUES ('%s', '%s', '%s', '%s')" % (first_name, last_name, hourlyWage, hoursPerWeek))
    connection.commit()

# works
def delete_instructor(cursor):
    instructor_id = input("Enter instructor id: ")
    cursor.execute("DELETE FROM instructors WHERE instructors_id = '%s'" % instructor_id)
    connection.commit()

#fix this one for sure & test
def update_instructor(cursor):
    instructor_id = input("Enter instructor id: ")
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    hourlyWage = input("Enter hourly wage: ")
    hoursPerWeek = input("Enter hours per week: ")
    cursor.execute("UPDATE instructors SET first_name = '%s', last_name = '%s', hourlyWage = '%s', hoursPerWeek = '%s' WHERE instructors_id = %s" % (first_name, last_name, hourlyWage, hoursPerWeek, instructor_id))


#############################################
# Students
#############################################
def get_students(cursor): 
    console_clear()
    while True:
        print("Please select an option below:") 
        print("1. Search student by name")
        print("2. View ALL students")
        print("3. Add student")
        print("4. Delete student")
        print("5. Update Student")
        print("5. Exit")
        choice = input("Enter your choice(1-6): ")
        if choice == "1":
            get_students_by_name(cursor)
        elif choice == "2":
            get_students_all(cursor)
        elif choice == "3":
            add_student(cursor)
        elif choice == "4":
            delete_student(cursor)
        elif choice == "5":
            update_student(cursor)
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")


# works
def get_students_by_name(cursor):
    student_statement = "SELECT * FROM students WHERE first_name='%s'"
    first_name = input("Enter first name:").capitalize()
    cursor.execute(student_statement%first_name)
    results = cursor.fetchall()
    for i in results:
        print(i[1] + " " + i[2] + " " + i[3] + " " + i[4])

# works
def get_students_all(cursor):
    cursor.execute("SELECT * FROM students")
    results = cursor.fetchall()
    for i in results:
        print(i[1] + " " + i[2] + " " + i[3] + " " + i[4])

# works
def add_student(cursor):
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    birthday = input("Enter birthday: ")
    level = input("Enter level: ")
    cursor.execute("INSERT INTO students (first_name, last_name, birthday, level) VALUES ('%s', '%s', '%s', '%s')" % (first_name, last_name, birthday, level))
    connection.commit()

# works like a charm  
def delete_student(cursor):
    student_id = input("Enter student id: ")
    cursor.execute("DELETE FROM students WHERE student_id1 = '%s'" % student_id)
    connection.commit()

def update_student(cursor):
    student_id = input("Enter student id: ")
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    birthday = input("Enter birthday: ")
    level = input("Enter level: ")
    cursor.execute("UPDATE students SET first_name = '%s', last_name = '%s', birthday = '%s', level = '%s' WHERE student_id1 = %s" % (first_name, last_name, birthday, level, student_id))
    connection.commit()

#############################################
# Schedule
#############################################
def get_schedule(cursor): 
    console_clear()
    while True:
        print("Please select an option below:") 
        print("1. View Schedule by Day")
        print("2. View Schedule by Instructor")
        print("3. Add Schedule")
        print("4. Delete Schedule")
        print("5. Update Schedule")
        print("6. Exit")
        choice = input("Enter your choice(1-4): ")
        if choice == "1":
            get_schedule_by_day(cursor)
        elif choice == "2":
            get_schedule_by_instructor(cursor)
        elif choice == "3":
            add_schedule(cursor)
        elif choice == "4":
            delete_schedule(cursor)
        elif choice == "5":
            update_schedule(cursor)
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")

# slays
def get_schedule_by_day(cursor):
    day_statement = "SELECT * FROM schedule WHERE day = '%s'"
    day = input("Enter day: ")
    cursor.execute(day_statement % day)
    results = cursor.fetchall()
    for i in results:
        print(i[1] + " " + i[2] + " | "+ get_instructor_name(cursor, i[3])+ " | " + get_student_name(cursor, i[4]) + " skill level: " + str(i[5]))

# works 
def get_schedule_by_instructor(cursor):
    instructor_statement = "SELECT * FROM schedule WHERE instructor_id = '%s'"
    instructor_id = input("Enter instructor id: ")
    cursor.execute(instructor_statement % instructor_id)
    results = cursor.fetchall()
    print(get_instructor_name(cursor, instructor_id))
    for i in results:
        print( str(i[1]) + " " + i[2] + "| " +  get_student_name(cursor, i[4]) + " skill level: " + str(i[5]))
        print("Skills Working On: ")
        show_student_skills(cursor, i[4])

def get_instructor_name(cursor, instructor_id):
    cursor.execute("SELECT * FROM instructors WHERE instructors_id = '%s'" % instructor_id)
    results = cursor.fetchone()
    return results[1] + " " + results[2] + " "

def get_student_name(cursor, student_id):
    cursor.execute("SELECT * FROM students WHERE student_id1 = '%s'" % student_id)
    results = cursor.fetchone()
    return results[1] + " " + results[2] + " "

def show_student_skills(cursor, student_id):
    cursor.execute("SELECT * FROM student_has_skill WHERE student_id = '%s'" % student_id)
    results = cursor.fetchall()
    for i in results:
        print(print_skillz(cursor, i[1]))

def print_skillz(cursor, skill_id):
    cursor.execute("SELECT * FROM specific_skills WHERE skill_id = '%s'" % skill_id)
    results = cursor.fetchone()
    return results[2] + " "

# works
def add_schedule(cursor):
    day = input("Enter day: ")
    time = input("Enter time: ")
    instructor_id = input("Enter instructor id: ")
    student_id = input("Enter student id: ")
    skill_id = input("Enter skill id: ")
    cursor.execute("INSERT INTO schedule (day, time, instructor_id, student_id, skill_id) VALUES ('%s', '%s', '%s', '%s', '%s')" % (day, time, instructor_id, student_id, skill_id))
    connection.commit()

# check
def delete_schedule(cursor):
    schedule_id = input("Enter schedule id: ")
    cursor.execute("DELETE FROM schedule WHERE schedule_id = '%s'" % schedule_id)
    connection.commit()


# check
def update_schedule(cursor):
    schedule_id = input("Enter schedule id: ")
    day = input("Enter day: ")
    time = input("Enter time: ")
    instructor_id = input("Enter instructor id: ")
    student_id = input("Enter student id: ")
    skill_id = input("Enter skill id: ")
    cursor.execute("UPDATE schedule SET day = '%s', time = '%s', instructor_id = '%s', student_id = '%s', skill_id = '%s' WHERE schedule_id = %s" % (day, time, instructor_id, student_id, skill_id, schedule_id))
    connection.commit()

def menu():
    while True:
        console_clear()
        print("Welcome to SwimDB")
        print("Please select an option below:") 
        print("1. View Instructors")
        print("2. View Students")
        print("3. View Schedule")
        print("4. Exit")
        choice = input("Enter your choice(1-4): ")
        if choice == "1":
            get_instructors(cursor)
        elif choice == "2":
            get_students(cursor)
        elif choice == "3":
            get_schedule(cursor)
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

menu()

connection.close()  