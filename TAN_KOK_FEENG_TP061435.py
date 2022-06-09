#TAN KOK FEENG
#TP061435


#admin_part

#admin_add_record
def admin_add_record_coach(): #12 input 
    def coach_file_write():
        
        file.write(coach_id+","+coach_name+","+coach_date_joined+","+
                    coach_date_terminated+","+coach_hourly_rate+","+coach_phone+","+
                    coach_address+","+coach_sport_center_code+","+
                    coach_sport_center_name+","+coach_sport_code+","+coach_sport_name+
                    ","+"0"+","+"0")
    choice = "Y"
    while choice == "Y":
        print("Please provide information below: ")
        coach_id = input("Coach ID (Cxxx):")
        coach_name = input("Coach Name: ")
        coach_date_joined = input("Date joined(DD/MM/YYYY): ")
        coach_date_terminated = input("Date Terminated(DD/MM/YYYY): ")
        coach_hourly_rate = input("Hourly Rate($): ")
        coach_phone = input("Phone NO: ")
        coach_address = input("Email: ")
        coach_sport_center_code = input("Sport Center Code: ")
        coach_sport_center_name = input("Sport Center Name: ")
        coach_sport_code = input("Sport Code: ")
        coach_sport_name = input("Sport Name: ")
        count = 0
        file = open("coach_information.txt","r")
        for i in file:
            count += 1
        file.close()
        file = open("coach_information.txt","a")
        if count == 0:
            coach_file_write()
        else:
            
            file.write("\n")
            coach_file_write()
        file.close()
        choice = input("Continue? (Y/N): ")
    admin_add_record()

def admin_add_record_sport():
    def sport_write():
        file.write(sport_id +","+sport_name +","+sport_coach_name + "," +
                   sport_number_player)
    choice = "Y"
    while choice =="Y":
        print("Please provide information below: ")
        sport_id = input("Sport ID: ")
        sport_name = input("Sport Name: ")
        sport_coach_name = input("Coach Name: ")
        sport_number_player = input("Number of player: ")
        count = 0
        file = open("sport_information.txt")
        for i in file:
            count += 1
        file.close()
        file = open("sport_information.txt","a")
        if count == 0:
            sport_write()
        else:
            file.write("\n")
            sport_write()
        file.close()
        choice = input("Continue? (Y/N): ")
    admin_add_record()

def admin_add_record_sport_schedule():
    def sport_schedule_write():
        file.write(sport_date+","+sport_id +"," +sport_name +","+start_time+","
                   +end_time)
    choice = "Y"
    while choice == "Y":
        print("Please provide information below: ")
        sport_date = input ("\nDate(DD/MM/YYYY): ")
        sport_id = input ("Sport ID: ")
        sport_name = input("Sport Name: ")
        start_time = input ("Start time(AM/PM): ")
        end_time = input ("End Time (AM/PM): ")
        file = open("sport_schedule_information.txt")
        count = 0
        for i in file:
            count += 1
        file.close()
        file = open("sport_schedule_information.txt","a")
        if count == 0:
            sport_schedule_write()
        else:
            file.write("\n")
            sport_schedule_write()
        file.close()
        choice = input("Continue? (Y/N): ")
    admin_add_record()
        
    
def admin_add_record():
    print("\nWhich Record you want to add?\n")
    print("1. Coach")
    print("2. Sport")
    print("3. Sport Schedule")
    print("4. Back to main menu\n")
    choice = input("Enter Your Choice: ")
    if choice == "1":
        admin_add_record_coach()
    elif choice == "2":
        admin_add_record_sport()
    elif choice == "3":
        admin_add_record_sport_schedule()
    elif choice == "4":
        admin_main()
    else:
        print("Invalid input")
        print("Please Try again")
        print("======================")
        admin_add_record()

        
#admin_display_record
  
            
def display_record(a,b):
    choice = "N"
    while choice == "N":
        count = 1
        
        file = open(a,"r")
        for i in file:
            print(str(count)+")",i)
            count += 1
           
        choice = input("\nPress Enter to go back")
    if b == "admin":
        admin_display_record()
    if b == "guest":
        guest_view_detail()
        

