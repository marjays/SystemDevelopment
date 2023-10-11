import customtkinter as ct                  #pip install customtkinter
from PIL import Image, ImageTk              #pip install pillow
import tkinter as tk 
from tkinter import DISABLED, Toplevel, messagebox
from CTkMessagebox import CTkMessagebox     #pip install ctkmessagebox  #https://pypi.org/project/CTkMessagebox/
from validate_email import validate_email   #pip install validate_email     
                                            #pip install py3dns
import ssl
import smtplib
from email.message import EmailMessage
import random
import string


########ADDED A COMMENT THERE, FOR TRIAL

path = "files/"       
icon_path = path+'logo.ico'
valid_path = path+'valid.png'
invalid_path = path+'warning.png'

mon_font_regular = font=("Montserrat", 12)
mon_font_bold = font=("Montserrat", 12, "bold")
rob_font_regular = font=("Roboto", 12)
rob_font_bold = font=("Roboto", 12, "bold")
appearance = "light"
if appearance == "light":
    bg_color = "#ebebeb"
    fg_color = "#161616"
    fg_color2 = "#161616"
    show_hide_color = "#f9f9fa"
    show_path = path+'show_b.png'
    hide_path = path+'hide_b.png'
else:
    bg_color = "#242424"
    fg_color = "#00ff06"
    fg_color2 = "#b7b9be"
    show_hide_color = "#343638"
    show_path = path+'show.png'
    hide_path = path+'hide.png'
    
#TEMPORARILY SET AS STATIC
email_sender = "notif.icaresys@gmail.com"
email_password = "azdh vrfc mqks lnmy"

class Login:
    def __init__(self, root):  
        ct.set_appearance_mode(appearance) #dark, system, light
        ct.set_default_color_theme("dark-blue")
        self.root = root
        self.root.title("iCareSys Login")
        # Calculate the center position
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        window_width = 350
        window_height = 210
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        #Set the window geometry to center it
        self.root.geometry(f"{window_width}x{window_height}+{x}+{y}")
        self.root.resizable(False, False)
        #self.root.overrideredirect(1) 
        #self.root.configure(bg="#f0f0f0")
        
        #THE WINDOW ICON
        self.root.iconbitmap(icon_path)
        
        #THE SHOW AND HIDE ICON
        self.show_image = Image.open(show_path)
        self.show_image = self.show_image.resize((15, 15))
        self.show_image = ImageTk.PhotoImage(self.show_image)
        
        self.hide_image = Image.open(hide_path)
        self.hide_image = self.hide_image.resize((15, 15))
        self.hide_image = ImageTk.PhotoImage(self.hide_image)
        
        #THE TASKBAR ICON - need as reference
        #logo_path = "logo.png"
        #logo_image = Image.open(logo_path)
        #logo_image = ImageTk.PhotoImage(logo_image)
        #self.root.iconphoto(True, logo_image)
        
        #DESIGNING
        self.login_frame = ct.CTkFrame(master=self.root)
        self.login_frame.pack(pady=50, padx=10, fill="both", expand=True)
        
        
       # setup_button = ct.CTkButton(master=self.root, font=mon_font_regular, 
       #                             text="Account setup", command=self.setup)
       # setup_button.place(x=250, y=10)
        
        setup_button = tk.Button(self.root, font=("Montserrat", 10), fg=fg_color, bg=bg_color,
                                 text="Account setup", activebackground=bg_color, bd=0, 
                                 highlightthickness=0, activeforeground="gray", 
                                 command=self.setup)
        setup_button.place(x=240, y=13)
        
        username_entry = ct.CTkEntry(master=self.login_frame, font=("Montserrat", 13), 
                                     placeholder_text="Username", width=300, height=30)
        username_entry.pack(pady=15, padx=5)
        
        self.password_entry = ct.CTkEntry(master=self.login_frame, font=("Montserrat", 13), show="*",
                                     placeholder_text="Password", width=300, height=30)
        self.password_entry.pack(pady=0, padx=5)
        
        self.show_button = tk.Button(self.login_frame, image=self.show_image, bg=show_hide_color, 
                                highlightthickness=0, bd=0, activebackground=show_hide_color,
                                cursor="hand2", command=self.show)
        self.show_button.place(x=288, y=68, width=20, height=18)
        
        forgotpass_button = tk.Button(self.root, font=("Montserrat", 10), fg=fg_color2, bg=bg_color,
                                 text="Forgot password?", activebackground=bg_color, bd=0, 
                                 highlightthickness=0, activeforeground="gray", 
                                 command=self.forgotpass)
        forgotpass_button.place(x=10, y=170)
        
        login_button = ct.CTkButton(master=self.root, font=mon_font_bold, text="Login", 
                                    command=self.login)
        login_button.place(x=200, y=170)
        
        self.root.bind("<Return>", self.login)
    
    #ACTIONS  
    def show(self):
        self.hide_button = tk.Button(self.login_frame, image=self.hide_image, bg=show_hide_color, 
                                highlightthickness=0, bd=0, activebackground=show_hide_color,
                                cursor="hand2", command=self.hide)
        self.hide_button.place(x=288, y=68, width=20, height=18)
        self.password_entry.configure(show="")
    
    def hide(self):
        self.show_button = tk.Button(self.login_frame, image=self.show_image, bg=show_hide_color, 
                                highlightthickness=0, bd=0, activebackground=show_hide_color,
                                cursor="hand2", command=self.show)
        self.show_button.place(x=288, y=68, width=20, height=18)
        self.password_entry.configure(show="*")
    
    def setup(self):
        self.root.destroy()
        setup_root = ct.CTk()
        setup_obj = Setup(setup_root)
        setup_root.mainloop()
        
    def login(self, event=None):
        print("login...")
        
    def forgotpass(self):
        print("forgot password...")
        
