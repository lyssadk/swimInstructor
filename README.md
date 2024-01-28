# Overview
This program I wrote is intended to make accessing a swim instructors schedule and identifying what skills a student is working on easier for the instructors at a previous job of mine. It uses python's sqlite, and keeps track of the schedule, students, instructors, and skills students have. 

When it runs it will display a menu and ask you to enter your first option (View instructors, view students, view schedule, or quit). As you click on each respectfully it will display a different menu of things you can do with the tables from the database (CRUD operations).

My purpose is to make it much faster process to gain the information needed before lessons, consolidating the information to one database. Currently at the job we have 3 different places we have to go to get our need information and it takes like 15-25 min. Ideally it should take a few minutes.

[Software Demo Video](https://youtu.be/2dO6laibdVU)

# Relational Database

I decided to use SQLite3 from Python to build my relational database, in the file swim.db

Currently it has 5 tables: instructors, students, schedule, specific skills, and student has skills.
Ideally in the future it will have a parents table to document that information as well. 

Instructors keeps track of the pay, names, & hours per week worked of the employees
Students keeps track of birthday, names, and skill level of the child (we have like 5 classifications)
Specific Skills keeps track of the individual skills we teach and want students to acquire
Student has Skills right now just attaches a skill to a student, in the future i want to add a true or false so we can see
where they are at better
Schedule keeps track of the days and times of appointments, right now its not perfect, but with some more fixes it'll get there:)


# Development Environment

Visual Studio Code (IDE)
Python (LANGUAGE)
SQLite3 (LIBRARY)


# Useful Websites

{Make a list of websites that you found helpful in this project}

- [Web Site Name](https://www.sqlitetutorial.net)
- [Web Site Name](https://www.sqlite.org/lang_datefunc.html)

# Future Work
- Figure out how to filter by age
- Add in parents information table
- Make the display of information more organized and readable.
- True or False for all the skills and attach all those skills to a student
