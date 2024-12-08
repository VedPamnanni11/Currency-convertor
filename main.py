from currency_converter import CurrencyConverter
import tkinter as tk
a = CurrencyConverter()
window = tk.Tk()
window.geometry("500x360")

def clicked():
    amount = int(e1.get())
    cur1 = e2.get()
    cur2 = e3.get()
    data = a.convert(amount, cur1, cur2)
    l5 = tk.Label(window, text=data, font="Times 25 bold").place(x=200, y=290)

l1 = tk.Label(window, text="Currency Convertor", font="Times 25 bold").place(x=100,y=30)
l2 = tk.Label(window, text="Enter amount here: ", font="Times 18 bold").place(x=50, y=80)
e1 = tk.Entry(window)

l3 = tk.Label(window, text="Enter from currency: ", font="Times 18 bold").place(x=50, y=130)
e2 = tk.Entry(window)

l4 = tk.Label(window, text="Enter to currency: ", font="Times 18 bold").place(x=50, y=180)
e3 = tk.Entry(window)

b1 = tk.Button(window, text="Convert", command=clicked).place(x=230, y=240)
e1.place(x=300, y=90)
e2.place(x=300, y=140)
e3.place(x=300, y=190)
window.mainloop()




# a = CurrencyConverter()
# print(a.convert(12, "USD", "INR"))