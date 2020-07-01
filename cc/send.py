from email.message import EmailMessage
import smtplib

def send(email,message,purpose):
	msg = EmailMessage()
	to_email_addrs = email
	from_email_addrs = 'campuscoins2020@gmail.com'
	msg['From'] = from_email_addrs
	msg['To'] = to_email_addrs
	try:
		int(message)
		
	except ValueError:
		msg.set_content(f'Click on this link to verify your email,{message}')

	if purpose == 'Transaction':
		msg['Subject'] = 'OTP - Transaction'
		msg.set_content(f'The OTP for your Transaction is, {message}')

	if purpose == 'ChangePass':
		msg['Subject'] = 'OTP - Change Password'
		msg.set_content(f'The OTP to change your password is, {message}')

	if purpose == 'EmailVerify':
		msg['Subject'] = 'Verification Link'
		msg.set_content(f'Click on this link to verify your Email, {message}')

	if purpose == 'ResetPass':
		msg['Subject'] = 'Password Reset Link'
		msg.set_content(f'Click on this link to change your forgotten Password, {message}')

	if purpose == 'receiver':
		msg['Subject'] = 'Amount Credited'
		amount = message.split("-")[1]
		sender = message.split("-")[0]
		msg.set_content(f'You received {amount} cc from {sender}\r\nTo check open: victorvickie.pythonanywhere.com')

	if purpose == 'sender':
		msg['Subject'] = 'Amount Debited'
		amount = message
		msg.set_content(f'You have been debited {amount} cc\r\nTo check open: victorvickie.pythonanywhere.com')

	p = 'bisfhskwmnkbpfac'

	with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
		smtp.login(from_email_addrs,p)
		smtp.send_message(msg)