class Setup:
    def __init__(self, root):
        ct.set_appearance_mode(appearance) #dark, system, light
        ct.set_default_color_theme("dark-blue")
        self.root = root
        self.root.title("iCareSys Account Setup")
        # Calculate the center position
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        window_width = 350
        window_height = 400
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        #Set the window geometry to center it
        self.root.geometry(f"{window_width}x{window_height}+{x}+{y}")
        self.root.resizable(False, False)
        
        #THE WINDOW ICON
        self.root.iconbitmap(icon_path)
        
        #THE SHOW AND HIDE ICON
        self.show_image = Image.open(show_path)
        self.show_image = self.show_image.resize((15, 15))
        self.show_image = ImageTk.PhotoImage(self.show_image)
        
        self.hide_image = Image.open(hide_path)
        self.hide_image = self.hide_image.resize((15, 15))
        self.hide_image = ImageTk.PhotoImage(self.hide_image)
        
        self.valid_image = Image.open(valid_path)
        self.valid_image = self.valid_image.resize((15, 15))
        self.valid_image = ImageTk.PhotoImage(self.valid_image)
        
        self.warning_image = Image.open(invalid_path)
        self.warning_image = self.warning_image.resize((15, 15))
        self.warning_image = ImageTk.PhotoImage(self.warning_image)
        
        self.setup_frame = ct.CTkFrame(master=self.root)
        self.setup_frame.pack(pady=50, padx=10, fill="both", expand=True)
        
        header_label = ct.CTkLabel(master=self.root, font=("Montserrat", 16, "bold"), 
                                   text="Admin Account Setup", text_color=fg_color)
        header_label.place(x=85, y=10)
        
        self.f_name_entry = ct.CTkEntry(master=self.setup_frame, font=("Montserrat", 13), 
                                     placeholder_text="First Name", width=300, height=30)
        self.f_name_entry.pack(pady=10, padx=5)
        
        self.l_name_entry = ct.CTkEntry(master=self.setup_frame, font=("Montserrat", 13), 
                                     placeholder_text="Last Name", width=300, height=30)
        self.l_name_entry.pack(pady=10, padx=5)
        
        self.email_entry = ct.CTkEntry(master=self.setup_frame, font=("Montserrat", 13),
                                  placeholder_text="Email", width=300, height=30)
        self.email_entry.pack(pady=10, padx=5)
        
        self.email_entry.bind("<Return>", self.validating_email)
        self.email_entry.bind("<Tab>", self.validating_email)
        self.email_entry.bind("<FocusOut>", self.validating_email)
        
        self.otp_label = ct.CTkLabel(master=self.setup_frame, font=("Montserrat", 16, "bold"), 
                                   text="OTP", text_color=fg_color)
        self.otp_label.place(x=17, y=162)
        
        #self.otp_entry = ct.CTkEntry(master=self.setup_frame, font=("Montserrat", 13),
        #                          width=150, height=30, validate="key", validatecommand=(self.root.register(self.limit_otp), "%P"))
        self.otp_entry = ct.CTkEntry(master=self.setup_frame, font=("Montserrat", 13), width=150, height=30)
        self.otp_entry.pack(pady=10, padx=60, anchor='w')
        
        self.resend_button = ct.CTkButton(master=self.setup_frame, font=mon_font_bold, text="Resend", 
                                    width=30, command=self.resend)
        #self.resend_button.place(x=220, y=160)
        self.resend_button.place_forget()
        
        self.username_entry = ct.CTkEntry(master=self.setup_frame, font=("Montserrat", 13),
                                     placeholder_text="Username", width=300, height=30)
        self.username_entry.pack(pady=10, padx=5)
        
        self.password_entry = ct.CTkEntry(master=self.setup_frame, font=("Montserrat", 13), show="*",
                                     placeholder_text="Password", width=300, height=30)
        self.password_entry.pack(pady=10,               padx=5)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
        self.confirm_password_entry = ct.CTkEntry(master=self.setup_frame, font=("Montserrat", 13), show="*",
                                     placeholder_text="Confirm Password", width=300, height=30)
        self.confirm_password_entry.pack(pady=10, padx=5)
        
        #need to readjust 
        #self.hide()
        
        self.submit_button = ct.CTkButton(master=self.root, font=mon_font_bold, text="Submit", 
                                    width=300, command=self.submit)
        self.submit_button.place(x=25, y=360)
        self.submit_button.configure(state=DISABLED)
        
        #self.root.bind("<Return>", self.submit)
        
    #this will limit the entry into 6 digit - but i can't use this for now because of CTk limited features when used
    def limit_otp(self, new_value):
        return new_value.isdigit() and len(new_value) <= 6
    
    def send_otp(self):
        def generate_otp():
            #"0123456789"
            otp = "".join(random.choices(string.digits, k=6))
            return otp
        
        self.otp_value = generate_otp()
        email_receiver = self.email_entry.get()
        ##########BELOW IS CRUCIAL FOR OTP-SENDING
       # em = EmailMessage()
       # em['From'] = email_sender
       # em['To'] = email_receiver
       # em['Subject'] = "One-Time-PIN notification"
       # em.set_content("Your OTP is " + self.otp_value)

       # context = ssl.create_default_context()

       # with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
       #     smtp.starttls(context=context)
       #     smtp.login(email_sender, email_password)
       #     smtp.send_message(em)
        #############################################
        
        print(self.otp_value)
        self.resend_button.place(x=220, y=160)
        self.otp_entry.bind("<Return>", self.validate_otp)
        self.otp_entry.bind("<Tab>", self.validate_otp)
        self.otp_entry.bind("<FocusOut>", self.validate_otp)
    
    def resend(self):
        self.otp_entry.unbind("<Return>")
        self.otp_entry.unbind("<Tab>")
        self.otp_entry.unbind("<FocusOut>")
        self.otp_entry.delete(0, "end")
        self.send_otp()
          
    def validate_otp(self, event=None):
        if self.otp_entry.get() == self.otp_value:
            self.otp_entry.unbind("<Return>")
            self.otp_entry.unbind("<Tab>")
            self.otp_entry.unbind("<FocusOut>")
            self.valid_label = tk.Label(self.setup_frame, image=self.valid_image, bg=show_hide_color)
            self.valid_label.place(x=290, y=115)
            self.otp_label.place_forget()
            self.otp_entry.pack_forget()
            self.resend_button.place_forget()
            self.email_entry.configure(state=DISABLED)
            self.hide()
            self.root.bind("<Return>", self.submit)
            
        else:
            #need to put wrong otp image in the otp entry
            print("incorrect otp")
        
    def validating_email(self, event=None):
        is_valid = validate_email(self.email_entry.get(), verify=False)
        if is_valid:
            if self.email_entry.get() != "":
                self.email_entry.unbind("<Return>")
                self.email_entry.unbind("<Tab>")
                self.email_entry.unbind("<FocusOut>")
                self.verify_popup = Toplevel(self.root)
                self.verify_popup.title("Verify Email")
                screen_width = self.verify_popup.winfo_screenwidth()
                screen_height = self.verify_popup.winfo_screenheight()
                window_width = 250
                window_height = 80
                x = (screen_width - window_width) // 2
                y = (screen_height - window_height) // 2
                #Set the window geometry to center it
                self.verify_popup.geometry(f"{window_width}x{window_height}+{x}+{y}")
                self.verify_popup.resizable(False, False)
        
                self.verify_popup.iconbitmap(icon_path)
        
                mini_frame = ct.CTkFrame(master=self.verify_popup, bg_color=bg_color)
                mini_frame.pack(pady=0, padx=0, fill="both", expand=True)
    
                otp_notif_label = ct.CTkLabel(master=mini_frame, text="We have sent a 6-digit PIN to your email."
                                      + " Please check your inbox or spam message.", wraplength=220, 
                                      font=("Montserrat", 13))
                otp_notif_label.pack(pady=15, anchor='center')
                
                self.verify_popup.protocol("WM_DELETE_WINDOW", self.on_closing)
        
        else:
            self.warning_label = tk.Label(self.setup_frame, image=self.warning_image, bg=show_hide_color)
            self.warning_label.place(x=290, y=115)
    
    def on_closing(self):
        self.verify_popup.destroy()
        self.send_otp()
               
    def show(self):
        self.hide_button = tk.Button(self.setup_frame, image=self.hide_image, bg=show_hide_color, 
                                highlightthickness=0, bd=0, activebackground=show_hide_color,
                                cursor="hand2", command=self.hide)
        self.hide_button.place(x=288, y=217, width=20, height=18)
        self.password_entry.configure(show="")
        self.confirm_password_entry.configure(show="")
    
    def hide(self):
        self.show_button = tk.Button(self.setup_frame, image=self.show_image, bg=show_hide_color, 
                                highlightthickness=0, bd=0, activebackground=show_hide_color,
                                cursor="hand2", command=self.show)
        self.show_button.place(x=288, y=217, width=20, height=18)
        self.password_entry.configure(show="*")
        self.confirm_password_entry.configure(show="*")
    
    def submit(self, event=None):
        first_name = self.f_name_entry.get()
        last_name = self.l_name_entry.get()
        email = self.email_entry.get()
        username = self.username_entry.get()
        password = self.password_entry.get()
        confirm_password = self.confirm_password_entry.get()
        
        if first_name != "" and last_name != "" and email != "" and username != "" and password != "" and confirm_password != "":
            if password == confirm_password:
                print("processed...")
        else:
            print("all fields required!")


class Forgot:
    def __init__(self, root):
        ct.set_appearance_mode(appearance) #dark, system, light
        ct.set_default_color_theme("dark-blue")
        self.root = root
        self.root.title("iCareSys Forgot password")
        # Calculate the center position
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        window_width = 400
        window_height = 200
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        #Set the window geometry to center it
        self.root.geometry(f"{window_width}x{window_height}+{x}+{y}")
        self.root.resizable(False, False)
        
        #THE WINDOW ICON
        self.root.iconbitmap(icon_path)
        

if __name__ == "__main__":
    root = ct.CTk()
    obj = Login(root)
    root.mainloop()