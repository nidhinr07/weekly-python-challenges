# Employee Management System

A simple **Employee Management System** built with **Python, SQLite, and Object-Oriented Programming (OOP)**.

This project is a menu-driven console application that allows users to add, view, search, delete, and manage employee information stored in an SQLite database.

## Features

* Add new employees
* View all employees
* View employees with salary of 40,000 or above
* Calculate average employee salary
* Search employee by ID
* Delete employee by ID
* Prevent duplicate employee IDs
* Validate employee age and salary
* Store employee data permanently using SQLite
* Handle invalid user input

## Technologies Used

* **Python**
* **SQLite**
* **sqlite3**
* **Object-Oriented Programming (OOP)**

## Employee Information

Each employee contains:

* Employee ID
* Employee Name
* Employee Age
* Employee Salary

## Project Structure

```text
employee-management-system/
│
├── employee_management.py
├── company.db
└── README.md
```

> `company.db` is automatically created when the program is run for the first time.

## Database

The project uses SQLite with an `employees` table.

```sql
CREATE TABLE employees (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    salary INTEGER NOT NULL
);
```

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/your-username/employee-management-system.git
```

### 2. Open the project folder

```bash
cd employee-management-system
```

### 3. Run the Python program

```bash
python employee_management.py
```

The `company.db` SQLite database will be created automatically.

## Menu

```text
==============================================
          Employee Management System
==============================================
1. Add Employee
2. View All Employees
3. View Employees with Salary >= 40000
4. Show Average Salary
5. Search Employee
6. Delete Employee
7. Exit
==============================================
```

## Example

### Adding an Employee

```text
Enter Employee ID : 1
Enter Employee Name : Nidhin
Enter Employee Age : 22
Enter Employee Salary : 35000

Employee Details Added Successfully
```

### Searching an Employee

```text
Enter Employee ID : 1

--------- Nidhin Details -----------
Employee ID      : 1
Employee Name    : Nidhin
Employee Age     : 22
Employee Salary  : 35000
-----------------------------------------
```

## Validation

The application includes basic validation:

* Employee ID must start from `1`
* Employee IDs must be unique
* Employee name cannot be empty
* Minimum employee age is `18`
* Minimum salary is `1000`
* Invalid numeric input is handled
* Employees that do not exist cannot be deleted

## Learning Objectives

This project was created to practice:

* Python classes and objects
* Methods and object-oriented programming
* SQLite database connectivity
* SQL `CREATE`, `INSERT`, `SELECT`, and `DELETE`
* Parameterized SQL queries
* Database transactions using `commit()`
* Exception handling
* User input validation
* Fetching data using `fetchone()` and `fetchall()`
* Building a menu-driven Python application

## Future Improvements

Possible improvements for future versions:

* Update employee details
* Search employees by name
* Search employees by salary range
* Sort employees by salary
* Add department information
* Add employee joining date
* Create a graphical user interface
* Add login/authentication

## Author

**Nidhin**

This project was created as part of my Python and SQLite practice to improve my understanding of database operations and Object-Oriented Programming.
