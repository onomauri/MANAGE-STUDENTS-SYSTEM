def u_students():
    # Local import to access the shared inventory list
    from add_s import students  
    
    # Ask the user which product to search for
    looking = input("Enter student name: ").lower()
    
    # Flag to track if we found at least one match
    found = False

    # Iterate through every dictionary in the list
    for student in students:
        # Check if the 'name' key matches the user's input
        if student['name'].lower() == looking:
            found = True
            print(f"Current details: {student}")
            
            # Request new data from the user
            new_id = input("New ID (Press Enter to skip): ")
            new_name = input("New name (Press Enter to skip): ")
            new_age = input("New age (Press Enter to skip): ")
            new_program = input("New program (Press Enter to skip): ")
            new_stage = input("New stage (Press Enter to skip): ")

            # Update the dictionary keys only if input is not empty
            if new_id:
                student['id'] = new_id
            if new_name:
                student['name'] = new_name
            if new_age:
                student['age'] = new_age
            if new_program:
                student['program'] = new_program
            if new_stage:
                student['stage'] = new_stage

            
            print("Student successfully updated!")
            print(f"New details: {student}")

    # If the loop finishes and 'found' is still False, show the error
    if not found:
        print("\n***The student entered does not exist, update failed.***\n")


