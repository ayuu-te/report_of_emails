# send_email_report.py
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime
import config

def send_email(subject, body, to_addrs):
    msg = MIMEMultipart()
    msg['From'] = config.EMAIL_ADDRESS
    msg['To'] = ", ".join(to_addrs)
    msg['Subject'] = subject
    
    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP(config.SMTP_SERVER, config.SMTP_PORT)
        server.starttls()
        server.login(config.EMAIL_ADDRESS, config.EMAIL_PASSWORD)
        text = msg.as_string()
        server.sendmail(config.EMAIL_ADDRESS, to_addrs, text)
        server.quit()
        print(f"Email sent successfully to {', '.join(to_addrs)}")
    except Exception as e:
        print(f"Failed to send email: {str(e)}")

def create_report():
    # Replace this with actual report generation logic
    report_date = datetime.now().strftime("%Y-%m-%d")
    report_body = f"Daily Report for {report_date}\n\nEverything is running smoothly."
    return report_body

if __name__ == "__main__":
    report = create_report()
    send_email(subject="Daily Report", body=report, to_addrs=["recipient@example.com"])
