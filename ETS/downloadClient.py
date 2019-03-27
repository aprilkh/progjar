import socket


def Main():
    host = '127.0.0.1'
    port = 5000

    s = socket.socket()
    s.connect((host, port))

    namafile = raw_input("masukkan nama file : ")
    if namafile != 'q':
        s.send(namafile)
        data = s.recv(1024)
        if data[:6] == 'EXISTS':
            filesize = long(data[6:])
            message = raw_input("File ada, " + str(filesize) + "Bytes, Mendownload file? (Ya/Tidak)? -> ")
            if message == 'Ya':
                s.send("OKE")
                f = open('new_' + namafile, 'wb')
                data = s.recv(1024)
                totalRecv = len(data)
                f.write(data)
                while totalRecv < filesize:
                    data = s.recv(1024)
                    totalRecv += len(data)
                    f.write(data)
                    print "{0:.2f}".format((totalRecv / float(filesize)) * 100) + "% Done"
                print "Download Berhasil!"
                f.close()
        else:
            print "File Tidak Ada!"

    s.close()


if __name__ == '__main__':
    Main()