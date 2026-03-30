def d_student():
    #Local import to access the shared inventory list
    from add_s import students
    
    #Ask the user which product they want to remove
    looking = input("Which student do you want to delete?: ").lower()
    
    #Flag to track if we found the item
    found = False
    
    #create a temporary list to store items that match
    #This avoids errors while iterating over the main list
    student_to_remove = []

    #First loop: Find all matching products
    for student in students:
        if student['name'].lower() == looking:
            student_to_remove.append(student)
            found = True

    #Second loop: Remove the identified products from the original inventory
    for student in student_to_remove:
        students.remove(student)
        print(f"student '{student['name']}' has been deleted.")

    #If the flag is still False, the item wasn't in the list
    if not found:
        print("\n***The student entered does not exist, nothing was deleted.***\n")
