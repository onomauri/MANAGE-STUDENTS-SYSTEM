import csv
import os

def l_csv():
    # Local import to access the inventory list
    from add_s import students
    
    file_name = "record.csv"

    #Check if the file exists before trying to open it
    if not os.path.exists(file_name):
        print(f"\n***Error: The file '{file_name}' does not exist yet. Save some information first.***\n")
        return

    try:
        #Open the file in read mode ('r')
        with open(file_name, mode='r', newline='') as file:
            # DictReader uses the first row (header) as keys for the dictionaries
            reader = csv.DictReader(file)
            
            #Clear the current inventory to avoid duplicating items 
            #if the user loads the file multiple times
            students.clear()
            
            #Iterate through each row in the CSV
            for row in reader:
                #'row' is already a dictionary, so we just add it to our list
                students.append(row)
                
        print(f"Record successfully loaded from {file_name}!")
        print(f"Total records loaded: {len(students)}")
        
    except Exception as e:
        #Catch any unexpected errors during the reading process
        print(f"An error occurred while loading the file: {e}")