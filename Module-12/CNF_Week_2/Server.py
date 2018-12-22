import socket
from xlrd import *
from threading import *

def main():
	host = '10.2.138.21'
	port = 5025
	loc = ("E:/CNF/6019_CNF/Module-12/CNF_Week_2/data.xlsx")
	wb = open_workbook(loc) 
	sheet = wb.sheet_by_index(0)
	rollnumbers = []
	questions = []
	answers = []
 
	sheet.cell_value(0, 0)
	for i in range(sheet.nrows):
		rollnumbers.append(str(int(sheet.cell_value(i,0))))
		questions.append(sheet.cell_value(i,1))
		answers.append(str(sheet.cell_value(i,2)))
	s = socket.socket()
	s.bind((host,port))
	print("server started")
	s.listen(10)
	while True:
		client,addr = s.accept()
		print("connection from: "+str(addr))
		roll = "Enter your RollNumber"
		client.send(roll.encode())
		data = client.recv(1024).decode()
		if not data:
			break
		elif str(data) not in rollnumbers:
			message = "ROLLNUMBER-NOTFOUND"
			client.send(message.encode())
		else:
			Thread(target = attendance, args = (client, data, rollnumbers, questions, answers)).start()

		
	s.close()
def attendance(client, data, rollnumbers, questions, answers):
	value = questions[rollnumbers.index(data)]
	client.send(str(value).encode())
	answer = client.recv(1024).decode()
	if str(answer) == str(answers[rollnumbers.index(data)]):
		message1 = "ATTENDANCE-PASSED"
		client.send(message1.encode())
		return
	else:
		message2 = "ATTENDANCE-FAILURE"+ '\n'
		client.send(message2.encode())
		attendance(client, data, rollnumbers, questions, answers)

if __name__ =="__main__":
	main()		
