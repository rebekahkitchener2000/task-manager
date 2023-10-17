from datetime import date #to print current date
from datetime import datetime

print("Good Morning!")
print("Please log in below: ")
with open ("user.txt", "r") as file: #open file to view
    username = [] #empty list for username
    password = [] #empty list for password
    for lines in file:
        temp = lines.strip('\n') #strip \n from each line
        temp = temp.split(', ') #split each line by comma
        username.append(temp[0]) #append username to username list
        password.append(temp[1]) #append password to password list
dictionary = dict(zip(username, password)) #dictionary combines lists at index
#found using https://realpython.com/python-zip-function/

counter = 0 #counter will be used for number of logon attempts
while True:
    user_username = input("Please enter your username: ") #ask user to input username
    user_password = input("Please enter your password: ") #ask user to input password
    if user_username in dictionary.keys() and user_password == dictionary[user_username]: 
    #check username and password match
            print(f"Welcome {user_username}!") #output Welcome to user
            break
    elif user_username != dictionary.keys() or user_password != dictionary[user_username]: 
        #wrong input if username or password are wrong
        print('''Sorry your input is not valid. 
        Please try again!''') #ask user to try again
        counter += 1 #add to counter every log on failure
        if counter == 3: #output 3 logon attempts failed
            print("Your login has failed on three attempts.")
            break
        continue

if counter == 3: 
    print('''You are now locked out. 
        Please contact admin support.''') #output locked out
