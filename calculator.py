import tkinter as tk


tab = tk.Tk()
tab.title('Calculator_Project')
frame = tk.Frame(master=tab, bg="black", padx=200, pady=200)
frame.pack()
entry = tk.Entry(master=frame)
entry.grid(row=0, column=0, columnspan=3, ipady=2, pady=20)

def click(num):
    entry.insert(tk.END, num)

def clear():
    entry.delete(0, tk.END)

btn_1 = tk.Button(master=frame, text=1, padx=30, pady=10, width=3, command=lambda: myclick(1))
btn_1.grid(row=1, column=0, pady=2)

btn_2 = tk.Button(master=frame, text=2, padx=30,pady=10, width=3, command=lambda: myclick(2))
btn_2.grid(row=1, column=1, pady=2)

btn_3 = tk.Button(master=frame, text=3, padx=30, pady=10, width=3, command=lambda: myclick(3))
btn_3.grid(row=1, column=2, pady=2)

btn_4 = tk.Button(master=frame, text=4, padx=30, pady=10, width=3, command=lambda: myclick(4))
btn_4.grid(row=2, column=0, pady=2)

btn_5 = tk.Button(master=frame, text=5, padx=30, pady=10, width=3, command=lambda: myclick(5))
btn_5.grid(row=2, column=1, pady=2)

btn_6 = tk.Button(master=frame, text=6, padx=30, pady=10, width=3, command=lambda: myclick(6))
btn_6.grid(row=2, column=2, pady=2)

btn_7 = tk.Button(master=frame, text=7, padx=30, pady=10, width=3, command=lambda: myclick(7))
btn_7.grid(row=3, column=0, pady=2)

btn_8 = tk.Button(master=frame, text=8, padx=30, pady=10, width=3, command=lambda: myclick(8))
btn_8.grid(row=3, column=1, pady=2)

btn_9 = tk.Button(master=frame, text=9, padx=30, pady=10, width=3, command=lambda: myclick(9))
btn_9.grid(row=3, column=2, pady=2)

btn_0 = tk.Button(master=frame, text=0, padx=30, pady=10, width=3, command=lambda: myclick(0))
btn_0.grid(row=4, column=1, pady=2)

tab.mainloop()