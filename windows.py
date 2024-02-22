from customtkinter import *
import tkinter
from PIL import Image
import os

app = CTk(fg_color="#252526")
app.iconbitmap("monument_tool_construction_landmark_development_architecture_software_icon_261675.ico")
app.geometry("1000x600")
set_window_scaling(1.0)
set_widget_scaling(1.0)
app.title("App Project")

mode = "dark"

# functions for dark/light mode
def change_appearance_mode():
    global mode
    if mode == "dark":
        mode = "light"
        frame.configure(bg_color="#ffffff", fg_color = "#d2d3db")
        frame1.configure(bg_color="#ffffff", fg_color = "#d2d3db")
        frame2.configure(bg_color="#ffffff", fg_color = "#ffffff")
        appearance_switch.configure(button_color = "#1e1e1e", button_hover_color = "#252526")
        option_menu.configure(fg_color = "#d2d3db", hover = True, button_color = "#d2d3db", button_hover_color = "#d2d3db",
            text_color = "black")
        option_menu1.configure(fg_color = "#d2d3db", hover = True, button_color = "#d2d3db", button_hover_color = "#d2d3db",
            text_color = "black")
        data_label.configure(text_color = "#8E00A7")
        data_label1.configure(bg_color = "#ffffff", fg_color = "#ffffff", text_color = "#8E00A7")
        entry1.configure(fg_color = "#d2d3db")
        data_label2.configure(bg_color = "#ffffff", fg_color = "#ffffff", text_color = "#8E00A7")
        entry2.configure(fg_color = "#d2d3db")
        data_label3.configure(bg_color = "#ffffff", fg_color = "#ffffff", text_color = "#8E00A7")
        entry3.configure(fg_color = "#d2d3db")
        data_label4.configure(bg_color = "#ffffff", fg_color = "#ffffff", text_color = "#8E00A7")
        entry4.configure(fg_color = "#d2d3db")
        button_entry.configure(fg_color = "#d2d3db", hover_color = "#FFCD00", text_color = "#8E00A7")
        option_log.configure(fg_color = "#d2d3db", hover_color = "#ffffff", text_color = "black")
        app.configure(fg_color="#ffffff")
    else:
        mode = "dark"
        frame.configure(bg_color="#252526", fg_color = "#1e1e1e")
        frame1.configure(bg_color="#252526", fg_color = "#1e1e1e")
        frame2.configure(bg_color="#252526", fg_color = "#252526")
        appearance_switch.configure(button_color = "#d2d3db", button_hover_color = "#ffffff")
        option_menu.configure(fg_color = "#1e1e1e", hover = True, button_color = "#1e1e1e", button_hover_color = "#1e1e1e",
            text_color = "white")
        option_menu1.configure(fg_color = "#1e1e1e", hover = True, button_color = "#1e1e1e", button_hover_color = "#1e1e1e",
            text_color = "white")
        data_label.configure(text_color = "white")
        data_label1.configure(fg_color = "#252526", text_color = "white")
        entry1.configure(fg_color = "#484848")
        data_label2.configure(fg_color = "#252526", text_color = "white")
        entry2.configure(fg_color = "#484848")
        data_label3.configure(fg_color = "#252526", text_color = "white")
        entry3.configure(fg_color = "#484848")
        data_label4.configure(fg_color = "#252526", text_color = "white")
        entry4.configure(fg_color = "#484848")
        button_entry.configure(fg_color = "#1e1e1e", hover_color = "#FFCD00", text_color = "white")
        option_log.configure(fg_color = "#1e1e1e", hover_color = "#252526", text_color = "white")
        app.configure(fg_color="#252526")

# frames in the window
frame = CTkFrame(master = app,
                 width=1000,
                 height=21,
                 corner_radius = 0,
                 bg_color = "#252526",
                 fg_color="#1e1e1e")  
frame.place(x = 0, y = 0)

frame1 = CTkFrame(master = app,
                 width=500,
                 height=579,
                 corner_radius = 0,
                 bg_color = "#252526",
                 fg_color="#1e1e1e")  
frame1.place(x = 0, y = 21)

frame2 = CTkFrame(master = app,
                 width=500,
                 height=579,
                 corner_radius = 50,
                 bg_color = "#252526",
                 fg_color="#252526")  
frame2.place(x = 500, y = 21) 

# frame1 options
image_frame = CTkImage(light_image = Image.open('side-img.png'),
    size = (510,579))
