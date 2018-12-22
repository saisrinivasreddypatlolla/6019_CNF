import socket

def main():
	host = '10.2.138.21'
	port = 5025

	s = socket.socket()
	s.connect((host,port))

	data = s.recv(1024).decode()
	if str(data) == 'ROLLNUMBER-NOTFOUND':
		print(str(data))
		return
	else:
		message = input(str(data)+" : ")
		s.send(message.encode())
		while True:
			data = s.recv(1024)
			if str(data) == 'ATTENDANCE-PASSED':
				return
			message = input(str(data.decode())+" : ")
			s.send(message.encode())
	s.close()
if __name__ == "__main__":
	main()	

