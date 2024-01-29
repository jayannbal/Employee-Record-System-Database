import tkinter as tk
import Balatero_Enriquez_Employee_Record_System_database as ed

#this window does function call from the other python file.

mainWindow = tk.Tk()
mainWindow.title('Employee Record System')
mainWindow.geometry("2000x1800+0+0")
mainWindow.configure(bg='#F6FAE7')


label_1 = tk.Label(mainWindow, text="EMPLOYEE RECORD SYSTEM", font='georgia 50 bold', relief='ridge', bd=50, bg='#6400B5', fg = 'white')
label_1.pack(padx=100, pady=50)

button_1 = tk.Button(mainWindow, text="Add Employee", command=lambda: ed.insert(), padx=275, pady=25,
                     font = 'georgia 10 bold', activebackground='#B7837A', activeforeground='white', relief='groove', bd=10, bg = '#F6E9E7')
button_1.pack()

button_2 = tk.Button(mainWindow, text="Update Employee", command=lambda: ed.update(), padx=264, pady=25,
                     font = 'georgia 10 bold', activebackground='#B7837A', activeforeground='white', relief='groove', bd=10, bg = '#F6E9E7')
button_2.pack()

button_3 = tk.Button(mainWindow, text="View Employee", command=lambda: ed.display(), padx=272, pady=25,
                     font = 'georgia 10 bold', activebackground='#B7837A', activeforeground='white', relief='groove', bd=10, bg = '#F6E9E7')
button_3.pack()

button_4 = tk.Button(mainWindow, text="Delete Employee", command=lambda: ed.delete(), padx=267, pady=25,
                     font = 'georgia 10 bold', activebackground='#B7837A', activeforeground='white', relief='groove', bd=10, bg = '#F6E9E7')
button_4.pack()

button_5 = tk.Button(mainWindow, text="Search Employee", command=lambda: ed.search(), padx=266, pady=25,
                     font = 'georgia 10 bold', activebackground='#B7837A', activeforeground='white', relief='groove', bd=10, bg = '#F6E9E7')
button_5.pack()

mainWindow.mainloop()