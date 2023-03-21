# Importing libraries
import time
import hashlib
from urllib.request import urlopen, Request
import pandas as pd
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC8cececd83cdae25430f8eacb853efd93"
# Your Auth Token from twilio.com/console
auth_token  = "0253c25019f8e2b31f0c8bc69083d87f"
client = Client(account_sid, auth_token)



# setting the URL you want to monitor
url = Request('https://oab.fgv.br/NovoSec.aspx?key=L7X80yWJsR4=&codSec=5149',
			headers={'User-Agent': 'Mozilla/5.0'})

# to perform a GET request and load the
# content of the website and store it in a var
response = urlopen(url).read()

# to create the initial hash
currentHash = hashlib.sha224(response).hexdigest()
print("running")
time.sleep(10)
while True:
	try:
		# perform the get request and store it in a var
		response = urlopen(url).read()

		# create a hash
		currentHash = hashlib.sha224(response).hexdigest()

		# wait for 30 seconds
		time.sleep(30)

		# perform the get request
		response = urlopen(url).read()

		# create a new hash
		newHash = hashlib.sha224(response).hexdigest()

		# check if new hash is same as the previous hash
		if newHash == currentHash:
			continue

		# if something changed in the hashes
		else:
			# notify
			print("something changed")

			message = client.messages.create(
						messaging_service_sid='MG0d36ef5d15b874cad33eeb3e5a68b456',
            to='+5517981462389',
            body=f'Site FGV OAB foi atualizado')
			
			print(message.sid)

			message = client.messages.create(
						messaging_service_sid='MG0d36ef5d15b874cad33eeb3e5a68b456',
            to='+5517996822227',
            body=f'Site FGV OAB foi atualizado')
			
			print(message.sid)

	# To handle exceptions
	except Exception as e:
		print("error")
