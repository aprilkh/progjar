from threading import Thread
import socket
import os

SERVER_IP = "127.0.0.1"
SERVER_PORT = 9000
FILE_SIZE = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = (SERVER_IP, SERVER_PORT)
sock.bind(server_address)

namagambar = ["griz.png", "ice.png", "pan.png"]


def kirimGambar(CLIENT_IP, CLIENT_PORT):
    addr = (CLIENT_IP, CLIENT_PORT)
    sock.sendto("START", (addr))
    for nama_gambar in namagambar:
        ukuran_gambar = os.stat(nama_gambar).st_size
        sock.sendto("SEND {}".format(nama_gambar), (addr))

        fp = open(nama_gambar, 'rb')
        k = fp.read()
        x_size = 0

        for x in k:
            sock.sendto(x, (addr))
            x_size = x_size + 1
            print "\r terkirim {} of {} ".format(x_size, ukuran_gambar)

        sock.sendto("FINISH", (addr))
        fp.close()

    sock.sendto("END", (addr))


while True:
    data, addr = sock.recvfrom(1024)
    print "Menerima: " + str(data)
    if str(data) == "READY":
        thread = Thread(target=kirimGambar, args=(addr))
        thread.start()



