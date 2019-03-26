import socket

SERVER_IP = "127.0.0.1"
SERVER_PORT = 9000

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto("READY", (SERVER_IP, SERVER_PORT))

def getGambar():
	while True:
		data, addr = sock.recvfrom(1024)
		if data[:4] == "SEND":
			print data[5:]
			fp = open(data[5:], "wb+")

		elif data[:6] == "FINISH":
			fp.close()

		elif data[:3] == "END":
			print "----------FINISH----------"
			break

		else:
			fp.write(data)
			print "Diterima ", len(data), data[0:10]

while True:
	data, addr = sock.recvfrom(1024)
	if str(data) == "START":
		print "Menerima Gambar"
		getGambar()
		break