import tkinter as tk
import sqlite3
from tkinter import ttk, messagebox

#creates database
con = sqlite3.connect("employees.db")
con.execute("CREATE TABLE IF NOT EXISTS employee(NAME text, AGE text, doe text, email text, gender text, contact text, address text, position text);")

#inserts the data input from main window to the database
def insert_data(name, age, doe, email, gender, contact, address, position):
    conn = sqlite3.connect("employees.db")
    conn.execute("INSERT INTO employee(name, age, doe, email, gender, contact, address, position) VALUES( '" + name + "', '" + age +"', '" + doe + "', '" + email + "', '" + gender + "', '" + contact + "', '" + address + "', '" + position + "' );")
    conn.commit()
    conn.close()
    messagebox.showinfo("Success", "Data Saved Successfully.")

#-------------------------------------------------------------------------------------------------------------------------------------


#function called to the main window
def insert():
    add_window = tk.Tk()
    add_window.title("Add Employee Details")
    tk.Label(add_window).grid(row=0, column=0, columnspan=2)

    tk.Label(add_window, text="Employee Name:", font=("georgia", "12")).grid(row=3, column=0, sticky="W", padx=10, pady=10)
    name_entry = tk.Entry(add_window, width=55, relief='ridge', bd=3)
    name_entry.grid(row=3, column=1, sticky="W", padx=10, pady=10)

    tk.Label(add_window, text="Age:", font=("georgia", "12")).grid(row=4, column=0, sticky="W", padx=10, pady=10)
    age_entry = tk.Entry(add_window, width=55, relief='ridge', bd=3)
    age_entry.grid(row=4, column=1, sticky="W", padx=10, pady=10)

    tk.Label(add_window, text="Date of Employment:", font=("georgia", "12")).grid(row=5, column=0, sticky="W", padx=10, pady=10)
    doe_entry = tk.Entry(add_window, width=55, relief='ridge', bd=3)
    doe_entry.grid(row=5, column=1, sticky="W", padx=10, pady=10)

    tk.Label(add_window, text="Email:", font=("georgia", "12")).grid(row=6, column=0, sticky="W", padx=10, pady=10)
    email_entry = tk.Entry(add_window, width=55, relief='ridge', bd=3)
    email_entry.grid(row=6, column=1, sticky="W", padx=10, pady=10)
    
    tk.Label(add_window, text="Gender:", font=("georgia", "12")).grid(row=7, column=0, sticky="W", padx=10, pady=10)
    options = tk.StringVar()
    gender_entry = ttk.Combobox(add_window, width=52, textvariable=options)
    gender_entry['values'] = ('Male', "Female", "Other")
    gender_entry.grid(row=7, column=1, sticky="W", padx=10, pady=10)

    tk.Label(add_window, text="Contact:", font=("georgia", "12")).grid(row=8, column=0, sticky="W", padx=10, pady=10)
    contact_entry = tk.Entry(add_window, width=55, relief='ridge', bd=3)
    contact_entry.grid(row=8, column=1, sticky="W", padx=10, pady=10)

    tk.Label(add_window, text="Address:", font=("georgia", "12")).grid(row=9, column=0, sticky="W", padx=10, pady=10)
    address_entry = tk.Entry(add_window, width=55, relief='ridge', bd=3)
    address_entry.grid(row=9, column=1, sticky="W", padx=10, pady=10)
    
    tk.Label(add_window, text="Company Position:", font=("georgia", "12")).grid(row=10, column=0, sticky="W", padx=10, pady=10)
    options = tk.StringVar()
    position_entry = ttk.Combobox(add_window, width=52, textvariable=options)
    position_entry['values'] = ('Chief Executive Officer', "Chief Operating Officer", "Chief Financial Officer",
                                "Chief Financial Officer", "President", "Executive Vice President",
                                "Senior Vice President", "Vice President", "Assistant Vice President",
                                "Associate Vice President", "Senior Director", "Aassistant Director",
                                "Manager", "Middle Manager", "Others")
    position_entry.grid(row=10, column=1, sticky="W", padx=10, pady=10)

    tk.Button(add_window, text='Submit', font=("georgia", "12"), activebackground='#7F5C88', activeforeground='white', bg='#6400B5', fg = 'white', relief = 'groove', bd=10, command=lambda: submit()).grid(row=11, column=0, columnspan=2, pady=10)

    def submit():
        name = name_entry.get()
        age = age_entry.get()
        doe = doe_entry.get()
        email = email_entry.get()
        gender = gender_entry.get()
        contact = contact_entry.get()
        address = address_entry.get()
        position = position_entry.get()
        insert_data(name, age, doe, email, gender, contact, address, position)
        add_window.destroy()

    add_window.mainloop()