image_label = CTkLabel(frame1, text = "", image = image_frame)
image_label.place(relx = 0.5, rely = 0.5, anchor = tkinter.CENTER)

# frame2 options
text_entry1 = ""
text_entry2 = ""
text_entry3 = ""
text_entry4 = ""

def calculate():
    text_entry1 = entry1.get()
    text_entry2 = entry2.get()
    text_entry3 = entry3.get()
    text_entry4 = entry4.get()

    f = open("Data", "a")
    f.write(text_entry1 + "\n" + text_entry2 + "\n" + text_entry3 + "\n" + text_entry4)
    f.close()

    Results = "An algorithm that calculates something based on the given data(reads data from the <<Data>> file)"
    f = open("Results", "a")
    f.write(Results)
    f.close()

    results_app = CTkToplevel(app)
    results_app.title("Results")
    results_app.geometry("400x200")
    text_label = CTkLabel(results_app, text = "The results are:", font=('Times New Roman', 20, 'bold'))
    text_label.place(relx = 0.5, rely = 0.05, anchor = tkinter.CENTER)
    
data_label = CTkLabel(frame2, text = "Insert your data", font = ('Times New Roman', 25, 'bold'), text_color = "white")
data_label.place(relx = 0.5, rely = 0.3, anchor = tkinter.CENTER)

data_label1 = CTkLabel(frame2, text = "Data1:", font = ('Times New Roman', 15, 'bold'), text_color = "white")
data_label1.place(relx = 0.19, rely = 0.375, anchor = tkinter.CENTER)
entry1 = CTkEntry(frame2, width = 250, state = "disabled", fg_color = "#484848")
entry1.place(relx = 0.5, rely = 0.375, anchor = tkinter.CENTER)

data_label2 = CTkLabel(frame2, text = "Data2:", font = ('Times New Roman', 15, 'bold'), text_color = "white")
data_label2.place(relx = 0.19, rely = 0.45, anchor = tkinter.CENTER)
entry2 = CTkEntry(frame2, width = 250, state = "disabled", fg_color = "#484848")
entry2.place(relx = 0.5, rely = 0.45, anchor = tkinter.CENTER)

data_label3 = CTkLabel(frame2, text = "Data3:", font = ('Times New Roman', 15, 'bold'), text_color = "white")
data_label3.place(relx = 0.19, rely = 0.525, anchor = tkinter.CENTER)
entry3 = CTkEntry(frame2, width = 250, state = "disabled", fg_color = "#484848")
entry3.place(relx = 0.5, rely = 0.525, anchor = tkinter.CENTER)

data_label4 = CTkLabel(frame2, text = "Data4:", font = ('Times New Roman', 15, 'bold'), text_color = "white")
data_label4.place(relx = 0.19, rely = 0.6, anchor = tkinter.CENTER)
entry4 = CTkEntry(frame2, width = 250, state = "disabled", fg_color = "#484848")
entry4.place(relx = 0.5, rely = 0.6, anchor = tkinter.CENTER)


button_entry = CTkButton(frame2, text = "Calculate", fg_color = "#1e1e1e", width = 250, hover_color = "#FFCD00", corner_radius = 10, command = calculate, state = "disabled")
button_entry.place(relx = 0.5, rely = 0.7, anchor = tkinter.CENTER)


# option menu functions
def function_menu(choise):

    def send():
        text_for_us = text_us.get(0.0, 'end')
        f = open("Messages", "a")
        f.write(text_for_us)
        f.close()
    
    def delete():
        text_us.delete(0.0, 'end')

    send_message_app = CTkToplevel(app)
    send_message_app.title("Send us a message")
    send_message_app.geometry("600x400")

    frame = CTkFrame(master = send_message_app,
                 width=600,
                 height=400)
    frame.place(x = 0, y = 0)

    text_label = CTkLabel(frame, text = "We would like to know your opinion!", font=('Times New Roman', 15, 'bold'))
    text_label.place(relx = 0.5, rely = 0.05, anchor = tkinter.CENTER)

    text_us = CTkTextbox(frame, width = 400, height = 300)
    text_us.place(relx = 0.1725, rely = 0.1)

    send_button = CTkButton(frame, text = "Send", fg_color = "#1e1e1e", command = send)
    send_button.place(relx = 0.7, rely = 0.9, anchor = tkinter.CENTER)

    delete_button = CTkButton(frame, text = "Delete", fg_color = "#1e1e1e", command = delete)
    delete_button.place(relx = 0.3, rely = 0.9, anchor = tkinter.CENTER)

