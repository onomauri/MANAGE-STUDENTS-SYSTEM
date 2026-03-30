from menu import f_menu
from add_s import add_s
from show_s import student_list
from search import search
from update_s import u_students
from delete_s import d_student
from save_csv import s_csv
from load_csv import l_csv

exit= "" #variable will help us get out of the loop or still there 

while exit != "yes":
    try:
        f_menu()

        menu= int(input("Enter an option:") )

        if menu == 1:
            add_s()

        elif menu == 2:
            student_list()
            
        elif menu==3:
            search()

        elif menu==4:
            u_students()
        
        elif menu==5:
            d_student()

        elif menu == 6:
            s_csv()

        elif menu == 7:
            l_csv()    

        elif menu==8:
            exit="yes"
        else:
            print("The option entered does not exist.")    
    except:
        print("\n***Error: Invalid value entered try again.***\n")

print("Thanks for use the program, see you next time!")