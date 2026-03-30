import csv

def s_csv():
    # Local import to get the current state of the inventory list
    from add_s import students
    
    # Define the name of the file where the data will be stored
    file_name = "record.csv"

    # Check if the inventory is empty before trying to save
    if not students:
        print("\n***The record is empty. There is nothing to save.\n***")
    else:
        # Get the headers (column names) from the keys of the first dictionary
        # Example: ['name', 'price', 'quantity']
        headers = students[0].keys()

        try:
            # Open the file in write mode ('w'). 
            # 'newline=""' prevents extra blank lines on some operating systems.
            with open(file_name, mode='w', newline='') as file:
                # Create a DictWriter object using the headers found
                writer = csv.DictWriter(file, fieldnames=headers)
                
                # Write the first row with the column names
                writer.writeheader()
                
                # Write all dictionaries from the list as rows in the CSV
                writer.writerows(students)
                
            print(f"Current information successfully saved to {file_name}!")
            
        except Exception as e:
            # Catch any unexpected errors during the file writing process
            print(f"An error occurred while saving: {e}")