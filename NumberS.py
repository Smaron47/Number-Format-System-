
'''
to do list next day the edit,delete needed and some ui to be added.
'''




import winreg
from tkinter import *
import sqlite3
from tkinter import messagebox,simpledialog
import customtkinter
import time

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"
customtkinter.set_widget_scaling(1.2)





class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        
        # configure window
        self.title("Number Format")
        self.geometry(f"{1100}x{580}")

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)
        self.create_table()
        self.opts()
        
        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=2, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(11, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Dashboard", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame,text="Clear All", command=self.buttonw)
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame,text="New Preset", command=self.add_new_set_layout)
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)
        self.sidebar_button_3 = customtkinter.CTkButton(self.sidebar_frame,text="Edit Preset", command=self.edit_l)
        self.sidebar_button_3.grid(row=3, column=0, padx=20, pady=10)
        self.sidebar_button_5 = customtkinter.CTkButton(self.sidebar_frame,text="Delete Preset", command=self.delete_l)
        self.sidebar_button_5.grid(row=4, column=0, padx=20, pady=10)
        self.sidebar_button_4 = customtkinter.CTkButton(self.sidebar_frame,text="Default", command=self.defo)
        self.sidebar_button_4.grid(row=5, column=0, padx=20, pady=10)
        self.sidebar_button_4 = customtkinter.CTkButton(self.sidebar_frame,text="Select PreSet", command=self.change_command)
        self.sidebar_button_4.grid(row=6, column=0, padx=20, pady=10)
        self.sidebar_button_4 = customtkinter.CTkButton(self.sidebar_frame,text="Timer", command=self.start_timer)
        self.sidebar_button_4.grid(row=7, column=0, padx=20, pady=10)
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=8, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],
                                                                        command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=9, column=0, padx=20, pady=(10, 10))
        
        # self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        # self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        # self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"],
        #                                                        command=self.change_scaling_event)
        # self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))

        # create main entry and button
        # self.entry = customtkinter.CTkEntry(self, placeholder_text="CTkEntry")
        # self.entry.grid(row=3, column=1, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew")

        # self.main_button_1 = customtkinter.CTkButton(master=self, fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"))
        # self.main_button_1.grid(row=3, column=3, padx=(20, 20), pady=(20, 20), sticky="nsew")

        # create textbox

    def start_timer(self):
        # Create a dialog box to get the timer duration from the user
        duration = self.get_duration()
        if duration:
            # Convert the duration to seconds
            seconds = int(duration.split(':')[0]) * 60 + int(duration.split(':')[1])
            # Start the timer
            self.timer = time.time() + seconds
            self.update_timer()

    def stop_timer(self):
        # Stop the timer
        self.timer = None
        

    def update_timer(self):
        if self.timer:
            # Get the remaining time in seconds
            remaining = self.timer - time.time()
            if remaining > 0:
                # Convert the remaining time to minutes and seconds
                minutes = int(remaining // 60)
                seconds = int(remaining % 60)
                # Update the timer label
                
                # Schedule the update to occur again after 1 second
                self.after(1000, self.update_timer)
            else:
                # Stop the timer when it reaches 0
                self.stop_timer()
                # Call the function you want to execute when the timer ends
                self.timer_ended()

    def get_duration(self):
        # Create a dialog box to get the timer duration from the user
        duration = simpledialog.askstring('Timer Duration', 'Enter the duration in the format HH:MM:')
        return duration

    def timer_ended(self):
        # Display a message box when the timer ends
        self.change(",",".")
        messagebox.showinfo('Time Ended', f'Back To Default Mode \n Format-> \n 123.456,987!')
    def create_table(self):
        # Connect to the database and create the customer table
        conn = sqlite3.connect('customer.db')
        c = conn.cursor()

        c.execute("""CREATE TABLE IF NOT EXISTS customer (
                        firstname text,
                        lastname text,
                        email text,
                        time text
                    )""")

        conn.commit()
        conn.close()
    def change(self,dot,com):

        # Open the registry key for the number format settings
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, 'Control Panel\\International', 0, winreg.KEY_ALL_ACCESS)

        # Set the desired number format options
        decimal_symbol = dot
        grouping_symbol = com
        number_format = '#,##0.00'

        # Set the number format options in the registry
        winreg.SetValueEx(key, 'sDecimal', 0, winreg.REG_SZ, decimal_symbol)
        winreg.SetValueEx(key, 'sThousand', 0, winreg.REG_SZ, grouping_symbol)
        winreg.SetValueEx(key, 'sPositivePattern', 0, winreg.REG_SZ, number_format)
        winreg.SetValueEx(key, 'sNegativePattern', 0, winreg.REG_SZ, number_format)

        # Close the registry key
        winreg.CloseKey(key)
        print("Change Done")
        
        

    def change_without_save_format(self):
        
        try:
            self.delet_all()
        except:
            pass
        self.label_fr=customtkinter.CTkLabel(self, text=f"Change The Format",font=("Courier",34,"bold"))
        self.label_fr.grid(row=0, column=1)
        self.frm=customtkinter.CTkFrame(self)
        self.frm.grid(row=1, column=1)
        self.label_firstname = customtkinter.CTkLabel(self.frm, text="Decimal point")
        self.label_firstname.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

        self.entry_firstname = customtkinter.CTkEntry(self.frm)
        self.entry_firstname.grid(row=0, column=2, padx=5, pady=5, sticky="ew")
        
        self.label_lastname = customtkinter.CTkLabel(self.frm, text="Digit Group")
        self.label_lastname.grid(row=0, column=3, padx=5, pady=5, sticky="ew")

        self.entry_lastname =  customtkinter.CTkEntry(self.frm)
        self.entry_lastname.grid(row=0, column=4, padx=5, pady=5, sticky="ew")
        self.button_search = customtkinter.CTkButton(self.frm, text="Done", command=self.change_without_save)
        self.button_search.grid(row=2, column=2, padx=20, pady=10)


    def change_without_save(self):

        doc=self.entry_firstname.get()
        com=self.entry_lastname.get()
        self.change(doc,com)
        self.delet_all()
        self.frm2=customtkinter.CTkFrame(self)
        self.frm2.grid(row=0,column=1)
        
        self.label_firstname2 = customtkinter.CTkLabel(self.frm2, text="New Format Updated")
        self.label_firstname2.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
    def add_new_set_layout(self):
        try:
            self.delet_all()
        except:
            pass
        self.label_fr=customtkinter.CTkLabel(self, text=f"Add New Set",font=("Courier",34,"bold"))
        self.label_fr.grid(row=0, column=1)
        self.frm=customtkinter.CTkFrame(self)
        self.frm.grid(row=1, column=1)
        self.label_firstname = customtkinter.CTkLabel(self.frm, text="Name")
        self.label_firstname.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

        self.entry_firstname = customtkinter.CTkEntry(self.frm)
        self.entry_firstname.grid(row=0, column=2, padx=5, pady=5, sticky="ew")
        
        self.label_lastname = customtkinter.CTkLabel(self.frm, text="Decimal")
        self.label_lastname.grid(row=0, column=3, padx=5, pady=5, sticky="ew")

        self.entry_lastname =  customtkinter.CTkEntry(self.frm)
        self.entry_lastname.grid(row=0, column=4, padx=5, pady=5, sticky="ew")
        
        self.label_email = customtkinter.CTkLabel(self.frm, text="Digit Group")
        self.label_email.grid(row=1, column=1, padx=5, pady=5)

        self.entry_email =  customtkinter.CTkEntry(self.frm)
        self.entry_email.grid(row=1, column=2, padx=5, pady=5)

        self.label_date = customtkinter.CTkLabel(self.frm, text="Time to Defoulte")
        self.label_date.grid(row=1, column=3, padx=5, pady=5)

        self.entry_date =  customtkinter.CTkEntry(self.frm)
        self.entry_date.grid(row=1, column=4, padx=5, pady=5)
        # Buttons
        self.button_search = customtkinter.CTkButton(self.frm, text="Add", command=self.add_new_set)
        self.button_search.grid(row=2, column=2, padx=20, pady=10)







    def add_new_set(self):
        firstname = self.entry_firstname.get()
        lastname = self.entry_lastname.get()
        email = self.entry_email.get()
        time=self.entry_date.get()
        conn = sqlite3.connect('customer.db')
        c = conn.cursor()
        c.execute("INSERT INTO customer VALUES (?, ?, ?, ?)",
                            (firstname, lastname, email, time))

        conn.commit()
        conn.close()

        self.change(lastname,email)
        self.delet_all()
        self.frm2=customtkinter.CTkFrame(self)
        self.frm2.grid(row=0,column=1)
        
        self.label_firstname2 = customtkinter.CTkLabel(self.frm2, text="New Format Updated")
        self.label_firstname2.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
        self.opts()
        
    def select_preset_layout(self):
        try:
            self.delet_all()
        except:
            pass
        self.label_fr=customtkinter.CTkLabel(self, text=f"Select Preset",font=("Courier",34,"bold"))
        self.label_fr.grid(row=0, column=1)
        self.frm=customtkinter.CTkFrame(self)
        self.frm.grid(row=1, column=1)
        self.label_firstname = customtkinter.CTkLabel(self.frm, text="Name")
        self.label_firstname.grid(row=0, column=0, padx=5, pady=5, sticky="ew")


        li=self.li

        
        self.option_m=customtkinter.CTkOptionMenu(self.frm,values=li,command=self.change_command)
        self.option_m.grid(row=2, column=0, padx=5, pady=5, sticky="ew")
    def opts(self):
        conn = sqlite3.connect("customer.db")