def admin_display_record():
     
    print("\nWhich Record you want to display?\n")
    print("1. Coach")
    print("2. Sport")
    print("3. Registered Students")
    print("4. Student Feedbacks")
    print("5. Back to main menu\n")
    choice = input("Enter your choice: ")
    role = "admin"
    if choice == "1":
        file_name = "coach_information.txt"
        print("Coach Record show as below\n")
        
    elif choice == "2":
        file_name = "sport_information.txt"
        print("Sport Record show as below\n")
        
    elif choice == "3":
        file_name = "student_information.txt"
        print("Registered Record show as below\n")
    elif choice == "4":
        file_name = "student_feedback.txt"
        print("Student's Feedback show as below\n")

    elif choice == "5":
        admin_main()
    else:
        print("Invalid Input")
        print("Please try again")
        print("======================")
        admin_display_record()
    display_record(file_name,role)
        
        
#admin_search_specific_record
def specific_record(target,last_index,file_name,search_type): #12 #===========================================
    choice = "y"
    while choice == "y":
        check = False
        search = input(search_type).lower()
        print("")
        if file_name == "coach_information.txt" :
            specific_name = ["CoachID: ", "Coach Name: ", "DateJoined: ", "Date Terminated: ",
                             "Hourly Rate: ", "Phone NO: ","Email: ", "Sport Centre Code: ",
                             "Sport Centre Name: ", "Sport Code: ", "Sport Name: ","Rating: ",
                             "Time Rated: "]
        if file_name == "sport_information.txt" :
            specific_name = ["Sport ID: ", "Sport Name: ", "Coach Name: ", "Max Player: "]

        if file_name == "student_information.txt":
            specific_name = ["Student Name: ", "Student ID: ", "Student Email: ", "Student Password: "]
        file = open(file_name,"r")
        for index in file:
            var = index.split(",")
            var[last_index]=var[last_index].strip()
            if search == var[target].lower() :
                for i in range(0,len(var)):
                    print(specific_name[i % len(specific_name)],var[i])
                    check = True
                print("")
                
        if( check == False ):
            print("Not Found")
            choice = input("\nExit?(y): ")
            if choice != "y":
                specific_record(target,last_index,file_name,search_type)
            break
            
        choice = input("\nPress 'y' to search again: ")
    admin_search_specific_record()

        
def admin_search_specific_record():
    print("\nWhich function you wish to use?: ")
    print("1. Search Coach by Coach ID")
    print("2. Search Coach by overall performance(Rating)")
    print("3. Search Sport by Sport ID")
    print("4. Search Student by Student ID")
    print("5. Back to main menu")
    choice = input("Enter your choice: ")
    if choice == "1":
        target = 0
        last_index = 12
        file_name = "coach_information.txt"
        search_type = "Coach ID: "
    
    elif choice == "2":
        target =11
        last_index = 12
        search_type = "Coach Rating: "
        file_name = "coach_information.txt"
        
    elif choice == "3":
        target = 0
        last_index = 3
        search_type = "Sport ID: "
        file_name = "sport_information.txt"
        
    elif choice == "4":
        target = 1
        last_index = 3
        search_type = "Student ID: "
        file_name = "student_information.txt"
        
    elif choice == "5":
        admin_main()
    else:
        print("Invalid input")
        print("Please try again")
        print("====================")
        admin_search_specific_record()
    specific_record(target,last_index,file_name,search_type)

