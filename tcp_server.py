from __future__ import print_function
import socket
import sys
import json
from operator import itemgetter
import time

# print information or not: if verbose is equal to 0 the programme will run silently. If it is set to 1 it will print some information
verbose = int(sys.argv[1])

# Create the necessary socket
tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 65432)

if verbose == 1: print('starting up on %s port %s' %(server_address))

# link socket to server address and listen to the incoming connections
tcp_socket.bind(server_address)
tcp_socket.listen(10)

while True:

	if verbose == 1: print('I am all ears... responding when the connection is established...')
	client_connection, client_address = tcp_socket.accept()
	start_time = time.time()

	try: 

		if verbose == 1: print('client connection is coming from an address: ', client_address) 

		# as long as there is a connection between client and the server, read the data and do soemthing with it
		while True:

			# receive the data from the client in 4K bytes (4096 bytes)
			client_data = client_connection.recv(4096)
			
			# calculate the time difference for writing
			recv_time = time.time()
			diff_time = recv_time - start_time 

			if client_data:

				# convert json string into a list of dictionary
				data = json.loads(client_data)

				if verbose == 1: 
					print('the keys of the JSON message sent by the client')
					for key in data[0].keys(): print(key)

				# reverse should be false for ascending and true for descending order
				sorted_data = sorted(data, key=itemgetter('timestamp'), reverse=False)

				if (len(sorted_data) >= 10) or (diff_time >= 10.0):
					# write the output to a text file
					with open('output_file.txt', 'a') as file:
		 				file.write(json.dumps(sorted_data))

	finally:

		# clean up everything and close the connection
		client_connection.close()