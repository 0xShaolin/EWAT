"""-------------------------------------------------
I would prefer that this be used as a module.

However, standalone code will be produced.
-------------------------------------------------"""

import smtplib

class Email:
	def __init__(self):
		self.author = ["Diante aka Shaolin"]
		self.version = ["0.1"] # will update if necessary
		self.contact = ["odinsecurity@protonmail.com", "https://github.com/0xShaolin"]

		self.mailClient = smtplib.SMTP("mail.cock.li:587")
		self.mailClient.starttls()
		self.mailClient.ehlo()

	def login(self, username, password):
		try:
			self.mailClient.login(username, password)
			self.username = username
			return 0 # 0 success
		except:
			return 1 # nonzero = failure

	def setHeader(self, spoofName, spoofFrom, spoofTo, subject):
		self.recipient = spoofTo
		self.mail = "From: %s <%s>\nTo: %s\nSubject: %s\n\n" % (spoofName, spoofFrom, spoofTo, subject)

	def send(self, message):
		self.mail += message
		try:
			self.mailClient.sendmail(self.username, self.recipient, self.mail)
			return 0
		except:
			return 1
	def close(self):
		self.mailClient.quit()

def login(x):
	import getpass

	username = raw_input("[*] Cock.li Email: ")
	password = getpass.getpass("[*] Cock.li Password: ")

	if x.login(username, password):
		print "Login successful!\n"
		return 0
	else:
		print "Login failed. Please Try Again.\n"
		return 1

def sendMessage(x):
	sendFrom = raw_input("[*] Email to Spoof As: ")
	sendName = raw_input("[*] Name to Spoof As: ")
	sendTo = raw_input("[*] Target's Email: ")
	subject = raw_input("[*] Email Subject: ")
	x.setHeader(sendName, sendFrom, sendTo, subject)

	message = raw_input("[*] Message: ")

	try:
		x.send(message)
		print "\n\n[!] Message sent successfully!"
		return 0
	except:
		print "\n\n[!] Message not sent."

def main():
	x = Email()

	h = 1

	while h != 0:
		h = login(x)

	sendMessage(x)

if __name__ == "__main__":
	main()
