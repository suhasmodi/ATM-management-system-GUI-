from tkinter import *
import customtkinter
from tkinter import messagebox
import time
import os
import datetime
import pytz
from reportlab.pdfgen import canvas


local_timezone = pytz.timezone('Asia/Kolkata')


def clear_terminal():
    # Clear the terminal screen based on the operating system
    os.system('cls' if os.name == 'nt' else 'clear')


username='admin'
password='admin123'

customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('dark-blue')
root=customtkinter.CTk(fg_color='darkblue')
root.title('atm')
root.geometry('500x400')



class ATM():
    balance1=0
    balance2=0
    user_acc_no1=123456789
    user_acc_no2=999988888
    transactions=[]



    def withdraw(self):
        global balance1
        global withd,amount_entry

        withd = Toplevel(root,bg='black')
        withd.title('Withdraw')
        withd.geometry('300x200')

        withd_msg =  customtkinter.CTkLabel(withd, text='Withdraw Money', font=('Times', 18))
        withd_msg.pack(pady=10)

        amount_label =  customtkinter.CTkLabel(withd, text='Enter Amount:',font=('Times', 18))
        amount_label.pack()

        amount_entry =  customtkinter.CTkEntry(withd, font=('Helvetica Font', 15),width=200)
        amount_entry.pack(pady=10)

        withd_button = Button(withd, text='Withdraw', font=('Times', 14),width=10,fg='darkblue',command=lambda: self.process_withdraw(amount_entry.get()))
        withd_button.pack()


    def process_withdraw(self, amount):
        local_time = datetime.datetime.now(local_timezone)
        date=local_time.strftime('%Y-%m-%d %H:%M:%S')
        time=local_timezone
        
        try:    
                amount=float(amount_entry.get())
                if amount<self.balance1:
                    self.balance1 = self.balance1 - amount
                    ATM.transactions.append(f'Debit: {amount} {date}')
                    messagebox.showinfo("Success", "Transaction Successful")
                else:
                     messagebox.showerror("Error", "Insuffecient Balance")
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter a valid number.")
        withd.destroy()
    
    def deposit(self):
        global balance1
        global Depo,amount_entry
        Depo = Toplevel(root,bg='black')
        Depo.title('Deposit')
        Depo.geometry('300x200')

        depo_msg =  customtkinter.CTkLabel(Depo, text='Deposit Money', font=('Times', 18))
        depo_msg.pack(pady=10)

        amount_label =  customtkinter.CTkLabel(Depo, text='Enter Amount:',font=('Times', 18))
        amount_label.pack()

        amount_entry =  customtkinter.CTkEntry(Depo, font=('Helvetica Font', 15),width=200)
        amount_entry.pack(pady=10)

        deposit_button = Button(Depo, text='Deposit', font=('Times', 14),fg='darkblue',width=10,command=lambda: self.process_deposit(amount_entry.get()))
        deposit_button.pack()

 
    def process_deposit(self, amount):
        local_time = datetime.datetime.now(local_timezone)
        date=local_time.strftime('%Y-%m-%d %H:%M:%S')
        time=local_timezone

        try:    
            amount=float(amount_entry.get())
            self.balance1+=amount
            ATM.transactions.append(f'Credit: {amount} {date}')

            messagebox.showinfo("Success", "Succefully Deposited Money")
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter a valid number.")
        Depo.destroy()

    def transfer(self):
        global balance1, balance2, user_acc_no1, user_acc_no2,TransferFrame

        TransferFrame = Toplevel(root, bg='black')
        TransferFrame.title('Transfer Money')
        TransferFrame.geometry('300x400')

        transfer_msg = Label(TransferFrame, text='Transfer Money', font=('Times', 18), bg='black', fg='white')
        transfer_msg.pack(pady=10)

        acc_no_label = Label(TransferFrame, text='Enter Receiver Account No:', font=('Times', 18), bg='black', fg='white')
        acc_no_label.pack()

        acc_no_entry = Entry(TransferFrame, font=('Helvetica Font', 15), width=200)
        acc_no_entry.pack(pady=10)

        amount_label = Label(TransferFrame, text='Enter Amount:', font=('Times', 18), bg='black', fg='white')
        amount_label.pack()

        amount_entry = Entry(TransferFrame, font=('Helvetica Font', 15), width=200)
        amount_entry.pack(pady=10)

        transfer_button = Button(TransferFrame, text='Transfer', font=('Times', 14),fg='darkblue', width=10,
                                 command=lambda: self.process_transfer(acc_no_entry.get(), amount_entry.get()))
        transfer_button.pack()


    def process_transfer(self, receiver_acc_no, amount):
        local_time = datetime.datetime.now()
        date = local_time.strftime('%Y-%m-%d %H:%M:%S')

        try:
            receiver_acc_no = int(receiver_acc_no)
            amount = float(amount)

            if receiver_acc_no == self.user_acc_no1:
                if amount > self.balance1:
                    messagebox.showerror("Error", "Insufficient Balance.")
                else:
                    self.balance1 -= amount
                    ATM.transactions.append(f'Transfer: {amount} to {receiver_acc_no} {date}')
                    messagebox.showinfo("Success", "Successfully Transferred Money")
            elif receiver_acc_no == self.user_acc_no2:
                if amount > self.balance2:
                    messagebox.showerror("Error", "Insufficient Balance.")
                else:
                    self.balance2 -= amount
                    ATM.transactions.append(f'Transfer: {amount} to {receiver_acc_no} {date}')
                    messagebox.showinfo("Success", "Successfully Transferred Money")
            else:
                messagebox.showerror("Error", "Receiver Account does not exist.")
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter valid account number and amount.")
        
        TransferFrame.destroy()

        
        

    def Balance_check(self):
        BalCheck= Toplevel(root,bg='black')
        BalCheck.title('Balance')
        BalCheck.geometry('300x200')

        amount_label =  customtkinter.CTkLabel(BalCheck, text=f'Balance:{self.balance1}',font=('Times', 18))
        amount_label.place(x=60,y=50)
    
    

    def transaction_history(self):
        global text_widget,content
        window =Tk()
        window.title("Print List in Tkinter")

        save_button =Button(window, text="Save to PDF",command=self.save_pdf)
        save_button.pack()

        text_widget = Text(window, height=50, width=60)
        text_widget.pack()

            
        text_widget.delete(1.0, END)
        for item in ATM.transactions:
            text_widget.insert(END, item + "\n")
        
        window.mainloop()
    def save_pdf(self):

        content = text_widget.get(1.0,END)

        content = content.strip()

        pdf_filename = "output.pdf"
        pdf_canvas = canvas.Canvas(pdf_filename)
        pdf_canvas.drawString(300, 830, "Transaction History")
        lines = content.split('\n')
        height=800

        lines = content.split('\n')

        height = 800

        # Draw each line on a new line in the PDF
        for line in lines:
            pdf_canvas.drawString(100, height, line)
            height -= 12  

        pdf_canvas.save()


        
             
    