elif counter < 3: #user continues to menu if logon is correct
    while True:
    # Present the menu to the user
    # make sure that the user input is converted to lower case.
        if user_username == "admin": #user "admin" can also display statistics in menu
            menu = input('''Please select one of the following options by typing the corresponding letter:
        r - register a user
        a - add task
        va - view all tasks
        vm - view my tasks
        s - display statistics
        e - exit
        : ''').lower() #ask user to input from selected menu
        else:
            menu = input('''Please select one of the following options by typing the corresponding letter:
        r - register a user
        a - add task
        va - view all tasks
        vm - view my tasks
        e - exit
        : ''').lower() #ask user to input from selected menu

        if menu == 'r' and user_username != "admin":
            print("You do not have access to register new users.") 
            #output to user that they cannot register users.
        elif menu == "r" and user_username == "admin":#continue if user is admin
            pass
            while True:
                new_username = input("Please enter a new username: ") #user enter name
                if new_username in dictionary.keys(): #check if username already exists
                    print("Username already exists. Please try again.")
                    continue
                else:
                    break
            while True:
                new_password = input("Please enter a new password: ") #admin to enter password
                confirm_password = input("Please confirm your new password: ")
                if confirm_password == new_password: #check if passwords match, break from loop
                    break
                else:
                    print("Both passwords do not match. Please try again!") #ask user to try again
                    continue
            with open ("user.txt", "a") as file: #open user.txt file
                file.write(f"\n{new_username}, {new_password}") #write username, password to file
                   
        elif menu == 'a': #user chooses add task
            pass
            while True:
                task_username = input("Please enter the username you would like to assign task to: ") 
                #ask for username
                if task_username in dictionary.keys(): #check username is in dictionary
                    break
                else:
                    print("Username does not exist. Please try again.") #output to user to try again
                    continue    
            today = date.today()#gets current date
            task_title = input("Please enter title of task: ") #input task title
            task_description = input("Please enter task description: ") #input task description
            task_date = input("Please enter due date for task: ") #input task due date
            current_date = (today.strftime("%d %b %Y")) #imports current date
            task_complete = "No" #set task to incomplete

            with open ("tasks.txt", "a") as f:
                f.write(f'''
{task_username}, {task_title}, {task_description}, {task_date}, {current_date}, {task_complete}''')
                #write new task to file

        elif menu == 'va': #user wants to view all tasks
            pass
            with open('tasks.txt', 'r') as f: #open tasks.txt file
                task_num = 0
                for line in f: 
                    new_line = line.strip().split(", ") #split every line by comma and space
                    task_num += 1
                    print(f''' 
                    Task Number: \t {task_num}
                    Task:\t \t {new_line[1]}
                    Assigned to: \t {new_line[0]} 
                    Date assigned:\t {new_line[4]}
                    Due Date: \t \t {new_line[3]}
                    Task Complete? \t {new_line[5]}
                    Task description:
                        {new_line[2]}''') #output task details

        elif menu == 'vm':
            pass
            with open('tasks.txt', 'r') as f: #open tasks.txt file
                task_num = 0
                for lines in f:
                    new_lines = lines.strip().split(', ') #split every line
                    task_num += 1 #add 1 to task_num for each line
                    if new_lines[0] == user_username:    
                    #if username matches a name in task, output tasks.
                        print(f'''
                    Task Number: \t {task_num}
                    Task:\t \t {new_lines[1]}
                    Assigned to: \t {new_lines[0]}
                    Date assigned:\t {new_lines[4]}
                    Due Date: \t \t {new_lines[3]}
                    Task Complete? \t {new_lines[5]}
                    Task description:
                        {new_lines[2]}''')
                
                edit_or_menu = input(''' 
                Please enter:
                'M'- to return to menu
                'E' to edit task                  
                ''').lower() #ask user to select edit or menu                 
                while True:
                        if edit_or_menu == 'e':
                            while True:
                                    try:
                                        task_number = int(input('''
                                        Please enter the task number you would like to edit: 
                                        e.g. enter '1' for task number 1.''')) #user enters task number
                                        break
                                    except ValueError: #invalid if input is not integer
                                        print("Your input is invalid. Please try again!")

                            task_num = 0
                            with open('tasks.txt', 'r') as f: #open tasks.txt file
                                for lines in f:
                                    lines = lines.strip().split(', ') #split every line by comma and space
                                    task_num += 1
                                    if task_number > 0: #valid task number
                                        break
                                    elif task_number <= 0 or task_number != task_num: #invalid task number
                                        print("Your input is invalid please try again!")
                                        continue

                            task_number -= 1 #subtract 1 from task_number so it matches index of line
                            with open('tasks.txt', 'r') as file: #open file in read mode
                                taskFile = file.readlines() #read each line
                                print(taskFile[task_number] + "\n") #print task to user
                                task_line = taskFile[task_number].strip().split(", ") #split task number line
                      
                                task_complete = input('''
                                Is this task complete?
                                    Please enter:
                                    Y - Yes
                                    N - No ''') #user seects whether task is complete
                                if task_complete == 'y' and task_line[5] == 'No': #changes task to complete
                                    with open('tasks.txt', 'r') as file:
                                        file_content = file.readlines()
                                        split_line = file_content[task_number].strip().split(", ")
                                        split_line[5] = "Yes" #change index 5 to Yes
                                        file_content[task_number] = ', '.join(split_line) + "\n" #join line
                                        file_content = " ".join(file_content)
                                        with open('tasks.txt', 'w') as f:
                                            f.write(file_content) #re-write to file
                                        task_number += 1
                                        print(f"Task number {task_number} is now marked as complete.")
                                elif task_complete == 'y' and task_line[5] == 'Yes': 
                                    #check if task is already complete
                                    print("This task is already marked as complete.")
                                elif task_complete == 'n' and task_line[5] == 'No':
                                    print("This task is already marked as incomplete.") #output task is incomplete
                                elif task_complete == 'n' and task_line[5] == 'Yes': #change to incomplete
                                    with open('tasks.txt', 'r') as file: #open file
                                        file_content = file.readlines()
                                        split_line = file_content[task_number].strip().split(", ")
                                        split_line[5] = "No" #change index 5 to 'No'
                                        file_content[task_number] = ', '.join(split_line) + "\n" #split task
                                        file_content = " ".join(file_content) #join line together
                                        with open('tasks.txt', 'w') as f:
                                            f.write(file_content) #re-write to file
                                        task_number += 1
                                        print(f"Task number {task_number} is now marked as incomplete.")
                                    
                                while True:
                                    edit_task = input('''
                                        Would you like to edit another task?
                                        Please enter:
                                        Y - Yes
                                        N - No''').lower() #user chooses to edit another task
                                    if edit_task == 'y':
                                        break 
                                    elif edit_task == 'n':
                                        break 
                                    else:
                                        print("You have entered an invalid input please try again")
                                        continue #checks for invalid input
                                if edit_task == 'y': #goes to edit another task
                                    continue
                                elif edit_task == 'n':
                                    break #goes back to menu
                        elif edit_or_menu == 'm':
                            break    

        elif menu == 's': #admin user chooses to display statistics
            pass
            number_tasks = 0 #set number of tasks to 0
            with open('tasks.txt', 'r') as f:
                for line in f:
                    number_tasks += 1 #go through every line and add to number of tasks
                print(f"The total number of tasks are: {number_tasks}") #output total number of tasks
            
            number_users = 0 #set number of users to 0
            with open('user.txt', 'r') as f:
                for line in f:
                    number_users += 1 #loop through file and add number of users
                print(f"The total number of users are: {number_users}") 
                #output total number of users
            
            with open('tasks.txt', 'r') as f: #open file as f
                for line in f:
                    line = line.strip().split(', ')
                    task_complete = 0
                    if line[5] == 'Yes': #count number of tasks complete
                        task_complete += 1
            percentage_tasks_complete = (task_complete / number_tasks) * 100 
            #calculate percentage of tasks complete
            print(f"The percentage of tasks complete is: {percentage_tasks_complete} %")


            with open('tasks.txt', 'r') as f: #open file as f
                counter = 0 #assign 0 to counter
                for line in f:
                    line = line.strip().split(', ')
                    string_input_with_date = line[4] #line 4 is due date
                    past = datetime.strptime(string_input_with_date, "%d %b %Y")
                    #convert due date into dd mm yyyy
                    present = datetime.now() 
                    if past.date() < present.date():
                        counter += 1 #if due date is less than current date add 1 to counter   
                print(f"Number of tasks overdue: {counter}") #output total tasks overdue

            with open('tasks.txt', 'r') as f: #open file as f
                for line in f:
                    line = line.strip().split(', ')
                    task_complete = 0
                    if line[5] == 'No': #count number of tasks complete
                        task_complete += 1
            percentage_tasks_complete = (task_complete / number_tasks) * 100 
            #calculate percentage of tasks incomplete
            print(f"The percentage of tasks incomplete is: {percentage_tasks_complete} %")

        elif menu == 'e': #user chooses to exit
            print('Goodbye!!!')
            exit()

        else:
            print("You have entered an invalid input. Please try again") 
            #user enters invalid input so is asked to try again





































































































