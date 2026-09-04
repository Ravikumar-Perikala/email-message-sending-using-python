Gmail Email Sender using Python

A simple and professional Python project that sends emails through Gmail SMTP using Python's built-in smtplib and email libraries.

This project demonstrates how to connect to Gmail's SMTP server, authenticate securely using a Gmail App Password, compose an email, and send it programmatically.

🚀 Features
Send emails using Gmail SMTP
Uses Python's built-in smtplib library
Supports HTML/plain-text email composition
Secure authentication using a Gmail App Password
Simple and beginner-friendly implementation
🛠️ Technologies Used
Python 3
smtplib
email.message.EmailMessage
Gmail SMTP
📁 Project Structure
gmail-email-sender/
│
├── send_email.py
├── README.md
├── .gitignore
└── requirements.txt


No external Python packages are required because the project uses Python's standard library.

⚙️ Gmail Configuration

To send emails through Gmail, you should use a Google App Password instead of your normal Gmail password.

1. Enable 2-Step Verification

Enable 2-Step Verification on the Google account that will send the email.

2. Create an App Password

Create an App Password from your Google Account security settings.

You will receive a 16-character password that can be used by your Python application.

Security warning: Never publish your Gmail password or App Password in your GitHub repository.

🔐 Using Environment Variables

Instead of putting your credentials directly in the Python source code, set them as environment variables.

Linux / macOS
export EMAIL_ADDRESS="your-email@gmail.com"
export EMAIL_APP_PASSWORD="your-app-password"
export RECIPIENT_EMAIL="recipient@gmail.com"

Windows PowerShell
$env:EMAIL_ADDRESS="your-email@gmail.com"
$env:EMAIL_APP_PASSWORD="your-app-password"
$env:RECIPIENT_EMAIL="recipient@gmail.com"

▶️ How to Run

Clone the repository:

git clone https://github.com/YOUR_USERNAME/gmail-email-sender.git
cd gmail-email-sender


Set your email credentials as environment variables and run:

python send_email.py


If everything is configured correctly, you should see:

Email sent successfully!

🔒 Security

Never commit credentials to GitHub.

Do not write this:

server.login("your-email@gmail.com", "your-app-password")


Instead, use environment variables:

server.login(EMAIL_ADDRESS, EMAIL_APP_PASSWORD)


Add .env or other credential files to .gitignore if you use them.

Example .gitignore:

__pycache__/
*.pyc
.env
venv/
.venv/

⚠️ Important

If you accidentally publish a Gmail App Password on GitHub:

Immediately revoke the exposed App Password.
Create a new App Password.
Remove the credential from your source code.
Never commit credentials to the repository again.
📌 Future Improvements

Possible improvements for this project include:

HTML email support
Email attachments
Sending emails to multiple recipients
Email templates
Command-line arguments
Logging and error reporting
Configuration through a .env file
👨‍💻 Author

Perikala Ravikumar (IAS)
