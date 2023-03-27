import socket
from bs4 import BeautifulSoup


target_list = []


def update_list_servers(host):

    port = 80

    sock = socket.socket(
        socket.AF_INET, socket.SOCK_STREAM)

    try:

        sock.connect((host, port))

        request = "GET / HTTP/1.1\r\nHost:%s\r\n\r\n" % host

        sock.send(request.encode())

        response = sock.recv(4096)

    except Exception:

        print("Failed")

    soup = BeautifulSoup(response, "html.parser")

    target_list.clear()

    for el in soup.find_all('a'):

        if 'http' in el['href']:

            target_list.append(el['href'])
