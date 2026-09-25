#Student Performance Analyzer
#Main program
from student import add_student
from marks import calculate_performance
from scholarship import check_scholarship
def main():
    while True:
     print("\n===============================")
     print("   STUDENT PERFORMANCE ANALYZER   ")
     print("================================")
     print("1. Add Student and generate report")
     print(" 2. Exit")

     choice=input("Enter your choice:")

     if choice=="1":
      student=add_student()

      
     #Calculate performance
      performance=calculate_performance()
     #Check scholarship
      scholarship=check_scholarship(performance[2],performance[4])
     #Display final report
      print("\n================================")
      print("              FINAL STUDENT REPORT ")
      print("================================")

      print("Student Name:",student["name"])
      print("Roll Number:",student["roll_no"])
      print("Course:",student["course"])

      print("\nPerformance Details:")
      print("Total Marks:",performance[1],"/400")
      print("Percentage:",performance[2],"%")
      print("Grade:",performance[3])
      print("Status:",performance[4])
      print("Highest Scoring Subject:",performance[5])
      print("\nScholarship Eligibility:",scholarship[0])
      print("=================================")
    
     elif choice=="2":
      print("\n Thank you for using student performance analyzer")
      break
     else:
      print("\n Invalid choice. Please try again.")
      print("Please enter 1 or 2")
      #Start the program
main()     