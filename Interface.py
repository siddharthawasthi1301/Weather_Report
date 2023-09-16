from tkinter import *
import requests
import json

window = Tk()
window.title('WELCOME MY FRIEND')

l1 = Label(window,text= 'WEATHER APPLICATION',bg="sky blue",fg="black",width=30,height=2,font=('arial black',12))
l1.place(x=135 ,y=300)
l2 = Label(window,text= 'Enter City',bg='Lavender',fg="Black",width=10,font=('Calibri',18))
l2.place(x=5,y=371)
img = PhotoImage(file="C:/Users/Asus/OneDrive/Desktop/unnamed.png")
l3 = Label(window,image=img)
l3.pack()
l4 = Label()
l4.place(x=200,y=450)
l5=Label()
l5.place(x=250,y=500)
v = StringVar()

def action():
    city =v.get()
    url1= 'http://api.weatherapi.com/v1/current.json?key=ed0deb94339846afb2694943230809&q='+city

    df = requests.get(url1)
    data = json.loads(df.content)
    l4.config(text="Temperature in Celsius :- " + str(data['current']['temp_c']),bg='Green',fg='White')
    l5.config(text="Temperature in Feherenite :- " + str(data['current']['temp_f']),bg='green',fg='white')




e1 = Entry(window, width=20,bg='lavender',font=('calibri',20),textvariable=v)
e1.place(x=150,y=370)

b1= Button(window,text='Submit',bg="sky blue",fg="black",command=action)
b1.place(x=150,y=420)

window.minsize(width=600,height=800)
window.maxsize(width=601,height=801)
window.mainloop()