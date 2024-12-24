# Email sent automation
'''now we will add subject and make sure to address is visible along with body of email using email package'''

import smtplib  # Import the smtplib library for sending emails


# Import necessary classes from the email package for creating email content
# mime stands for Multipurpose internet mail extensions
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Define the sender's and recipient's email addresses
From = "thadkapallysaikiran2001@gmail.com"
to = "savinayvinay909@gmail.com"
subject = "Python testmail"  # Define the subject of the email

# Create a MIMEMultipart message object
msg = MIMEMultipart()
msg['From'] = From  # Set the sender's email address
msg['To'] = to  # Set the recipient's email address
msg['Subject'] = subject  # Set the subject of the email

# Define the body of the email
body = "Hello! first mail using python script"
msg.attach(MIMEText(body, 'plain'))  # Attach the body to the email as plain text

# Convert the MIMEMultipart object to a string
text = msg.as_string()

# Set up the SMTP server
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()  # Start TLS for security
server.login(From, "ovvt jyvm rpfz oyso")  # Log in to the email account

# Send the email
server.sendmail(From, to, text)
print("Mail sent")  # Print a confirmation message

# Quit the SMTP server
server.quit()















