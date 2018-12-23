import socket
import threading
import os, signal
s = socket.socket()
def main():
	host = '192.168.238.1'
	port = 1249
	s.connect((host, port))
	welcomeMsg = s.recv(1024).decode()
	print(welcomeMsg)
	s.send(input().encode())
	threading.Thread(target = sender, args = ()).start()
	while True:
		try:
			msg = s.recv(1024).decode()
			print(msg)
			if msg == "You successfully exited your chat,Thank you ! ":
				os.kill(os.getpid(), signal.CTRL_BREAK_EVENT)
			if not msg:
				continue
			

		except:
			print("Oops!, Host server Closed by admin.")
			break
	s.close()
def sender():
	while True:
		msg = input("->")
		if not msg:
			continue
		s.send(msg.encode())
	s.close()

if __name__ == '__main__':
	main()