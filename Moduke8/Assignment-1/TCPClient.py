import socket

def main():
	host = '10.10.9.57'
	port = 5123

	s = socket.socket()
	s.connect((host,port))
	print ("connection established")
	message = input("->")
	while  message != 'q':
		s.send(message)
		message = s.recv(1024)
		print ('output = ' + message)
		message = input("->")
	s.close()

if __name__ == '__main__':
	main()