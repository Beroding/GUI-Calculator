import tkinter as tk


tab = tk.Tk()
tab.title('Calculator_Project')
frame = tk.Frame(master=tab, bg="black", padx=10)
frame.pack()
entry = tk.Entry(master=frame)
entry.grid(row=0, column=0, columnspan=3, ipady=2, pady=2)



tab.mainloop()