from tkinter import *
from tkinter import ttk
from tkinter import messagebox


root = Tk()
root.title('Inder Currency Converter')
#root.iconbitmap('Logo_2.ico')
root.geometry('500x500')



# Create Tabs
my_notebook =   ttk.Notebook(root)
my_notebook.pack(padx=5)



#create frmae
currency_frame = Frame(my_notebook, width=460, height=460)
conversion_frame = Frame(my_notebook, width=460, height=460)

currency_frame.pack(fill='both', expand=1)
conversion_frame.pack(fill='both', expand=1)

# add our tabs
my_notebook.add(currency_frame, text='Currency')
my_notebook.add(conversion_frame, text='Convert')


#Disable tabs
my_notebook.tab(1, state = 'disabled')


#########################
# CURRENCY STUFF
# #######################
def lock():
    if not home_entry.get() or not conversion_entery.get() or not rate_entery.get():
        messagebox.showwarning('WARNING', "You Didn't fill the all fildes")
    else:
        # Disable entery boxes
        home_entry.config(state='disabled')
        conversion_entery.config(state='disabled')
        rate_entery.config(state='disabled')
        
        # Enable entery boxes
        my_notebook.tab(1, state = 'normal')
        # Change Tab Field
        amount_lable.config(text=f'Amount of {home_entry.get()}To Convert To {conversion_entery.get()}')
        converted_lable.config(text=f'Equals This Many {conversion_entery.get()}')
        convert_button.config(text=f'Convert From {home_entry.get()}')

def unlock():
    # Enable entery boxes
        home_entry.config(state='normal')
        conversion_entery.config(state='normal')
        rate_entery.config(state='normal')
        
    # Disable entery boxes
        my_notebook.tab(1, state = 'disabled')
        


# currency stuff
home = LabelFrame(currency_frame, text='Your Home Currency')
home.pack(pady=20)

#Entery box
home_entry = Entry(home, font=('Helvetica',24))
home_entry.pack(pady=10, padx=10)


#Conversion Currency Frame
conversion = LabelFrame(currency_frame, text='Coversion currency')
conversion.pack(pady=20)

#Convert to lable
conversion_lable = Label(conversion, text='Currency To convert to....')
conversion_lable.pack(pady=10)

#Convert to Entery

conversion_entery = Entry(conversion,font=('Helvetica',24))
conversion_entery.pack(pady=10, padx=10)


#Rate to lable
rate_lable = Label(conversion, text='Current Conversion Rate...')
rate_lable.pack(pady=10)

#Rate to Entery

rate_entery = Entry(conversion,font=('Helvetica',24))
rate_entery.pack(pady=10, padx=10)



#button frame
button_frame = Frame(currency_frame)
button_frame.pack(pady=20)

# Create buttons

lock_button = Button(button_frame, text='Lock', command=lock)
lock_button.grid(row=0, column=0, padx=10)


unlock_button = Button(button_frame, text='Unlock', command=unlock)
unlock_button.grid(row=0, column=1, padx=10)





#########################
# Cnvesion STUFF
# #######################

def convert():
    # Clear Converted Entery Box
    converted_entery.delete(0, END)
    
    # Convert 
    conversion = float(rate_entery.get()) * float(amount_entery.get())
    
    # Convert to two Decimals
    conversion = round(conversion, 2)
    # add commas
    conversion = '{:,}'.format(conversion)
    
    #Upadate entery box
    converted_entery.insert(0, conversion)



def clear():
    amount_entery.delete(0, END)
    converted_entery.delete(0, END)


amount_lable = LabelFrame(conversion_frame, text= 'Amount To Convert')
amount_lable.pack(pady=2)

#Entery Box
amount_entery = Entry(amount_lable, font=('Helvetica',24))
amount_entery.pack(padx=10, pady=10)

#Convert button
convert_button = Button(amount_lable, text='Convert', command=convert)
convert_button.pack(pady=20)



#Equals Frame

converted_lable = LabelFrame(conversion_frame, text='Converted Currency')
converted_lable.pack(pady=20)

# Converted Entery
converted_entery = Entry(converted_lable, font=('Helvetica',24), bd=0, bg='systembuttonface' )
converted_entery.pack(pady=10, padx=10)

#Clear Button
clear_button = Button(conversion_frame, text='Clear', command=clear)
clear_button.pack(pady=20)


# Fake Lable for spacing
spacer = Label(conversion_frame, text='', width=68)
spacer.pack()









 









root.mainloop()
