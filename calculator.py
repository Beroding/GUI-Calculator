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

# def equal():


btn_1 = tk.Button(master=frame, text=1, padx=30, pady=10, width=3, command=lambda: click(1))
btn_1.grid(row=1, column=0, pady=2)

btn_2 = tk.Button(master=frame, text=2, padx=30,pady=10, width=3, command=lambda: click(2))
btn_2.grid(row=1, column=1, pady=2)

btn_3 = tk.Button(master=frame, text=3, padx=30, pady=10, width=3, command=lambda: click(3))
btn_3.grid(row=1, column=2, pady=2)

btn_4 = tk.Button(master=frame, text=4, padx=30, pady=10, width=3, command=lambda: click(4))
btn_4.grid(row=2, column=0, pady=2)

btn_5 = tk.Button(master=frame, text=5, padx=30, pady=10, width=3, command=lambda: click(5))
btn_5.grid(row=2, column=1, pady=2)

btn_6 = tk.Button(master=frame, text=6, padx=30, pady=10, width=3, command=lambda: click(6))
btn_6.grid(row=2, column=2, pady=2)

btn_7 = tk.Button(master=frame, text=7, padx=30, pady=10, width=3, command=lambda: click(7))
btn_7.grid(row=3, column=0, pady=2)

btn_8 = tk.Button(master=frame, text=8, padx=30, pady=10, width=3, command=lambda: click(8))
btn_8.grid(row=3, column=1, pady=2)

btn_9 = tk.Button(master=frame, text=9, padx=30, pady=10, width=3, command=lambda: click(9))
btn_9.grid(row=3, column=2, pady=2)

btn_0 = tk.Button(master=frame, text=0, padx=30, pady=10, width=3, command=lambda: click(0))
btn_0.grid(row=4, column=1, pady=2)

btn_plus = tk.Button(master=frame, text='+', padx=30, pady=10, width=3, command=lambda: click('+'))
btn_plus.grid(row=5, column=0, pady=2)

btn_minus = tk.Button(master=frame, text='-', padx=30, pady=10, width=3, command=lambda: click('-'))
btn_plus.grid(row=5, column=1, pady=2)

btn_times = tk.Button(master=frame, text='*', padx=30, pady=10, width=3, command=lambda: click('*'))
btn_times.grid(row=5, column=2, pady=2)

btn_delete = tk.Button(master=frame, text='<', padx=30, pady=10, width=3, command=lambda: entry.delete(len(entry.get()) - 1))
btn_delete.grid(row=4, column=2, pady=3)

btn_equal = tk.Button(master=frame, text='=', padx=30, pady=10, width=3, command=eval)
btn_equal.grid(row=6, column=2, pady=5)

tab.mainloop()