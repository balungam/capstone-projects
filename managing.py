import datetime
from collections import Counter


# In this project we will create a program that will manage txt files
# It will also give the users the ability to manage their tasks.
# The program will allow users to access information from the tasks.txt.
# The program will also generate reports.
# The user.txt will be used to save users and their passwords,
# the user.txt will also be used for access control.

# I imported the datetime so that i can use it for the "current date"

# I created a function to create a new user.
# If te user exists the program will output an error.
def reg_user():
    create_user = open("user.txt", "r+")
    username = input("Enter new username: ")

    for line in create_user:
        user, passcode = line.split(",")
        if username == user:
            print("User already exists try again")
            reg_user()

    password = input("Enter password for new user: ")
    confirm_password = input("Confirm password: ")
    if password == confirm_password:
        create_user.write("\n")
        create_user.write(username)
        create_user.write(",")
        create_user.write(" ")
        create_user.write(password)
        create_user.close()
    else:
        print("Passwords don't match")

# I created a function that will add a new task.
def add_task():
    print("add task")
    # The program will ask the user to input the said info.
    username = input("The task is assigned to (Username): ")
    title_of_task = input("Enter the title of the task: ")
    description_of_task = input("The description of the task: ")
    due_date = input("Enter the due date: ")
    current_date = datetime.datetime.today().strftime('%d %b %y')
    Completed = "No"
    # The program will then write the info on the tasks.txt file.
    task_file = open("tasks.txt", "a")
    task_file.write("\n")
    task_file.write(username)
    task_file.write(", ")
    task_file.write(title_of_task)
    task_file.write(", ")
    task_file.write(description_of_task)
    task_file.write(", ")
    task_file.write(current_date)
    task_file.write(", ")
    task_file.write(due_date)
    task_file.write(", ")
    task_file.write(Completed)
    task_file.close()

# I created a function that will allow the user to view, their tasks.
def view_all():
    print("view all tasks\n")

    mylines = []

    with open("tasks.txt", "r") as myfile:
        # The program will read the tasks.txt file line by line,
        # and will print out the task information.
        for myline in myfile:
            mylines.append(myline)
            element = myline.split(",")
            username = element[0]
            tasks1 = element[1]
            tasks2 = element[2]
            current_date = element[3]
            due_date = element[4]
            complete = element[5]
            print("Username:", "\t\t ", username)
            print("Title of task:", "\t\t", tasks1)
            print("Description of task:", "\t", tasks2)
            print("Current date:", "\t\t", current_date)
            print("due_date:", "\t\t", due_date)
            print("Complete (Yes/No):", "\t", complete, "\n")

# I created a function for te user to view their specific task.
def view_mine():
    print("view my tasks")
    myfile = open("tasks.txt", "r+")
    data = myfile.readlines()

    for j, row in enumerate(data):
        user, task_title, task_description, date, due_date, complete = row.split(",")
        if username == user:
            print("Task number", str(j))
            print("Username:", "\t\t ", user)
            print("Title of task:", "\t\t", task_title)
            print("Description of task:", "\t", task_description)
            print("Current date:", "\t\t", date)
            print("due_date:", "\t\t", due_date)
            print("Complete (Yes/No):", "\t", complete, "\n")

            select_id = int(input("Please enter task number: "))
            if select_id == j:
                user, task_title, task_description, date, due_date, complete = row.split(",")
                change_user = input("Do you want to change the user? (YES/NO) ").lower()

                if change_user == "yes":
                    new_user = input("Enter new user: ")
                    row = row.replace(user, new_user)
                    print(row)
                    data[j] = row

                change_date = input("Do you want to change the due date? (YES/NO) ").lower()

                if change_date == "yes":
                    new_date = input("Enter new due date: ")
                    row = row.replace(due_date, new_date)
                    print(row)
                    data[j] = row

                progress = input("Do you want to edit the task progress (YES/NO) ")

                if progress == "yes":
                    change_progress = input("Confirm if the task is complete or not (YES/NO) ").capitalize()
                    row = row.replace(complete, change_progress)
                    print(row)
                    data[j] = row

    print("****    ****   ***")
    print(data)
    myfile.write(data)
    myfile.close()

