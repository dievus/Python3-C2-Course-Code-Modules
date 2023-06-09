# SMTP Module

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/M4M03Q2JN)

<p align="center">
  <img src="https://github.com/dievus/Python3-C2-Course-Code-Modules/blob/main/SMTP%20Module/images/smtp.png" />
</p>

This module adds a function file called smtp.py to the project, which can be used to notify you that a new connection has been made to your C2.

# Usage

### .env file
1. Create a new file in your main directory called ".env"
2. Inside of the directory, input the proper information for your email address, and which account you wish to receive the messages on

### smtp.py 

1. Create a new folder called "functions", and add the smtp.py file to it. 
2. Inside of your C2 main script, add a new import - ```from functions.smtp import email_handler```
3. In the ```comm_handler``` function, add the following variable code block after op_sys
```
if email_gen == 1:
    email_format = f'{remote_ip[0]}'
    email_handler(email_format)
```
4. In the main function, add a variable at the top called ```email_gen```
```
email_gen = 0
```
5. In the command while loop, add the following lines which will enable and disable email notifications
```
# Enable email notifications by setting email_gen value to 1
if command == 'email_gen -e':
    email_gen = 1
# Disable email notifications by setting email_gen value to 0
if command == 'email_gen -d':
    email_gen = 0
```
6. In smtp.py, modify the ```smtp_server``` and ```smtp_port``` variables to meet the requirements of your email service
7. Make sure to update your Help menu with the new commands

### Functionality 

When the C2 server starts, the email_gen variable is set to 0. When you run `email_gen -e` you are setting the email_gen variable to 1, which tells the updated comm_handler function to send the email_format variable to the email_handler variable of smtp.py. The smtp.py file loads the environmental variables set in the .env file, takes the information provided by the email_handler() call, and sends the email.

### Notes

It is up to you to determine how to set up and manage the appropriate information for your email account. 
