import tkinter
root=tkinter.Tk()
tkinter.Label(root,text="PYTHON REGISTARTION FORM",background='#00ffd9').place(x=170,y=10)

root.geometry('500x500')
root.title("Registration form")
root.config(background='#fe93c6')



name_label=tkinter.Label(root,text="Enter Name",background='#00ffd9')
name_label.pack(pady=50, padx=50)
name_textbox=tkinter.Entry(root)
name_textbox.pack(pady=10, padx=30)#pack is used for closing

age_label=tkinter.Label(root,text="Enter age",background='#00ffd9')
age_label.pack(pady=10, padx=50)
age_textbox=tkinter.Entry(root)
age_textbox.pack(pady=10, padx=50)

email_label=tkinter.Label(root,text="Enter Email",background='#00ffd9')
email_label.pack(pady=10, padx=50)
email_textbox=tkinter.Entry(root)
email_textbox.pack(pady=10, padx=50)

phone_label=tkinter.Label(root,text="Enter Phone number",background='#00ffd9')
phone_label.pack(pady=10, padx=50)
phone_textbox=tkinter.Entry(root)
phone_textbox.pack(pady=10, padx=50)

submit_button=tkinter.Button(root,text='Submit',background='#00ffd9')
submit_button.pack(pady=10, padx=50
                   )

root.mainloop()