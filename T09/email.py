### --- OOP Email Simulator --- ###


# --- Email Class --- #
# Create the class, constructor and methods to create a new Email object.
class Email:
    # Declare the class variable, with default value, for emails. 
    has_been_read = False
    
    # Initialise the instance variables for emails.
    def __init__(self,email_address, subject_line, email_content, has_been_read):
        self.email_address=email_address
        self.subject_line=subject_line
        self.email_content=email_content
        self.has_been_read=has_been_read

    # Create the method to change 'has_been_read' emails from False to True.
    def mark_as_read(self):
        self.has_been_read = True

# --- Lists --- #
# Initialise an empty list to store the email objects.
inbox=[]

def populate_inbox():
      
    # Create 3 sample emails and add it to the Inbox list. 
    inbox=[
        "123@gmail.com",
        "Welcome to HyperionDev!",
        "email content 1",
        "456@hotmail.com",
        "Great work on the bootcamp!",
        "email content 2",
        "789@yahoo.com",
        "Your excellent marks!",
        "email content 3",
    ]       
    return inbox

def list_emails(emails):    
    # Create a function which prints the email’s subject_line, along with a corresponding number.
    enum_emails=list(enumerate(emails))
    for i, j in enumerate(emails):        
        print(f"{i}    {j}")

# Create a function which displays a selected email.
def read_email(index):

    print(f'''\n Email from: {index.email_address}
              Subject: {index.subject_line}
              Content: {index.email_content}''')
    # Once displayed, call the class method to set its 'has_been_read' variable to True.
    Email.mark_as_read(index)
    return False

# --- Email Program --- #

menu = True
# Call the function to populate the Inbox for further use in your program.
inbox = populate_inbox()
Email1=Email(inbox[0],inbox[1],inbox[2],False)
Email2=Email(inbox[3],inbox[4],inbox[5],False)
Email3=Email(inbox[6],inbox[7],inbox[8],False)

inbox_subject=[Email1.subject_line, Email2.subject_line, Email3.subject_line]
#list_emails(inbox_subject)

while True:
    try:
        user_choice = int(input('''\nWould you like to:
    1. Read an email
    2. View unread emails
    3. Quit application

    Enter selection: '''))
       
        if user_choice == 1:
        # add logic here to read an email
            UserBool=True

            while UserBool == True:
                try:
                    email_choice= int(input(f'''\n Which email would you like to read:
    1. From: {Email1.email_address} Subject: {Email1.subject_line} Read: {Email1.has_been_read}
    2. From: {Email2.email_address} Subject: {Email2.subject_line} Read: {Email2.has_been_read}
    3. From: {Email3.email_address} Subject: {Email3.subject_line} Read: {Email3.has_been_read}
    4. Go Back

    Enter selection: '''))
        
                    if email_choice==1:
                        UserBool=read_email(Email1)
                    elif email_choice==2:
                        UserBool=read_email(Email2)
                    elif email_choice==3:
                        UserBool=read_email(Email3)
                    elif email_choice==4:
                        break
                    else:
                        print("Oops - incorrect input.")

                except ValueError:
                    print("The input was not valid.\n")

        elif user_choice == 2:
            if Email1.has_been_read==True:
                print(f"\nEmail from {Email1.email_address} has been read\n")
            else:
                print(f"\nEmail from {Email1.email_address} has not been read\n")
            if Email2.has_been_read==True:
                print(f"\nEmail from {Email2.email_address} has been read\n")
            else:
                print(f"\nEmail from {Email2.email_address} has not been read\n")
            if Email3.has_been_read==True:
                print(f"\nEmail from {Email3.email_address} has been read\n")
            else:
                print(f"\nEmail from {Email3.email_address} has not been read\n")
 
            
        elif user_choice == 3:
            break
        # quit appplication

        else:
            print("Oops - incorrect input.")
    except ValueError:
        print("The input was not valid.\n")
