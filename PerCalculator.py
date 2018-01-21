from tkinter import *



def percentage():
    a = int(cal1.get())
    b = int(cal2.get())
    ans.config(text=a/b*100)



#Tk
root = Tk()
root.geometry('400x400')
root.title('MY GUI')

#call
cal1 = StringVar()
cal2 = StringVar()

#Heading
label = Label(root, text= 'Percentage Calculator', font=50, fg='White', bg='red')
label.pack(fill=X)

label = Label(root, text= '')
label.pack()
label = Label(root, text= '')
label.pack()
label = Label(root, text= '')
label.pack()


#Obtain Marks
label = Label(root, text= 'Enter Marks Obtained', bg='yellow')
label.pack()
entry1 = Entry(root, textvariable=cal1, justify='center')
entry1.pack()

label = Label(root, text= '')
label.pack()
label = Label(root, text= '')
label.pack()

#Total Marks
label = Label(root, text= 'Enter Total Marks', bg='yellow')
label.pack()
entry2 = Entry(root, textvariable=cal2, justify='center')
entry2.pack()

label = Label(root, text= '')
label.pack()


#Get %
button = Button(root, text='Get %', bg= 'green', fg='white', command=percentage)
button.pack()

label = Label(root, text= '')
label.pack()



#Answer
ans = Label(root, text='%', bg='orange', fg='white', font=30)
ans.pack()

label = Label(root, text= '')
label.pack()


#Exit
QUIT = Button(root, text='Exit', bg= 'white', fg='red', command=root.destroy)
QUIT.pack()



#Creator
creator = Label(root, text='Created by Arvind Vishwakarma', bg='grey',fg='white')
creator.pack(fill=X,side=BOTTOM)



root.mainloop()