# create a cursor object to execute SQL commands
        cur = conn.cursor()

        # execute a SELECT query to retrieve the options from the database
        cur.execute("SELECT firstname FROM customer")

        # fetch all the results
        options = cur.fetchall()

        # create a new tkinter window
        self.li=[]
        for option in options:
            self.li.append(option[0])

    def buttonw(self):
        for i in range(self.grid_size()[1]):
            self.grid_slaves(row=i, column=1)[0].grid_forget()
    def defo(self):
        self.change(",",".")
    def change_command(self):
        #print(option_m)]
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,r'Control Panel\International', 0,
                    winreg.KEY_READ)

# Get the decimal point character from the registry
        decimal_point = winreg.QueryValueEx(key, 'sDecimal')[0]

        # Get the grouping symbol from the registry
        grouping_symbol = winreg.QueryValueEx(key, 'sThousand')[0]

        # Close the registry key
        winreg.CloseKey(key)

        
        self.label_fr=customtkinter.CTkLabel(self, text=f"Select Preset\nCurrent Format\n123{grouping_symbol}456{decimal_point}987",font=("Courier",34,"bold"))
        self.label_fr.grid(row=0, column=1)
        self.frm=customtkinter.CTkFrame(self)
        self.frm.grid(row=1, column=1)
        self.label_firstname = customtkinter.CTkLabel(self.frm, text=f" D ---- H ")
        self.label_firstname.grid(row=0, column=2, padx=5, pady=5, sticky="ew")
        conn=sqlite3.connect("customer.db")
        c=conn.cursor()
        c.execute("select * from customer")
        row=c.fetchall()
        conn.commit()
        conn.close()
        print(len(row))
        o=0
        self.label_lastname=customtkinter.CTkLabel(self.frm,text=f'Number Format')
        self.label_lastname.grid(row=0, column=1)
        while o < len(row):
            arg1=row[o][1]
            arg2=row[o][2]
            def button_clicked(arg1=arg1, arg2=arg2):
                self.change(arg1, arg2)
            self.label_email=customtkinter.CTkLabel(self.frm,text=f'123{row[o][1]}456{row[o][2]}000')
            self.label_email.grid(row=o+1, column=1)
            self.label_date=customtkinter.CTkLabel(self.frm,text=f'" {row[o][1]} " ---- " {row[o][2]} "  ')
            self.label_date.grid(row=o+1, column=2)
            self.label_amount=customtkinter.CTkLabel(self.frm,text=row[o][0])
            self.label_amount.grid(row=o+1, column=0)
            self.button_search = customtkinter.CTkButton(self.frm, text="Use", command=button_clicked)
            self.button_search.grid(row=o+1, column=3, padx=20, pady=10)
            o+=1
    def edit_l(self):
        self.label_fr=customtkinter.CTkLabel(self, text=f"Edit Preset",font=("Courier",34,"bold"))
        self.label_fr.grid(row=0, column=1)
        self.frm=customtkinter.CTkFrame(self)
        self.frm.grid(row=1, column=1)
        self.label_firstname = customtkinter.CTkLabel(self.frm, text=f" D ---- H ")
        self.label_firstname.grid(row=0, column=2, padx=5, pady=5, sticky="ew")
        conn=sqlite3.connect("customer.db")
        c=conn.cursor()
        c.execute("select * from customer")
        row=c.fetchall()
        conn.commit()
        conn.close()
        print(len(row))
        o=0
        self.label_lastname=customtkinter.CTkLabel(self.frm,text=f'Number Format')
        self.label_lastname.grid(row=0, column=1)
        while o < len(row):
            arg1=row[o][0]
            arg2=row[o][2]
            def button_clicked(arg1=arg1):
                self.edit_layout(arg1)
            self.label_email=customtkinter.CTkLabel(self.frm,text=f'123{row[o][1]}456{row[o][2]}000')
            self.label_email.grid(row=o+1, column=1)
            self.label_date=customtkinter.CTkLabel(self.frm,text=f'" {row[o][1]} " ---- " {row[o][2]} "  ')
            self.label_date.grid(row=o+1, column=2)
            self.label_amount=customtkinter.CTkLabel(self.frm,text=row[o][0])
            self.label_amount.grid(row=o+1, column=0)
            self.button_search = customtkinter.CTkButton(self.frm, text="Edit", command=button_clicked)
            self.button_search.grid(row=o+1, column=3, padx=20, pady=10)
            o+=1
    def delete_l(self):
        self.label_fr=customtkinter.CTkLabel(self, text=f"Delete Preset",font=("Courier",34,"bold"))
        self.label_fr.grid(row=0, column=1)
        self.frm=customtkinter.CTkFrame(self)
        self.frm.grid(row=1, column=1)
        self.label_firstname = customtkinter.CTkLabel(self.frm, text=f" D ---- H ")
        self.label_firstname.grid(row=0, column=2, padx=5, pady=5, sticky="ew")
        conn=sqlite3.connect("customer.db")
        c=conn.cursor()
        c.execute("select * from customer")
        row=c.fetchall()
        conn.commit()
        conn.close()
        print(len(row))
        o=0
        self.label_lastname=customtkinter.CTkLabel(self.frm,text=f'Number Format')
        self.label_lastname.grid(row=0, column=1)
        while o < len(row):
            arg1=row[o][0]
            arg2=row[o][2]
            def button_clicked(arg1=arg1):
                self.delete_layout(arg1)
            self.label_email=customtkinter.CTkLabel(self.frm,text=f'123{row[o][1]}456{row[o][2]}000')
            self.label_email.grid(row=o+1, column=1)
            self.label_date=customtkinter.CTkLabel(self.frm,text=f'" {row[o][1]} " ---- " {row[o][2]} "  ')
            self.label_date.grid(row=o+1, column=2)
            self.label_amount=customtkinter.CTkLabel(self.frm,text=row[o][0])
            self.label_amount.grid(row=o+1, column=0)
            self.button_search = customtkinter.CTkButton(self.frm, text="Delete", command=button_clicked)
            self.button_search.grid(row=o+1, column=3, padx=20, pady=10)
            o+=1
    def current(self):
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,r'Control Panel\International', 0,
                    winreg.KEY_READ)