#-------------------------------------------------------------------------------------------------------------------------------------

#function called to the main window
def display():
    connn = sqlite3.connect("employees.db")
    display_window = tk.Tk()
    display_window.title("View Employee Details")
    table = ttk.Treeview(display_window)
    table["columns"] = ("one", "two", "three", "four", "five", "six", "seven", "eight")

    table.heading("one", text="Name")
    table.heading("two", text="Age")
    table.heading("three", text="Date of Employment")
    table.heading("four", text="Email")
    table.heading("five", text="Gender")
    table.heading("six", text="Contact")
    table.heading("seven", text="Address")
    table.heading("eight", text="Company Position")

    cursor = connn.execute("SELECT rowid,* FROM employee;")
    i = 0
    for row in cursor:
        table.insert('', i, text="Employee ID Number " + str(row[0]), values=(row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]))
        i = i + 1
    table.pack()
    connn.close()

#-------------------------------------------------------------------------------------------------------------------------------------

#function called to the main window
def update():
    update_window = tk.Tk()
    update_window.title("Update Employee Details")
    
    tk.Label(update_window, text="Enter the ID Number of Employee to be Updated:", font=("georgia", "12")).grid(row=0, column=0, sticky="W", padx=10, columnspan=2)
    s_id = tk.Entry(update_window, width=77, relief='ridge', bd=3)
    s_id.grid(row=1, column=0, sticky="W", padx=10, columnspan=2)

    tk.Label(update_window, text="\nEnter the new values:", font=("georgia", "12")).grid(row=2, column=0, sticky="W", padx=10, pady=10, columnspan=2)

    tk.Label(update_window, text="Name:", font=("georgia", "12")).grid(row=3, column=0, sticky="W", padx=10, pady=10)
    s_name = tk.Entry(update_window, width=55, relief='ridge', bd=3)
    s_name.grid(row=3, column=1, sticky="W", padx=10, pady=10)

    tk.Label(update_window, text="Age:", font=("georgia", "12")).grid(row=4, column=0, sticky="W", padx=10, pady=10)
    s_age = tk.Entry(update_window, width=55, relief='ridge', bd=3)
    s_age.grid(row=4, column=1, sticky="W", padx=10, pady=10)
    

    tk.Label(update_window, text="Date of Employment:", font=("georgia", "12")).grid(row=5, column=0, sticky="W", padx=10, pady=10)
    s_doe = tk.Entry(update_window, width=55, relief='ridge', bd=3)
    s_doe.grid(row=5, column=1, sticky="W", padx=10, pady=10)

    tk.Label(update_window, text="Email:", font=("georgia", "12")).grid(row=6, column=0, sticky="W", padx=10, pady=10)
    s_email = tk.Entry(update_window, width=55, relief='ridge', bd=3)
    s_email.grid(row=6, column=1, sticky="W", padx=10, pady=10)

    tk.Label(update_window, text="Gender:", font=("georgia", "12")).grid(row=7, column=0, sticky="W", padx=10, pady=10)
    options = tk.StringVar()
    s_gender= ttk.Combobox(update_window, width=52, textvariable=options)
    s_gender['values'] = ('Male', "Female", "Other")
    s_gender.grid(row=7, column=1, sticky="W", padx=10, pady=10)

    tk.Label(update_window, text="Contact:", font=("georgia", "12")).grid(row=8, column=0, sticky="W", padx=10, pady=10)
    s_contact = tk.Entry(update_window, width=55, relief='ridge', bd=3)
    s_contact.grid(row=8, column=1, sticky="W", padx=10, pady=10)

    tk.Label(update_window, text="Address:", font=("georgia", "12")).grid(row=9, column=0, sticky="W", padx=10, pady=10)
    s_address = tk.Entry(update_window, width=55, relief='ridge', bd=3)
    s_address.grid(row=9, column=1, sticky="W", padx=10, pady=10)
    
    tk.Label(update_window, text="Company Position:", font=("georgia", "12")).grid(row=10, column=0, sticky="W", padx=10, pady=10)
    options = tk.StringVar()
    s_position = ttk.Combobox(update_window, width=52, textvariable=options)
    s_position['values'] = ('Chief Executive Officer', "Chief Operating Officer", "Chief Financial Officer",
                                "Chief Financial Officer", "President", "Executive Vice President",
                                "Senior Vice President", "Vice President", "Assistant Vice President",
                                "Associate Vice President", "Senior Director", "Aassistant Director",
                                "Manager", "Middle Manager", "Others")
    s_position.grid(row=10, column=1, sticky="W", padx=10, pady=10)

    tk.Button(update_window, text="Update", font=("georgia", "12"), activebackground='#7F5C88', activeforeground='white',
              bg='#6400B5', fg = 'white', relief = 'groove', bd=10, command=lambda: submit()).grid(row=12, column=0, padx=10, pady=10, columnspan=2)

    def submit():
        sid = s_id.get()
        sname = s_name.get()
        sage = s_age.get()
        sdoe = s_doe.get()
        semail = s_email.get()
        sgender = s_gender.get()
        scontact = s_contact.get()
        saddress = s_address.get()
        sposition = s_position.get()
        scon = sqlite3.connect("employees.db")
        scon.execute("UPDATE employee SET name = '" + sname + "', age = '" + sage + "', doe = '" + sdoe +"', email = '" + semail + "', gender = '" + sgender + "', contact = '" + scontact + "', address = '" + saddress + "', position = '" + sposition + "' WHERE rowid = " + sid + ";")
        scon.commit()
        scon.close()
        messagebox.showinfo("Success", "Data Updated Successfully.")
        update_window.destroy()
    update_window.mainloop()

