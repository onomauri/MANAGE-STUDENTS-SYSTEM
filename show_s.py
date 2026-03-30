def student_list():
    from add_s import students
    if not students:
        print("\n***No student in the record yet.***\n") 
    else:
        for s in students:
            print(f"ID:{s['id']}|Name of the student: {s['name']}| age:{s['age']}| program: {s['program']}|Stage: {s['stage']}")
