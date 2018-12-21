import socket
def main():
	host = '10.10.9.57'
	port = 5135

	s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
	s.bind((host, port))
	print("server started")
	while True:
		data, addr = s.recvfrom(1024)
		if not data:
			break
		print("recived message from client is : "+data.decode())
		l = data.decode().split()
		if l[1]=="INR":
			if l[-1] == "Dollar":
				s.sendto(str(int(l[2])/67).encode(), addr)
			if l[-1] == "Pounds":
				s.sendto(str((int(l[2])/67)*0.75).encode(), addr)
			if l[-1] == "Yen":
				s.sendto(str((int(l[2])/67)*113.41).encode(), addr)
		if l[1]=="Dollar":
			if l[-1] == "Pounds":
				s.sendto(str(int(l[2])*0.75).encode(), addr)
			if l[-1] == "Yen":
				s.sendto(str(int(l[2])*113.41).encode(), addr)
			if l[-1] == "INR":
				s.sendto(str(int(l[2])*67).encode(), addr)
		if l[1]=="Pounds":
			if l[-1] == "Dollar":
				s.sendto(str(int(l[2])/0.75).encode(), addr)
			if l[-1] == "Yen":
				s.sendto(str((int(l[2])/0.75)*113.41).encode(), addr)
			if l[-1] == "INR":
				s.sendto(str((int(l[2])/0.75)*67).encode(), addr)
		if l[1]=="Yen":
			if l[-1] == "Dollar":
				s.sendto(str(int(l[2])/113.41).encode(), addr)
			if l[-1] == "Pounds":
				s.sendto(str((int(l[2])/113.41)*0.75).encode(), addr)
			if l[-1] == "INR":
				s.sendto(str((int(l[2])/113.41)*67).encode(), addr)
	s.close()

if __name__ == '__main__':
	main()