def function_menu1(choise):
    if choise == "About us":
        about_us_app = CTkToplevel(app)
        about_us_app.title("About us")
        about_us_app.geometry("400x200")
        text_label = CTkLabel(about_us_app, text = "Insert text", font=('Times New Roman', 15, 'bold'))
        text_label.place(relx = 0.5, rely = 0.05, anchor = tkinter.CENTER)
    else:
        about_project_app = CTkToplevel(app)
        about_project_app.title("About us")
        about_project_app.geometry("400x200")
        text_label = CTkLabel(about_project_app, text = "Insert text", font=('Times New Roman', 15, 'bold'))
        text_label.place(relx = 0.5, rely = 0.05, anchor = tkinter.CENTER)

#option menu
options_for_menu = ["Send a message"]
option_menu = CTkOptionMenu(frame, values = options_for_menu, command = function_menu,
    fg_color = "#1e1e1e",
    hover = True,
    button_color = "#1e1e1e",
    button_hover_color = "#1e1e1e",
    text_color = "white")
option_menu.place(relx = 0.068, rely = 0.5, anchor = tkinter.CENTER)

options_for_menu1 = ["About us", "About the project"]
option_menu1 = CTkOptionMenu(frame, values = options_for_menu1, command = function_menu1,
    fg_color = "#1e1e1e",
    hover = True,
    button_color = "#1e1e1e",
    button_hover_color = "#1e1e1e",
    text_color = "white")
option_menu1.place(relx = 0.20, rely = 0.5, anchor = tkinter.CENTER)


Username = "parola"
Password = "parola"
def login():
    login_app = CTkToplevel(app)
    login_app.title("Login for access")
    login_app.geometry("400x200")
    frame = CTkFrame(master = login_app,
                 width=400,
                 height=200)
    frame.place(x = 0, y = 0)

    def logged():
        global Username
        global Password
        username = username_entry.get()
        password = password_entry.get()
        if username == Username and password == Password:
            entry1.configure(state = "normal")
            entry2.configure(state = "normal")
            entry3.configure(state = "normal")
            entry4.configure(state = "normal")
            button_entry.configure(state = "normal")
            login_app.destroy()
            login_app.update()
            option_log.configure(text = "Logged")
        else:
            username_entry.configure(placeholder_text = "Unknown user or bad password", placeholder_text_color = "red")
            password_entry.configure(placeholder_text = "Unknown user or bad password", placeholder_text_color = "red")
            username_entry.delete(0, 'end')
            password_entry.delete(0, 'end')


    login_label1 = CTkLabel(frame, text = "Username:", font = ('Times New Roman', 15, 'bold'), text_color = "white")
    login_label1.place(relx = 0.35, rely = 0.175, anchor = tkinter.CENTER)
    username_entry = CTkEntry(frame, width = 200, fg_color = "#484848")
    username_entry.place(relx = 0.5, rely = 0.3, anchor = tkinter.CENTER)

    login_label2 = CTkLabel(frame, text = "Password:", font = ('Times New Roman', 15, 'bold'), text_color = "white")
    login_label2.place(relx = 0.35, rely = 0.475, anchor = tkinter.CENTER)
    password_entry = CTkEntry(frame, width = 200, fg_color = "#484848")
    password_entry.place(relx = 0.5, rely = 0.6, anchor = tkinter.CENTER)

    login = CTkButton(frame, text = "Login", width = 100, fg_color = "#1e1e1e", hover_color = "#252526", text_color = "white", command = logged)
    login.place(relx = 0.5, rely = 0.8, anchor = tkinter.CENTER)


option_log = CTkButton(frame, text = "Log in", width = 30, fg_color = "#1e1e1e", hover_color = "#252526", text_color = "white", command = login)
option_log.place(relx = 0.92, rely = 0.5, anchor = tkinter.CENTER)

# switch for the dark/light mode
switch_var = StringVar(value = "on")
appearance_switch = CTkSwitch(frame, text = "", command = change_appearance_mode, 
    variable = switch_var, onvalue = "on", offvalue = "off", progress_color = "#252526")
appearance_switch.place(relx = 1, rely = 0.5, anchor = tkinter.CENTER)

app.mainloop()

if os.path.exists("Data"):
    os.remove("Data")
if os.path.exists("Messages"):
    os.remove("Messages")
if os.path.exists("Results"):
    os.remove("Results")