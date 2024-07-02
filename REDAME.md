# Daily Email Report

This project automates sending daily email reports using Python. It includes a script to generate and send emails and a configuration file for email credentials.

## Files

- `send_email_report.py`: Main script to send email reports.
- `config.py`: Configuration file for email credentials and SMTP server details.
- `README.md`: Project documentation.
- `.gitignore`: Specifies files and directories to be ignored by Git.

## Setup

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/email_report_project.git
    cd email_report_project
    ```

2. Install necessary Python packages:
    ```sh
    pip install smtplib email
    ```

3. Configure email credentials in `config.py`:
    ```python
    # config.py
    EMAIL_ADDRESS = "your_email@example.com"
    EMAIL_PASSWORD = "your_password"
    SMTP_SERVER = "smtp.example.com"
    SMTP_PORT = 587
    ```

4. Run the script to send a test email:
    ```sh
    python send_email_report.py
    ```

## Scheduling the Script

### On Unix-based Systems (using cron):

1. Open the crontab file:
    ```sh
    crontab -e
    ```

2. Add the following line to schedule the script to run daily at 8 AM:
    ```sh
    0 8 * * * /usr/bin/python3 /path/to/send_email_report.py
    ```

### On Windows (using Task Scheduler):

1. Open Task Scheduler and create a new task.
2. Set the trigger to run daily at your desired time.
3. Set the action to start a program, and specify the path to your Python executable and the script:
    - Program/script: `C:\Path\To\Python.exe`
    - Add arguments (optional): `C:\Path\To\send_email_report.py`
