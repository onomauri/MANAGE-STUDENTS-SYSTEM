
students=[]

def add_s():
    finish= ""
    while finish != "yes":
        try:
            id_s=int(input("Enter an ID for the student: "))  
            name=input("Enter the student name: ")
            age=int(input("Enter the age of the studen: ")) #change from str to int a ege can only be a number 
            while age <=5 or age>=22:                       #stablish a range for the students
                print("Student out of the range enter a valid value.")    
                age=int(input("Enter the age of the studen: ")) 
            program=input("Enter the student's program:  ")
            stage=input("Enter the stage of the student (Active/Inactive): ").lower() #.lower() to try handle the same format for the information 
            if stage == "a" or stage == "act":
                stage = "active"                          #aditional asistance to help autocomplete in some situations 
            if stage == "i" or stage == "in":
                stage= "inactive" 
            finish=input("would you like to finish (Yes/anyother key to continue.): ")     

            s_log={
                "id": id_s,
                "name": name,
                "age": age,
                "program":program,
                "stage": stage
            }
            students.append(s_log)
            print("Student added succesfully")
        except:
            print("Error: Invalid value was entered, try again.")  


