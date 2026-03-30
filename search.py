def search():
    # Import the list 
    from add_s import students
    
    looking = input("Which student are you looking for?: ").lower()
    
    # Create the “flag” (we start by assuming it does NOT exist)
    found = False 

    # Let's go through the entire list
    for student in students:
    # IMPORTANT: ‘product’ is a dictionary; we access the ‘name’ key
        if student['name'].lower() == looking:
            print(f"student found: {student}")
            found = True # we check it if we found it
            
    #At the end of the for loop do we check the flag
    if not found:
        print("\n***The student entered does not exist.***\n")