list1 = []
while True:
    choice = int(input(
        '''
        Enter a choice you want to perform
        1 Push Elements
        2 Pop Elements
        3 Peek Element
        4 Display Stack
        5 Exit
        '''
    ))

    if(choice == 1):
        val = input("Enter a value :- ")
        list1.append(val)
    elif(choice == 2):
        if(len(list1) == 0):
            print("Empty List")
        else:
            list1.pop()
    elif(choice == 3):
        if(len(list1) == 0):
            print("Empty List")
        else:
            print("Stack last value :",list1[-1])
    elif(choice == 4):
        print("Stack Values :",list1)
    elif(choice == 5):
        break
    else:
        print("Invalid choice")