# This function will generate two txt reports,
# one reports for the task's statistics,
# the other for the user's statistics.
def generate_reports():
    with open("tasks.txt", "r+") as report_one:
        data = report_one.readlines()
        task_due_date = datetime.datetime.today().strftime('%d %b %y')

        # I used empty variables to create lists, dictionaries and counters.
        data_list = []
        user_task_count = []
        task_count = 0
        uncompleted = 0
        completed = 0
        overdue = 0
        user_info = {}
        # I used a for loop to iterate over the task file to get,
        # the statistics of the tasks and generate a report.
        for i in data:
            user, task_title, task_description, date, due_date, complete = i.split(",")
            user_task_count.append(user)
            data_list.append(i)
            task_count += 1
            progress = complete.strip()
            if progress == "No":
                uncompleted += 1
                if due_date < task_due_date:
                    overdue += 1
            elif progress == "Yes":
                completed += 1
            for j in data:
                user_info[user] = list()
                user_info[user].extend(progress)

        percent_incomplete = (uncompleted / task_count) * 100
        percent_complete = (completed / task_count) * 100

        # these are the print outs of the said statistics
        print("Task overview  ")
        print("The total number of tasks", task_count)
        print("The number of completed tasks", completed)
        print("The number of uncompleted tasks", uncompleted)
        print("The number of overdue tasks", overdue)
        print("The percentage of incomplete tasks: ", percent_incomplete)
        print("The percentage of overdue tasks: ", percent_complete)

        # all that information will be written onto a text file.
        task_report = open("task_overview.txt", "w")
        task_report.write("---Task overview---\n")
        task_report.write(f"The total number of tasks {task_count} \n")
        task_report.write(f"The number of completed tasks {completed} \n")
        task_report.write(f"The number of uncompleted tasks {uncompleted} \n")
        task_report.write(f"The number of overdue tasks {overdue} \n")
        task_report.write(f"The percentage of incomplete tasks: {percent_incomplete} \n")
        task_report.write(f"The percentage of overdue tasks: {percent_complete}")
        task_report.close()

    with open("user.txt", "r+") as report_two:
        user_data = report_two.readlines()

        user_list = []

        for name in user_data:
            name, password = name.split(",")
            user_list.append(name)

        print("The total number of users : ", len(user_list))
        print("The total number of tasks generated", task_count)

        user_report = open("user_overview.txt", "w")
        user_report.write("---User overview---\n")
        user_report.write(f"The total number of users {len(user_list)} \n")
        user_report.write(f"The total number of tasks generated {task_count} \n")
        user_report.close()

        with open("tasks.txt", "r+") as report_one:
            data = report_one.readlines()

            for i in user_list:
                total_tasks = 0
                not_done = 0
                done = 0
                passed_duedate = 0
                for j in data:
                    user, task_title, task_description, date, due_date, complete = j.split(",")
                    if i == user:
                        total_tasks += 1
                        complete = complete.strip()
                        if complete == "No":
                            not_done += 1
                        elif complete == "Yes":
                            done += 1
                        if due_date < task_due_date:
                            passed_duedate += 1

                print("User: ", i, "\n    Total tasks: ", total_tasks,
                      "\n    Percentage of tasks", (total_tasks / task_count) * 100,
                      "\n    Percentage of completed tasks", (done / total_tasks) * 100,
                      "\n    Percentage of incomplete tasks", (not_done / total_tasks) * 100,
                      "\n    Percentage of overdue tasks", (passed_duedate / total_tasks) * 100)
                user_report = open("user_overview.txt", "a")
                user_report.write(f"\nUsername : {i} \n")
                user_report.write(f"Total tasks, {total_tasks} \n")
                user_report.write(f"Percentage of tasks, {(total_tasks / task_count) * 100} \n")
                user_report.write(f"Percentage of completed tasks, {(done / total_tasks) * 100} \n")
                user_report.write(f"Percentage of incomplete tasks, {(not_done/ total_tasks) * 100} \n")
                user_report.write(f"Percentage of overdue tasks, {(passed_duedate / total_tasks) * 100} \n")
                user_report.close()

logged_in = True

while logged_in:
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    username = username.strip()
    password = password.strip()
    for line in open("user.txt", "r").readlines():
        login_info = line.split(",")
        if username == login_info[0] and password == login_info[1].strip(" \n"):
            print("\nLogin successful!!")
            logged_in = False
            login = True
            break
    # the while loop will break once the input is found in the user.txt file
    # If the input is not in the file, the user will get an error.
    if username != login_info[0]:
        print("User doesn't exist or Password entered is incorrect")

# If the user logs in successfully the user will get some options.

if login == True:
    if username == "admin":
        options = input("""\nPlease select one of the following options:
    r - register user
    a - add task
    va view all tasks
    vm - view my tasks
    gr - generate reports
    ds - display statistics
    e - exit
    Enter your selection here : """).lower()
    else:
        options = input("""\nPlease select one of the following options:
    r - register user
    a - add task
    va view all tasks
    vm - view my tasks
    e - exit
    Enter your selection here : """).lower()

# The first option will allow the "admin" to register users.
if options == "r":
    if username == "admin":
        reg_user()
    else:
        print("Only the Admin is allowed to register users.")

# The second option will allow all the users to add tasks.
if options == "a":
    add_task()

# The third option will allow the user to view all the tasks.
if options == "va":
    view_all()

# The fourth option will allow the user to only see their tasks.
if options == "vm":
    view_mine()

if options == "gr":
    if username == "admin":
        generate_reports()
    else:
        print("Only the Admin is allowed to generate reports.")

# The fifth option will exit from the program.
if options == "e":
    print("Exit")
