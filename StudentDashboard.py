student={}
print("STUDENT MANAGER APP")
print(" 1.Add Student")
print(" 2.View Students")
print(" 3.Check Results")
print(" 4.Exit")
while True:
    choice = input("enter your choice:")
    #Add student 
    if choice =="1":
        name=input("enter student name:")
        marks=int(input("enter the marks:"))
        student[name]=marks
        print(f"{name} successfully Added!")
    elif choice=="2":
        if not student :
            print("no student found")
        else:
            for name,marks in student.items():
                print(name,":",marks)
    elif choice=="3":
        name=input("enter studnt name:")
        if name in student:
            marks =student[name]
            if marks>=40:
                print("pass")
            else:
                print("fail")
        else:
            print("sttudent not found")
    elif choice=="4":
        print("existing")
        break
    else:
        print("Invaild input")                                        
