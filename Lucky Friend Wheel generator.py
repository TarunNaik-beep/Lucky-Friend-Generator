 from tkinter import *
import random

root = Tk()
root.title("Lucky Friend Wheel")
root.geometry("500x500")

list_name_of_freinds = []
enter_name = Entry(root)
enter_name.place(relx=0.5, rely=0.2, anchor=CENTER)

friends_list = Label(root)
random_num = Label(root)
lucky_friend = Label(root)

def addFriend():
    name = enter_name.get()
    list_name_of_freinds.append(name)
    friends_list["text"] = "Your Friend List is " + str(list_name_of_freinds)
    
def randomNumber():
    length = len(list_name_of_freinds)
    random_no = random.randint(0, length-1)
    random_num["text"] = str(random_no)
    random_friend = list_name_of_freinds[random_no]
    lucky_friend["text"] = "Your Lucky Friend is " + str(random_friend)
    

btn = Button(root, text="Add to Your freind list", command=addFriend)
btn.place(relx=0.5, rely=0.3, anchor=CENTER)

friends_list.place(relx=0.5, rely=0.4, anchor=CENTER)

btn2 = Button(root, text="Who is Your Lucky Friend", command=randomNumber)
btn2.place(relx=0.5, rely=0.5, anchor=CENTER)

random_num.place(relx=0.5, rely=0.6, anchor=CENTER)
lucky_friend.place(relx=0.5, rely=0.7, anchor=CENTER)



root.mainloop()
