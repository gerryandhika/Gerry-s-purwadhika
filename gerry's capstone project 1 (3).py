#!/usr/bin/env python
# coding: utf-8

# In[ ]:


kids ={
    0:{
        'studentId': 1,
        'name':"andy",
        'age':6,
        'score':89,
        'siblings':1
    },
    1:{
        'studentId': 2,
        'name':"bety",
        'age':8,
        'score':88,
        'siblings':2
    },
    2:{
        'studentId': 3,
        'name':"charly",
        'age':7,
        'score':87,
        'siblings':3
    },
    3:{
        'studentId': 4,
        'name':"dicky",
        'age':9,
        'score':88,
        'siblings':1
    },
    4:{
        'studentId': 5,
        'name':"elaine",
        'age':8,
        'score':70,
        'siblings':8
    },
    5:{
        'studentId': 6,
        'name':"figha",
        'age':7,
        'score':80,
        'siblings':5
    }
}

def print_kids():
    print("Class of 2023")
    print('Index\t|StudentID\t|Name\t|Age\t|score\t|siblings')
    for item in kids:
        print(f"{item}\t|{kids[item]['studentId']}\t\t|{kids[item]['name']}\t|{kids[item]['age']}\t|{kids[item]['score']}\t|{kids[item]['siblings']}")