#admin_sort_display_record
def admin_sort_display_record():
    def sort(x):
        choice = "+"
        while choice == "+":
            a_array = [] #for the whole line
            b_array = [] #for the selected value

            file = open("coach_information.txt")
            for i in file:
                a_array.append(i.strip())
            file.close() #ihave to close here if not below array can't read

            file = open ("coach_information.txt")
            for i in file:
                var = i.split(",")
                b_array.append(var[int(x)])
            file.close()

            for i in range(0,len(b_array)):
                for j in range(i+1,len(b_array)): #i+1 is to make the second loop infront of first loop
                    if b_array[i] > b_array[j]:
                        b_array[i],b_array[j] = b_array[j],b_array[i]
                        a_array[i],a_array[j] = a_array[j],a_array[i]
            count = 0
            for i in range(0,len(a_array)):
                count += 1
                
                print("\n"+str(count)+") "+ a_array[i])
            
            choice = input("\nEnter any key to exit: ")
            admin_sort_display_record()

    
    print("How do you want to sort?\n")
    print("1. Sort by Coaches names")#1 in var[x]
    print("2. Sort by Coaches Hourly Pay Rate") #4 in var[x]
    print("3. Sort by Coachs Overall Performance")#11 in var[x]
    print("4. Back to main menu\n")
    choice = input("Enter your choice: ")
    if choice == "1":
        sort_type = "1"
        sort(sort_type)
    elif choice == "2":
        sort_type = "4"
        sort(sort_type)
    elif choice == "3":
        sort_type = "11"
        sort(sort_type)
    elif choice == "4":
        admin_main()
    else:
        print("Invalid input")
        print("Please try again")
        print("============================")
        admin_sort_display_record()
        

#admin_modify_record
def modify_coach(search_index,last_index,file_name,search_by,student_name,role):                            
    exist = False
    search_id = input("Please Enter Specific "+str(search_by)+": ")
    count = 0
    file = open(file_name)
    for i in file:
        var = i.split(",")
        var[last_index] = var[last_index].strip()
        if search_id == var[search_index]:
            exist = True
            break
        count += 1
    if file_name == "student_information.txt":
        if student_name != var[0]:
            print("Please Enter Your own Student ID")
            modify_coach(search_index,last_index,file_name,search_by,student_name,role)
    if exist == False :
        print (str(search_by)+" Not Found")
        try_again = input("\nTry again?(y/n): ")
        if try_again == "y":
            modify_coach(search_index,last_index,file_name,search_by,student_name,role)
        else:
            print("\nBack to previous page")
            admin_modify_record()
    file.close()
    if exist == True:
        arr = []
        file = open (file_name)
        for i in file:
            arr.append(i.strip())
        file.close()
        choice = "y"
        while choice =="y":
            if file_name == "coach_information.txt":
                print("\nWhich do you want to modify?")
                print("\n1.  Coach ID")
                print("2.  Coach Name")
                print("3.  Datejoined")
                print("4.  Date Terminated")
                print("5.  Hourly Rate")
                print("6.  Phone Number")
                print("7.  Email address")
                print("8.  Sport Centre Code")
                print("9.  Sport Centre Name")
                print("10. Sport Code")
                print("11. Sport Name")
                print("12. Back to previous page")
                choice_type = input("\nEnter your choice: ")
                try:
                    choice_type = int(choice_type)
                except:
                    print ("Invalid input")
                    continue
                specific_array = ["Coach ID","Coach Name","Date joined", "Date Terminated",
                               "Hourly Rate","Phone Number","Email address","Sport Centre Code",
                               "Sport Centre Name","Sport Code","Sport Name"]
                if int(choice_type) > 0 and int(choice_type) <= 12:
                    if int (choice_type) == 12 :
                        admin_modify_record()
        
                else:
                    print ("Invalid input")
                    continue
            if file_name == "sport_information.txt":
                print("\nWhich do you want to modify?")
                print("\n1. Sport ID")
                print("2. Sport Name")
                print("3. Sport Coach")
                print("4. Maximum Player")
                print("5. Back to previous page")
                choice_type = input("\nEnter your choice: ")
                try:
                    choice_type = int(choice_type)
                except:
                    print ("Invalid input")
                    continue
                specific_array = ["Sport ID","Sport Name","Sport Coach","Maximum Player"]
                if int(choice_type) > 0 and int(choice_type) <= 5:
                    if int (choice_type) == 5 :
                        admin_modify_record()
        
                else:
                    print ("Invalid input")
                    continue
            if file_name == "sport_schedule_information.txt":
                print("\nWhich do you want to modify?")
                print("\n1.Sport Date")
                print("2. Sport ID")
                print("3. Sport Name")
                print("4. Start Time")
                print("5. End Time")
                print("6. Back to previous page")
                choice_type = input("\nEnter your choice: ")
                try:
                    choice_type = int(choice_type)
                except:
                    print ("Invalid input")
                    continue
                specific_array = ["Sport Date","Sport ID","Sport Name","Start Time","End Time"]
                if int(choice_type) > 0 and int(choice_type) <= 6:
                    if int (choice_type) == 6 :
                        admin_modify_record()
    
                else:
                    print ("Invalid input")
                    continue
                
            if file_name == "student_information.txt":
                print("\n Which do you want to modify?")
                print("\n1. Student Name")
                print("2. Student ID")
                print("3. Student Email")
                print("4. Student Password")
                print("5. Back to previous page")
                choice_type = input("\nEnter your choice: ")
                try:
                    choice_type = int(choice_type)
                except:
                    print ("Invalid input")
                    continue
                specific_array = ["Student Name","Student ID","Student Email",
                                  "Student Password"]
                if int(choice_type) > 0 and int(choice_type) <= 5:
                    if int (choice_type) == 5 :
                        student_main(student_name)
                else:
                    print ("Invalid input")
                    continue
                    
                
            target_modify = input("New "+specific_array[int(choice_type)-1]+": ")
        
            var[int(choice_type)-1] = target_modify
            if file_name == "student_information.txt":
                student_name = var[0] #to change the current student name to new student name
            temp = ",".join(var) #add to arr with "," this is basically temp = var[0] +.......var[last_index]
            arr[count] = temp
            choice = input("Continue?(y/n): ")
        file=open(file_name,"w") 
        file.write("") #to clean the txt file
        file.close()


        count_file = 0
        for i in range(0,len(arr)):
            file = open(file_name)
            for counting in file:
                count_file += 1
            file.close()
            file = open(file_name,"a")
            if count_file == 0:
                file.write(arr[i])
            else:
                file.write("\n")
                file.write(arr[i])
            file.close()
        print("Modify succesful!!!")
        if role == "admin":
            admin_modify_record()
        elif role == "student":
            student_main(student_name)
        
            
