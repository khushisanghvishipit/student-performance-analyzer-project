#Marks and performance Calculation Module
def calculate_performance():
    print("\n-----Enter Student Marks-----")
    subjects=["Python","Mathematics","Enviromental studies","communication"]
    marks={}
    for subject in subjects:
        while True:
            mark=float(input(f"Enter marks for{subject}(0-100):"))
            if 0<=mark<=100:
                    marks[subject]=mark
                    break
            else:
                    print("Please enter a valid number.")
            

#Calculate total and percentage
    total=sum(marks.values()) 
    percentage=total/len(subjects) 

#Calculate grade
    if percentage>=90:
     grade="A+"
    elif percentage>=80:
     grade="A" 
    elif percentage>=70:
     grade="B" 
    elif percentage>=60:
     grade="C"
    elif percentage>=50:
     grade="D" 
    else:
     grade="F" 
#Pass/Fail
    if percentage>=40:
     status="PASS"
    else:
     status="FAIL" 
#Find higest-scoring subject
    higest_subject=max(marks,key=marks.get) 

    print("\n-----Performance Report-----")
    print("Total Marks:",total,"/400")
    print("Percentage:",percentage,"%")
    print("Grade:",grade)
    print("Status:",status)
    print("Higest Scoring Subject:",higest_subject) 
    print("Marks:",marks[higest_subject])

    return marks, total, percentage, grade, status, higest_subject



 

