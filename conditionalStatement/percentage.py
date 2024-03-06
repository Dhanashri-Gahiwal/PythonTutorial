sub1 = int(input("Enter sub1 marks"))
sub2 = int(input("Enter sub2 marks"))
sub3 = int(input("Enter sub3 marks"))
sub4 = int(input("Enter sub4 marks"))

total = sub1 + sub2 + sub3 + sub4
print("total:",total)
percentage = total/4
print("percentage:",percentage)

if(percentage >= 70):
    print("Grade: Distinction")
elif(percentage >=60):
    print("Grade: First class")
elif(percentage >=50):
    print("Grade: Second class")
elif(percentage >=35):
    print("Grade: Pass class")
else:
    print("Grade: Fail")