#function called to the main window
def delete():
    delete_window = tk.Tk()
    delete_window.title("Delete Employee ")
    tk.Label(delete_window, text="Enter Employee Name whose details are to be removed:", font=("georgia", "12")).grid(row=0, column=0, padx=10, pady=10)
    d_name = tk.Entry(delete_window, width=55, relief='ridge', bd=3)
    d_name.grid(row=0, column=1, padx=10, pady=10)
    tk.Button(delete_window, text="Delete Details", font=("georgia", "12"), relief='groove', bd=10, activebackground='#7F5C88', activeforeground='white',
              bg='#6400B5', fg = 'white', command=lambda: submit()).grid(row=1, column=0, columnspan=2)
    tk.Label(delete_window).grid(row=2, column=0, columnspan=2)

    def submit():
        dname = d_name.get()
        dcon = sqlite3.connect("employees.db")
        dcon.execute("DELETE FROM employee WHERE name = '" + dname+"';")
        dcon.commit()
        dcon.close()
        messagebox.showinfo("Success", "Deleted Successfully.")
        delete_window.destroy()
    delete_window.mainloop()

#function called to the main window
def search():
    search_window = tk.Tk()
    search_window.title("Search Employee Details")

    tk.Label(search_window, text="Enter the name of Employee whose details are to be searched:", font=("georgia", "12")).grid(row=0, column=0,
                                                                                                     padx=10, pady=10)
    f_name = tk.Entry(search_window, width=55)
    f_name.grid(row=0, column=1, padx=10, pady=10)

    tk.Label(search_window, text="Results:", font=("georgia", "12")).grid(row=1, column=0, sticky="W", columnspan=2, padx=10, pady=10)

    tk.Button(search_window, text="Search", font=("georgia", "12"), relief='groove', bd=10, activebackground='#7F5C88', activeforeground='white',
              bg='#6400B5', fg = 'white', command=lambda: submit()).grid(row=2, column=0, columnspan=2)
    tk.Label(search_window).grid(row=3, column=0, sticky="W", columnspan=2, padx=10, pady=10)
    details = ttk.Treeview(search_window)
    details["columns"] = ("one", "two", "three", "four", "five", "six", "seven", "eight")

    details.heading("one", text="Name")
    details.heading("two", text="Age")
    details.heading("three", text="Date of Employment")
    details.heading("four", text="Email")
    details.heading("five", text="Gender")
    details.heading("six", text="Contact")
    details.heading("seven", text="Address")
    details.heading("eight", text="Company Position")


    def submit():
        for row in details.get_children():
            details.delete(row)

        fname = f_name.get()
        fcon = sqlite3.connect("employees.db")
        cursor = fcon.execute("SELECT rowid,* from employee WHERE name = '" + fname + "';")
        fcon.commit()

        i = 0
        for row in cursor:
            details.insert('', i, text="Employee ID Number" + str(row[0]), values=(row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]))
            i = i + 1

        details.grid(row=4, column=0, columnspan=2, padx=10, pady=10)
        fcon.close()
    search_window.mainloop()


con.close()