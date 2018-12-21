import socket

def main():
	host = '10.10.9.57'
	port = 5012

	server = ('10.10.9.57', 5135)

	s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
	s.bind((host, port))

	message = input("enter message here: ")
	while message!="q" :
		s.sendto(message.encode(), server)
		data, addr = s.recvfrom(1024)
		print(str(data.decode()))
		message = input("enter message here")
	s.close()
	
if __name__ == "__main__":
	main()	

