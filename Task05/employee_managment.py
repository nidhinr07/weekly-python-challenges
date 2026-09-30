import sqlite3

connection = sqlite3.connect("company.db")
cursor = connection.cursor()


# Table Creation
cursor.execute("""
    CREATE TABLE IF NOT EXISTS employees (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        age INTEGER NOT NULL,
        salary INTEGER NOT NULL
    )
""")

connection.commit()


class Employee:

    def menu(self):
        print("\n==============================================")
        print("          Employee Management System")
        print("==============================================")
        print("1. Add Employee")
        print("2. View All Employees")
        print("3. View Employees with Salary >= 40000")
        print("4. Show Average Salary")
        print("5. Search Employee")
        print("6. Delete Employee")
        print("7. Exit")
        print("==============================================")

    def add_employee(self):
        try:
            print("\n------------------------")
            print("Fill This Details")
            print("------------------------")

            employee_id = int(input("Enter Employee ID : "))

            if employee_id <= 0:
                print("Employee ID Starts From 1")
                return

            # Check whether employee already exists
            cursor.execute(
                "SELECT * FROM employees WHERE id = ?",
                (employee_id,)
            )

            employee = cursor.fetchone()

            if employee:
                print("Employee with this ID already exists :(")
                return

            name = input("Enter Employee Name : ").strip()

            if not name:
                print("Employee Name Cannot Be Empty")
                return

            age = int(input("Enter Employee Age : "))

            if age < 18:
                print("Minimum Age Must Be 18 or Above")
                return

            salary = int(input("Enter Employee Salary : "))

            if salary < 1000:
                print("Minimum Salary Is 1000")
                return

            cursor.execute("""
                INSERT INTO employees (id, name, age, salary)
                VALUES (?, ?, ?, ?)
            """, (employee_id, name, age, salary))

            connection.commit()

            print("\nEmployee Details Added Successfully")

        except ValueError:
            print("\nPlease Enter Valid Numbers.")

        except Exception as e:
            print(f"\nError : {e}")

    def view_employees(self):
        try:
            print("\n--------------- All Employee Details -----------------")

            cursor.execute("SELECT * FROM employees")
            employees = cursor.fetchall()

            if not employees:
                print("No Employee Details Found :(")
                return

            for employee in employees:
                print(f"\n--------- {employee[1]} Details -----------")
                print(f"Employee ID      : {employee[0]}")
                print(f"Employee Name    : {employee[1]}")
                print(f"Employee Age     : {employee[2]}")
                print(f"Employee Salary  : {employee[3]}")
                print("-----------------------------------------")

        except Exception as e:
            print(f"Error : {e}")

    def view_employees_based_on_salary(self):
        try:
            print(
                "\n--------------- Employees With Salary >= 40000 -----------------"
            )

            cursor.execute(
                "SELECT * FROM employees WHERE salary >= 40000"
            )

            employees = cursor.fetchall()

            if not employees:
                print("No Employee Details Found :(")
                return

            for employee in employees:
                print(f"\n--------- {employee[1]} Details -----------")
                print(f"Employee ID      : {employee[0]}")
                print(f"Employee Name    : {employee[1]}")
                print(f"Employee Age     : {employee[2]}")
                print(f"Employee Salary  : {employee[3]}")
                print("-----------------------------------------")

        except Exception as e:
            print(f"Error : {e}")

    def average_salary(self):
        try:
            print("\n---------------- Average Salary ----------------\n")

            cursor.execute("SELECT AVG(salary) FROM employees")
            avg = cursor.fetchone()[0]

            if avg is None:
                print("No Employee Details Found :(")
            else:
                print(f"Average Salary of Employees : {avg:.2f}")

        except Exception as e:
            print(f"Error : {e}")

    def search_employees(self):
        try:
            print("\n--------------- Search Employee Details -----------------")

            emp_id = int(input("Enter Employee ID : "))

            cursor.execute(
                "SELECT * FROM employees WHERE id = ?",
                (emp_id,)
            )

            employee = cursor.fetchone()

            if not employee:
                print("No Employee Details Found :(")
                return

            print(f"\n--------- {employee[1]} Details -----------")
            print(f"Employee ID      : {employee[0]}")
            print(f"Employee Name    : {employee[1]}")
            print(f"Employee Age     : {employee[2]}")
            print(f"Employee Salary  : {employee[3]}")
            print("-----------------------------------------")

        except ValueError:
            print("Please Enter a Valid Employee ID.")

        except Exception as e:
            print(f"Error : {e}")

    def delete_employee(self):
        try:
            print("\n--------------- Delete Employee Details -----------------")

            emp_id = int(input("Enter Employee ID : "))

            # Check employee before deleting
            cursor.execute(
                "SELECT * FROM employees WHERE id = ?",
                (emp_id,)
            )

            employee = cursor.fetchone()

            if not employee:
                print("No Employee Found With This ID.")
                return

            cursor.execute(
                "DELETE FROM employees WHERE id = ?",
                (emp_id,)
            )

            connection.commit()

            print("\nEmployee Deleted Successfully")

        except ValueError:
            print("Please Enter a Valid Employee ID.")

        except Exception as e:
            print(f"Error : {e}")

    def run(self):

        while True:
            try:
                self.menu()

                choice = int(input("Enter Your Choice : "))

                if choice < 1 or choice > 7:
                    print("Invalid Choice. Choose an Option From 1-7.")
                    continue

                if choice == 1:
                    self.add_employee()

                elif choice == 2:
                    self.view_employees()

                elif choice == 3:
                    self.view_employees_based_on_salary()

                elif choice == 4:
                    self.average_salary()

                elif choice == 5:
                    self.search_employees()

                elif choice == 6:
                    self.delete_employee()

                elif choice == 7:
                    print("\nThanks for Using Our Employee Management System :)")
                    break

            except ValueError:
                print("\nPlease Enter a Valid Number.")

            except Exception as e:
                print(f"\nError : {e}")



emp = Employee()


emp.run()

connection.close()