def admin_modify_record():
        
    print ("\nWhich do you want to modify")
    print ("\n1. Coach")
    print ("2. Sport")
    print ("3. Sport Schedule")
    print ("4. Back to main menu\n")
    student_name = ""
    role = "admin"
    choice = input("Enter your choice: ")
    if choice == "1":
        search_index = 0
        last_index = 12
        search_by = "Coach ID"
        file_name = "coach_information.txt"
    elif choice == "3":
        search_index = 1
        last_index = 4
        search_by = "Sport ID"
        file_name = "sport_schedule_information.txt"
        
    elif choice == "2":
        search_index = 0
        last_index = 3
        search_by = "Sport ID"
        file_name = "sport_information.txt"
    elif choice == "4":
        admin_main()
    else:
        print("Invalid input")
        print("Please try again")
        admin_modify_record()
    modify_coach(search_index,last_index,file_name,search_by,student_name,role)
        
    
    
#admin_mainmenu
def admin_main():
    print("\nWelcome Admin")
    print("=================\n")
    print("What do you want to do?\n")
    print("1. Add Records ")
    print("2. Display All Records ")
    print("3. Search Specific Records ")
    print("4. Sort and display Records of coaches" )
    print("5. Modifiy Records")
    print("6. Logout\n")
    choice = input("Enter Your Choice: ")
    if choice == "1":
        admin_add_record()
    elif choice == "2":
        admin_display_record()
    elif choice == "3":
        admin_search_specific_record()
    elif choice == "4":
        admin_sort_display_record()
    elif choice == "5":
        admin_modify_record()
    elif choice == "6":
        main()
    else:
        print("Invalid input")
        print("Please try again")
        print("==========================")
        admin_main()
      

def admin_login():
    print("Please Enter Admin username and password")
    username=input("Username: ")
    password = input("Password: ")
    if username == "admin" and password == "admin123":
        print("Login Succesful")
        admin_main()
    else:
        print("Invalid username or password")
        print("Please try again")
        choice = input("Retry?(Y/N): ")
        while choice != "N":
            print("-------------------------")
            admin_login()
        main()

#student_part
        
