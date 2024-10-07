myList = []

def printList():
  print()
  for i in myList:
    print(i)
  print()

while True:
    firstName =input("What is your First Name? ").strip().capitalize()
    secondName =input("What is your Second Name? ").strip().capitalize()
    print()
    fullName = f"{firstName} {secondName}"
    if fullName in myList:
        print("ERROR: Duplicate name")
    else:
        myList.append(fullName)
    printList()

    