menu_item =0
while menu_item!=5:
    print('List Menu of Purwadhika-s Capstone Project')
    print('1. List and search student from class of 2023')
    print('2. Add new information')
    print('3. Update information')
    print('4. Delete information')
    print('5. Exit Program')
    menu_item = int(input("Insert Menu Selection: "))
    if menu_item>5:
        print("The number you entered is not valid, please insert the correct number!")
    elif menu_item==5:
        break

    elif menu_item==1:
        print_kids()
        option=0
        while option!=4:
            print('Find a student based on')
            print('1. Name')
            print('2. Age')
            print('3. Score[C(0-50),B(51-70),A(71-100)]')
            print('4. Siblings')
            print('5. Student Id')
            print('6. Back to main menu')
            option = int(input("Insert Menu Selection: "))
            if option==6:
                break
            elif option==1:
                summon_keyword = input("Insert kid's name to be searched: ")
                found = False
                for i in range(len(kids)):
                    if summon_keyword in kids[i]['name']:
                        print(kids[i])
                        print("The information has been found")
                        found = True
                        break

                    if not found:
                        print("The name you are searching for does not exist")
            elif option == 2:
                summon_age_keyword = int(input("Insert kid's age to be searched: "))
                found_students = []
                for i in range(len(kids)):
                    if summon_age_keyword == kids[i]['age']:
                        found_students.append(kids[i])

                if found_students:
                    print("Matching students with the age of", summon_age_keyword)
                    print('Index\t|StudentID\t|Name\t|Age\t|score\t|siblings')
                    for student in found_students:
                        print(f"{student['studentId']}\t|{student['name']}\t|{student['age']}\t|{student['score']}\t|{student['siblings']}")
                    print("The information has been found")
                else:
                    print("There are no students with that age")   
            elif option == 3:
                summon_score_keyword = input("Insert kid's score group [A/B/C] to be searched: ")
                found = False
                for i in range(len(kids)):
                    if kids[i]['score'] >= 0 and kids[i]['score'] <= 50 and summon_score_keyword == 'C':
                        print(kids[i])
                        found = True
                    elif kids[i]['score'] >= 51 and kids[i]['score'] <= 70 and summon_score_keyword == 'B':
                        print(kids[i])
                        found = True
                    elif kids[i]['score'] >= 71 and kids[i]['score'] <= 100 and summon_score_keyword == 'A':
                        print(kids[i])
                        found = True

                    if not found:
                        print("No kids found with the specified score range.")
                        
            elif option == 4:
                summon_siblings_keyword = int(input("Insert kid's siblings to be searched: "))
                found = False
                for i in range(len(kids)):
                    if summon_siblings_keyword == kids[i]['siblings']:
                        print(kids[i])
                        print("The information has been found")
                        found = True
                        break

                    if not found:
                        print("The siblings you are searching for does not exist") 

            elif option == 5:
                summon_stId_keyword = int(input("Insert StudentID to be searched: "))
                found = False
                for i in range(len(kids)):
                    if summon_stId_keyword == kids[i]['studentId']:
                        print(kids[i])
                        print("The information has been found")
                        found = True
                        break

                    if not found:
                        print("The studentID you are searching for does not exist") 
        
    elif menu_item==2:
        print_kids()
        option=0
        while option!=2:
            print('Add data')
            print('1. Entry a new data')
            print('2. Back to main menu')
            option = int(input("Insert Menu Selection: "))
            if option==2:
                break
            elif option==1:
                print_kids()
                temp_kids_stId = int(input("Insert Student ID: "))
                temp_kids_name = input("Insert Name: ")
                temp_kids_age = int(input(f"Insert {temp_kids_name}'s age: "))
                temp_kids_score = int(input(f"Insert {temp_kids_name}'s score: "))
                temp_kids_siblings = int(input(f"Insert {temp_kids_name}'s siblings: "))

                duplicate_id = False
                for kid in kids.values():
                    if kid['studentId'] == temp_kids_stId:
                        duplicate_id = True
                        break

                if duplicate_id:
                    print("Warning: The Student ID already exists.")
                else:
                # Check if the information already exists
                    exists = False
                    for kid in kids.values():
                        if (
                            kid ['studentId'] == temp_kids_stId
                            and kid['name'] == temp_kids_name
                            and kid['age'] == temp_kids_age
                            and kid['score'] == temp_kids_score
                            and kid['siblings'] == int(temp_kids_siblings)
                        ):
                            exists = True
                            break

                    if exists:
                        print("The information already exists and does not need to be added.")
                    else:
                        print("New information:")
                        print(f"Student Id: {temp_kids_stId}")
                        print(f"Name: {temp_kids_name}")
                        print(f"Age: {temp_kids_age}")
                        print(f"Score: {temp_kids_score}")
                        print(f"Siblings: {temp_kids_siblings}")

                        save_confirmation = input("Do you want to save this data? (yes/no): ")
                        if save_confirmation.lower() == "yes":
                            kids[len(kids)] = {
                                'studentId': temp_kids_stId,
                                'name': temp_kids_name,
                                'age': temp_kids_age,
                                'score': temp_kids_score,
                                'siblings': temp_kids_siblings
                            }
                            print("The information has been added successfully and saved.")
                        else:
                            print("The information has not been saved.")       
        
    elif menu_item == 3:
        print_kids()
        option = 0
        while option != 2:
            print('Update data')
            print('1. Update entry based on student Id')
            print('2. Back to main menu')
            option = int(input("Insert Menu Selection: "))
            if option == 2:
                break
            elif option == 1:
                summon_stid_keyword = int(input("Insert kid's student ID: "))
                found = False
                for i in range(len(kids)):
                    if summon_stid_keyword == kids[i]['studentId']:
                        found = True
                        print(kids[i])
                        print("The information has been found, continue to update")
                        while True:
                            print('Update data')
                            print('1. Update a specific column')
                            print('2. Save and exit')
                            update_option = int(input("Insert Menu Selection: "))
                            if update_option == 2:
                                break
                            elif update_option == 1:
                                print('Choose a column to update:')
                                print('1. Name')
                                print('2. Age')
                                print('3. Score')
                                print('4. Siblings')
                                column_option = int(input("Insert Menu Selection: "))
                                if column_option == 1:
                                    new_name = input("Enter new name: ")
                                    kids[i]['name'] = new_name
                                elif column_option == 2:
                                    new_age = int(input("Enter new age: "))
                                    kids[i]['age'] = new_age
                                elif column_option == 3:
                                    new_score = int(input("Enter new score: "))
                                    kids[i]['score'] = new_score
                                elif column_option == 4:
                                    new_siblings = int(input("Enter new number of siblings: "))
                                    kids[i]['siblings'] = new_siblings
                                else:
                                    print("Invalid column option")
                        confirmation = input("Do you want to update the data? (yes/no): ")
                        if confirmation.lower() == "yes":
                            print("Data successfully updated")
                            print_kids()
                        else:
                            print("Update canceled")
                            print_kids()
                        break

                if not found:
                    print("The student ID you are searching for does not exist")

        
        
        
    elif menu_item == 4:
        print_kids()
        option = 0
        while option != 2:
            print('Delete data')
            print('1. Delete entry based on student ID')
            print('2. Back to main menu')
            option = int(input("Insert Menu Selection: "))
            if option == 2:
                break
            elif option == 1:
                temp_delete_keyword = int(input("Insert student ID to be deleted: "))
                found = False
                for i in range(len(kids)):
                    if temp_delete_keyword == kids[i]['studentId']:
                        print(kids[i])
                        delete_option = input("Are you sure you want to delete this data? (yes/no): ")
                        if delete_option.lower() == 'yes':
                            del kids[i]
                            print("The information has been successfully deleted.")
                            found = True
                            print_kids()
                            break
                        else:
                            print("Deletion canceled. Returning to the main menu.")
                            found = True
                            break
                if found:
                    print("The student ID has been deleted.")
                else:
                    print("The student ID you are looking for does not exist.")
            else:
                print("Invalid option. Please choose a valid menu option.")


