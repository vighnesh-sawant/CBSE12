#Write a program in Python to create a binary file with name and roll number. Search for a given roll number and display the name, if not found display appropriate message.
import pickle

file=open("Text/student.dat",'ab')
student=[]
#taking input
while True:
    f=input("Do you want to add records? Enter y/n:")
    if f.lower() != "y" :
        break
    n=input("Enter name of student:")
    r=int(input("Enter rollno of student:"))
    student.append((n,r))

pickle.dump(student,file)
file.close()
#reading input
student=[]
fl=0
file=open("Text/student.dat","rb")
student=pickle.load(file)
while True:
    f=input("Do you want to search for records?Enter y/n:")
    if f.lower() != "y":
        break
    r=int(input("Enter roll no to search:"))
    for s in student:
        
        if s[1]==r:
            fl=1
            print(s[0])
    if fl!=1:
       print("No such student found")
file.close()