#registered_student

def student_feedbackstar_to_coach(student_name): #max13
    count = 0
    coach_id=input("Who do you want to feedback & rate (CoachID): ")
    file = open ("coach_information.txt")
    for i in file:
        
        var = i.split(",")
        if coach_id == var[0]:
            break
        count += 1
        
    if coach_id != var[0]:
        print("Coach Not Found")
        continue_choice = input("Try again?(Y/N): ")
        if continue_choice != "Y":
            student_main(student_name)
        else:
            student_feedbackstar_to_coach(student_name)
    file.close()
    #feedbackpart
    feedback = input("Feedback to " + str(var[1]) +":")
    file = open("student_feedback.txt")
    count_feedback = 0
    
    for i in file:
        count_feedback += 1
        
    file.close()
    file=open("student_feedback.txt","a")
    
    if count_feedback == 0:
        file.write(feedback+", from "+student_name+" to " +str(var[1]))
    else:
        file.write("\n"+feedback+", from "+student_name+" to "+ str(var[1]))
    file.close()

    #rating part
    a_array = []
    file = open("coach_information.txt")
    for i in file:
        a_array.append(i.strip())
    file.close()
    choice = "y"
    while choice == "y":
        rate = input("Rate(0 to 5): ")
        try:
            rate = int(rate)
            
        except:
            print("Invalid input")
            continue
        if rate >= 0 and rate <= 5:

            var[11] = float(var[11]) * int(var[12])
            var[11] =  float(var[11]) + float(rate)
            var[12] = str(int(var[12]) + 1)
            var[11] = str(round(float(float(var[11])/float(var[12])),1))
            temp = ','.join(var)
            a_array[count]= temp
            file = open ("coach_information.txt","w")
            file.write("")
            file.close()

            count_file = 0
            for i in range(0,len(a_array)):
                file = open("coach_information.txt","r")
                for count in file:
                    count_file += 1
                file.close()
                file = open("coach_information.txt","a")
                if count_file ==0 :
                    file.write(a_array[i])
                else:
                    file.write("\n")
                    file.write(a_array[i])
                file.close()
        else:
            print("Out of range")
            continue
        choice = input("Press Enter to Continue")
    student_main(student_name)    
    
    
def student_view_detail(student_name):
    def student_display_self_record(student_name):
        choice = "y"
        while choice == "y":
            file = open("student_information.txt","r")
            for i in file:
                var = i.split(",")
                var[3] = var[3].strip()
                if student_name == var[0]:
                    for i in range (len(var)):
                        print(var[i])
                    break
            file.close()
            choice = input("Press Enter to back to previous page:")
        student_view_detail(student_name)
                
        
    def student_display_record(a,student_name):
        choice = "N"
        while choice == "N":
            count = 1
            
            file = open(a,"r")
            for i in file:
                print(str(count)+")",i)
                count += 1
            choice = input("\nPress Enter to go back")
        student_view_detail(student_name)
    print("Which you category you wish to view")
    print("1. Coach")
    print("2. Self-Record")
    print("3. Registered Sport Schedule")
    print("4. Back to previous page\n")
    choice = input("Enter your choice: ")
    if choice == "1":
        #same as the admin display coach coding
        file_name = "coach_information.txt"
        student_display_record(file_name,student_name)
    elif choice == "2":
        student_display_self_record(student_name)
    elif choice == "3":
        file_name = "sport_schedule_information.txt"
        student_display_record(file_name,student_name)
    elif choice == "4" :
        student_main(student_name)
    else:
        print("Invalid Input")
        print("===================")
        student_view_detail(student_name)
    
 #search_index,last_index,file_name,search_by,student_name   
#registered_student_mainmenu
def student_main(student_name):
    print("\nWelcome",student_name,"\n")
    print("1. View Detail of")
    print("2. Modify self Record")
    print("3. Provide feedback and Star to Coach.")
    print("4. Logout\n")
    choice = input("Enter your choice: ")
    if choice == "1":
        student_view_detail(student_name)
    if choice == "2":
        search_index = 1
        last_index = 3
        file_name = "student_information.txt"
        search_by = "your Student ID"
        role = "student"
        #same coding as admin modify
        modify_coach(search_index,last_index,file_name,search_by,student_name,role)
    
    elif choice == "3":
        student_feedbackstar_to_coach(student_name)
    elif choice == "4":
        student_category()
    else:
        print("Invalid input")
        print("Please Try again")
        print("=========================")
        student_main(student_name)
        