# Get the decimal point character from the registry
        decimal_point = winreg.QueryValueEx(key, 'sDecimal')[0]

        # Get the grouping symbol from the registry
        grouping_symbol = winreg.QueryValueEx(key, 'sThousand')[0]

        # Close the registry key
        winreg.CloseKey(key)

        
        self.label_fr=customtkinter.CTkLabel(self, text=f"Current Format\n123{grouping_symbol}456{decimal_point}987",font=("Courier",34,"bold"))
        self.label_fr.grid(row=0, column=1)
    def edit_layout(self,sidebar_button_3):
        try:
            self.delet_all()
        except:
            pass
        self.delet_all()
            # Get the email to search for from the user
        search_email = sidebar_button_3
        self.pm=search_email
        conn=sqlite3.connect("customer.db")
        c=conn.cursor()
        c.execute("SELECT * FROM customer WHERE firstname=?",(search_email,))
        row=c.fetchall()
        print(row)
        conn.commit()
        conn.close()
        self.label_fr=customtkinter.CTkLabel(self, text=f"{row[0][0]}",font=("Courier",34,"bold"))
        self.label_fr.grid(row=0, column=1)
        self.frm=customtkinter.CTkFrame(self)
        self.frm.grid(row=1, column=1)
        self.label_lastname = customtkinter.CTkLabel(self.frm, text="Decimal")
        self.label_lastname.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

        self.entry_lastname =  customtkinter.CTkEntry(self.frm)
        self.entry_lastname.grid(row=0, column=2, padx=5, pady=5, sticky="ew")
        
        self.label_email = customtkinter.CTkLabel(self.frm, text="Digit Group")
        self.label_email.grid(row=1, column=1, padx=5, pady=5)

        self.entry_email =  customtkinter.CTkEntry(self.frm)
        self.entry_email.grid(row=1, column=2, padx=5, pady=5)

        self.label_date = customtkinter.CTkLabel(self.frm, text="Time to Defoulte")
        self.label_date.grid(row=1, column=3, padx=5, pady=5)
        self.entry_date =  customtkinter.CTkEntry(self.frm)
        self.entry_date.grid(row=1, column=4, padx=5,pady=5)
        self.button_search = customtkinter.CTkButton(self.frm, text="Update", command=self.edit)
        self.button_search.grid(row=2, column=2, padx=20, pady=10)

    def edit(self):
        #firstname = self.entry_firstname.get()
        lastname = self.entry_lastname.get()
        print(type(lastname))
        email = self.entry_email.get()
        time=self.entry_date.get()
        conn = sqlite3.connect('customer.db')
        c = conn.cursor()
        c.execute(f"UPDATE customer SET firstname='{self.pm}', lastname='{lastname}', email='{email}', time='{time}' WHERE firstname='{self.pm}'")
        conn.commit()
        conn.close()
        self.delet_all()
        self.frm2=customtkinter.CTkFrame(self)
        self.frm2.grid(row=0,column=1)
        
        self.label_firstname2 = customtkinter.CTkLabel(self.frm2, text="New Format Updated")
        self.label_firstname2.grid(row=0, column=1, padx=5, pady=5, sticky="ew")


    def delete_layout(self,sidebar_button_5):
        try:
            self.delet_all()
        except:
            pass
        conn = sqlite3.connect('customer.db')
        c = conn.cursor()
        self.pm=sidebar_button_5
        c.execute("SELECT * FROM customer WHERE firstname=?", (self.pm,))
        rows = c.fetchall()
        conn.commit()
        conn.close()
        self.frm=customtkinter.CTkFrame(self)
        self.frm.grid(row=0,column=1)
        self.label_firstname = customtkinter.CTkLabel(self.frm, text=f"Set Name: {rows[0][0]}")
        self.label_firstname.grid(row=0, column=1, padx=5, pady=0)
        self.label_lastname = customtkinter.CTkLabel(self.frm, text=f"Decimal: {rows[0][1]}")
        self.label_lastname.grid(row=0, column=3, padx=5, pady=0, sticky="ew")
        self.label_email = customtkinter.CTkLabel(self.frm, text=f"Digite Group: {rows[0][2]}")
        self.label_email.grid(row=0, column=2, padx=5, pady=0, sticky="ew")
        self.label_amount = customtkinter.CTkLabel(self.frm, text=f"Time: {rows[0][3]}")
        self.label_amount.grid(row=1, column=1, padx=5, pady=0, sticky="ew")

        self.button_search = customtkinter.CTkButton(self.frm, text="Delete", command=self.delete)
        self.button_search.grid(row=3, column=1, padx=20, pady=10)

    def delete(self):
        conn=sqlite3.connect("customer.db")
        c=conn.cursor()
        c.execute("DELETE FROM customer WHERE firstname=?",(self.pm,))
        conn.commit()
        conn.close()
        self.delet_all()
        self.frm=customtkinter.CTkFrame(self)
        self.frm.grid(row=0,column=1)
        self.label_firstname = customtkinter.CTkLabel(self.frm, text=f"Set Deleted")
        self.label_firstname.grid(row=0, column=1, padx=5, pady=0)
        
        
        print(self.pm)
        print("Fuck you!!!!!!!!")






    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)
    def delet_all(self):
        try:
            self.label_bticoin.grid_remove()
        except:
            pass
        try:
            self.entry_bticoin.grid_remove()
        except:
            pass
        try:
            self.frm2.grid_remove()
        except:
            pass
        try:
            self.fr.grid_remove()
        except:
            pass
        try:
            self.label_firstname2.grid_remove()
        except:
            pass

        try:
            self.label_firstname1.grid_remove()
        except:
            pass
        try:
            self.tabview.grid_remove()
        except:
            pass
        try:
            self.textbox.grid_remove()
        except:
            pass
        try:

            self.label_fr.grid_remove()
        except:
            pass
        
        try:
            self.scrollable_frame.grid_remove()
        except:
            pass
        try:
            self.radiobutton_frame.grid_remove()
        except:
            pass
        try:
            self.button_show_table.grid_remove()
        except:
            pass
        try:
            self.frm1.grid_remove()
        except:
            pass
        try:
            self.button_update.grid_remove()
        except:
            pass
        try:
            self.button_show_table.grid_remove()
        except:
            pass
        try:
            self.button_search.grid_remove()
        except:
            pass        
        try:
            self.label_firstname.grid_remove()
        except:
            pass            
        try:
            self.entry_firstname.grid_remove()
        except:
            pass            
        try:
            self.label_lastname.grid_remove()
        except:
            pass
        try:
            self.entry_lastname.grid_remove()
        except:
            pass
        try:
            self.label_email.grid_remove()
        except:
            pass
        try:
            self.entry_email.grid_remove()
        except:
            pass
        try:
            self.label_currency.grid_remove()
        except:
            pass
        try:
            self.entry_currency .grid_remove()
        except:
            pass
        try:
            self.entry_amount.grid_remove()
        except:
            pass
        try:
            self.label_amount.grid_remove()
        except:
            pass
        try:
            self.label_date.grid_remove()
        except:
            pass
        try:
            self.entry_date.grid_remove()

        except:
            pass
        try:
            self.frm.grid_remove()
        except:
            pass













if __name__ == "__main__":
    app = App()
    
    app.mainloop()
