list1 = []
while True:
    choice = int(input(
        '''
        Enter a choice you want to perform :
        1 Enqueue Element(add element)
        2 Dequeue Element(delete first element)
        3 Front Element(display 1st element)
        4 Rear Element(display last element)
        5 Display Queue
        6 Exit
        '''
    ))

    if(choice == 1):
            val = input("Enter a value : ")
            list1.append(val)
    elif(choice == 2):
          if(len(list1) == 0):
                print("Empty List")
          else:
                del list1[0]
    elif(choice == 3):
          if(len(list1) == 0):
                print("Empty List")
          else:
                print("First Element of Queue :",list1[0])
    elif(choice == 4):
          if(len(list1) == 0):
                print("Empty List")
          else:
                print("Last Element of Queue :",list1[-1])
    elif(choice == 5):
          print("Queue Values :",list1)
    elif(choice == 6):
          break
    else:
          print("Invalid choice")