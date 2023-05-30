# SMTP Module

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/M4M03Q2JN)

This module adds a function file called smtp.py to the project, which can be used to notify you that a new connection has been made to your C2.

# Usage

### .env file
1. Create a new file in your main directory called ".env"
2. Inside of the directory, input the proper information for your email address, and which account you wish to receive the messages on

### smtp.py 

1. Create a new folder called "functions", and add the smtp.py file to it. 
2. Inside of your C2 main script, add a new import - ```from functions.smtp import email_handler```
3. In the ```comm_handler``` function, add the following variable - ```email_format = f'{hostname_val}@{remote_ip[0]}'```
4. On the following line in ```comm_handler```, add the following call - ```email_handler(email_format)```

What is happening here is that we are creating a variable that will load into the email_handler function of smtp.py, which will tell you the hostname and IP address of the connecting client. The smtp.py script will load the environmental variables set in .env, start a SMTP session, and send an email with the information provided by the variable.

