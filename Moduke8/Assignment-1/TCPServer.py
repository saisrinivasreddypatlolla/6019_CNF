import socket

def main():
	host = '10.10.9.57'
	port = 5010

	s = socket.socket()
	s.bind((host,port))
	print("server started")
	s.listen(1)
	client,addr = s.accept()
	print("connection from: "+str(addr))
	while True:
		data = client.recv(1024).decode()
		if not data:
			break
		print("recieved data from client is: "+str(data))
		l = data.split()
		if l[1]=="INR":
			if l[-1] == "Dollar":
				client.send(str(int(l[2])/67).encode())
			if l[-1] == "Pounds":
				client.send(str((int(l[2])/67)*0.75).encode())
			if l[-1] == "Yen":
				client.send(str((int(l[2])/67)*113.41).encode())
		if l[1]=="Dollar":
			if l[-1] == "Pounds":
				client.send(str(int(l[2])*0.75).encode())
			if l[-1] == "Yen":
				client.send(str(int(l[2])*113.41).encode())
			if l[-1] == "INR":
				client.send(str(int(l[2])*67).encode())
		if l[1]=="Pounds":
			if l[-1] == "Dollar":
				client.send(str(int(l[2])/0.75).encode())
			if l[-1] == "Yen":
				client.send(str((int(l[2])/0.75)*113.41).encode())
			if l[-1] == "INR":
				client.send(str((int(l[2])/0.75)*67).encode())
		if l[1]=="Yen":
			if l[-1] == "Dollar":
				client.send(str(int(l[2])/113.41).encode())
			if l[-1] == "Pounds":
				client.send(str((int(l[2])/113.41)*0.75).encode())
			if l[-1] == "INR":
				client.send(str((int(l[2])/113.41)*67).encode())
	client.close()

if __name__ =="__main__":
	main()		
