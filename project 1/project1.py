import socket
import threading
import json
import time

def build_server(server_list, index):
    bind_ip = "127.0.0.1"
    bind_port = 7000+index
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((bind_ip, bind_port))
    server_list.append(server)
    print("Listening on %s:%d" % (bind_ip, bind_port))

def handle_client(client_socket):
    request = client_socket.recv(1024)
    print("Received: %s" % request)
    client_socket.send(("ACK!").encode())
    client_socket.close()

def server_accept(server, num):
    try:
        client, addr = server.accept()
        print("Acepted connection from: %s:%d" % (addr[0],addr[1]))
        request = client.recv(1024)
        print("Received: %s" % request)
        file_out.write("r" + str(num) + " : " + str(request.decode()) + "\n")
        client.send(("ACK!").encode())
        client.close()
        server.close()
    finally:
        return

if __name__ == "__main__":
    file_out = open('output.txt', 'w')
    file = open('input.json')
    data = json.load(file)
    network = data['network']
    input = data['input']

    server_list=[]
    server_thread=[]
    for i in range(len(network)):
        build_server(server_list, i)

    for i in range(len(input)):
        for j in range(len(input[i])):
            if not (input[i][j][1] in network[i][1]):
                print("unreachable")
                file_out.write("r" + str(i) + " : " + str(input[i][j]) + "Unreachable\n")
                continue
            server_list[input[i][j][1]].listen(5)
            server_thread.append(threading.Thread(target=server_accept, args=(server_list[input[i][j][1]], input[i][j][1],)))
            server_thread[-1].start()
            
            target_host = "127.0.0.1"
            target_port = 7000+input[i][j][1]
            server_list[i].connect((target_host, target_port))
            server_list[i].send((input[i][j][2]).encode())
            response = server_list[i].recv(4096)
            print(response)

            server_thread[-1].join()

            server_list[i].shutdown(socket.SHUT_RDWR)
            server_list[i].close()
            server_list[input[i][j][1]].close()

            bind_ip = "127.0.0.1"
            server_list[i] = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server_list[i].setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            server_list[i].bind((bind_ip, 7000+i))
            server_list[input[i][j][1]] = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server_list[input[i][j][1]].setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            server_list[input[i][j][1]].bind((bind_ip, 7000+input[i][j][1]))

    file_out.close()