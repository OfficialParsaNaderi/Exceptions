list = []
try :
    user1 = (input("<<"))
    user2 = int(input(">>"))
    user3 = (input("<."))
    user4 = str(input(".>"))
    user5 = str(input("<.>"))
    user6 = (input("do you want remove !?"))
    list.append(user1)
    list.append(user2)
    list.append(user3)
    list.append(user4)
    list.append(user5)
    list.remove(user6)
    print(f"user personality : {list[0]}\nphone number : {list[1]}\nage : {list[1]}\nmarital status : {list[2]}\nheight :{list[3]}")
    user7 = len(list)
    print(user7)
except ValueError:
    print("you have entered a wrong value !")