#all_student        
def student_login():
    choice = "y"
    while choice == "y":
        print("Please Enter your Student ID and password")
        student_id = input("Student ID: ")
        student_password = input("Password: ")
        if len(student_id.strip()) == 0 or len(student_password.strip()) ==0 : # to avoid spacing input
            print("Invalid input")
            print("Please Try again")
            continue
            
            
        else:
            file = open ("student_information.txt","r")
            for i in file:
                var = i.split(",")
                var[3]=var[3].strip()
                if (student_id == var[1]) and (student_password == var[3]):
                    print("Login succesful")
                    print("==================")
                    student_main(var[0])
                    break
                    
                    
                
                
            if (student_id != var[1]) or (student_password != var[3]):
                print("Wrong Student ID or Password")
                print("Please Try again")
                print("------------------------------")
                choice = input("Continue?(y): ") 
                if choice != "y":
                     student_category()
               
           
                
            file.close()
   
            
    


def student_register():
    print("Please enter below information to register")
    student_name = input("Name: ")
    student_id = input("Student ID: ")
    student_email = input("Email Address: ")
    student_password = input("Password: ")
    count = 0
    file = open("student_information.txt","r")
    for i in file:
        count += 1
    
    if len(student_id.strip()) == 0 or len(student_password.strip()) ==0 : # to avoid spacing input
        print("invalid input for studentID or Password")
        print("Please Try again")
        print("-------------------")       
        student_register()
    elif count == 0 :
        file = open ("student_information.txt","a")
        file.write(student_name+","+student_id+","+student_email+","+student_password)
        file.close()
        print("Registered Succesful")
        file.close()
            
    else:
        file = open("student_information.txt","r")
        for i in file: #to make sure the new registered is not existed
            var= i.split(",")
            var[3]=var[3].strip()
            var[1] = var[1].lower()
            if (student_id.lower() == var[1]):
                print("This studentID is already registered")
                user_exist = True
                break
            else:
                user_exist = False
                
        if user_exist == False: 
            file = open ("student_information.txt","a")
            file.write("\n"+student_name+","+student_id+","+student_email+","+student_password)
            file.close()
            print("Registered Succesful")
            file.close()
            
        file.close()
    print("----------------")
    student_category()


    

def guest_view_detail():
    print("\nWhat you want to do?\n")
    print("1. Sport")
    print("2. Sport Schedule")
    print("3. Exit")
    choice = input("Enter your choice: ")
    role = "guest"
    if choice == "1":
        #same coding as admin display record sport
        file_name = "sport_information.txt"
        
    elif choice == "2":
        file_name = "sport_schedule_information.txt"
    elif choice == "3":
        student_category()
    else:
        print("Invalid input")
        print("Please Try Again")
        print("===================")
        guest_view_detail()
    display_record(file_name,role)
        
        
        


#all_student_mainmenu   
def student_category():
    
    print("\nWhat you want to do?\n")
    print("1. Login")
    print("2. Register")
    print("3. View details as Guest")
    print("4. Exit\n")
    choice1 = input("Enter your choice: ")
    if choice1 == "2":
        student_register()
    elif choice1 == "1":
        student_login()
    elif choice1 =="3":
        guest_view_detail()
    elif choice1 == "4":
        main()
    else:
        print("Invalid input")
        student_category()
    
#main_part
def main():
    print ("Welcome to Sport Academy System")
    print ("====================================\n")
    print ("Who are you?")
    print ("1. Admin")
    print ("2. Student")
    print ("3. Exit\n")


    choice = input("Enter your choice: ")
    if choice == "2":
        student_category()
    elif choice == "1":
        admin_login()
    elif choice == "3":
        exit()
    else:
        print("***********************************")
        print("Invalid input\n")
        main()

main()