a=ATM()

def validate():
    
    user_get=user_input.get()
    pwd_get=pwd_input.get()

    if user_get==username and pwd_get==password:
        messagebox.showinfo("Success", "Login Successful")
        show_main_frame()
    else:
        messagebox.showerror("Error", "Invalid username or password")

def show_main_frame():
   
    login_frame.place_forget()
    option_frame.grid()

def destroy():
    root.destroy()




login_frame = customtkinter.CTkFrame(root,width=500, height=400)

head= customtkinter.CTkLabel(login_frame,text='Welcome ATM Management System\n\nSign In',font=('Times',20))
head.place(x=120,y=50)

name= customtkinter.CTkLabel(login_frame,text='Username:',font=('Helvetica Font',18))
name.place(x=20,y=125)

user_input= customtkinter.CTkEntry(login_frame,font=('Helvetica Font',15),width=250)
user_input.place(x=150,y=125)

pwd =  customtkinter.CTkLabel(login_frame,text='Password:', font=('Times', 20))
pwd.place(x=20,y=190)

pwd_input= customtkinter.CTkEntry(login_frame,show='*',font=('Helvetica Font',15),width=250)
pwd_input.place(x=150,y=190)


submit=Button(login_frame,text='Submit',font=('Times', 20),fg='darkblue',command=validate)
submit.place(x=250,y=400)


#welcome  customtkinter.CTkFrame
welcome_frame = customtkinter.CTkFrame(root, width=500, height=400)

message_label =  customtkinter.CTkLabel(welcome_frame, text="Welcome", font=('Times', 14))
message_label.place(x=200, y=200)

login_frame.place(x=0, y=0)


Depo= customtkinter.CTkFrame(root, width=500, height=400)
depo_msg= customtkinter.CTkLabel(Depo,text='Desposit')
depo_msg.pack()

#OPTION  customtkinter.CTkFrame

option_frame= customtkinter.CTkFrame(root, width=500, height=400)

opt_msg= customtkinter.CTkLabel(option_frame,text='Select Option')

tr_hist=Button(option_frame,text='Transaction History',font=('Times', 16),width=15,fg='darkblue',command=a.transaction_history)
tr_hist.place(x=100,y=100)

Deposit=Button(option_frame,text='Deposit',font=('Times', 16),fg='darkblue',width=15,command=a.deposit)
Deposit.place(x=300,y=100)


Withd=Button(option_frame,text='Withdraw',font=('Times', 16),fg='darkblue',width=15,command=a.withdraw)
Withd.place(x=100,y=200)

trans=Button(option_frame,text='Transfer money',font=('Times', 16),fg='darkblue',width=15,command=a.transfer)
trans.place(x=300,y=200)

Bal=Button(option_frame,text='Balance',font=('Times', 16),fg='darkblue',width=15,command=a.Balance_check)
Bal.place(x=100,y=300)


Exit=Button(option_frame,text='Exit',font=('Times', 16),fg='darkblue',width=15,command=destroy)
Exit.place(x=300,y=300)

msg_Frame= customtkinter.CTkFrame(option_frame, width=500, height=400)
msg= customtkinter.CTkLabel(msg_Frame,text='')
msg.pack()

root.mainloop()

