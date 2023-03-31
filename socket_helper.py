import socket
from bs4 import BeautifulSoup


target_list = []


def update_list_servers(host):

    port = 80

    sock = socket.socket(
        socket.AF_INET, socket.SOCK_STREAM)

    try:

        REAL_HOST = host.replace(
            "http://", "").replace("https://", "").split("/")[0].split(":")[0]

        print(REAL_HOST)
        sock.connect(("imc.ssau.ru/", port))

        sock.send(
            b'GET / HTTP/1.1\r\nHost: imc.ssau.ru/\r\nConnection:close\r\n\r\n')

        response = sock.recv(4096)

    except Exception as ex:

        print("Failed:" + str(ex))

    soup = BeautifulSoup(response, "html.parser")
    print(soup.text)

    target_list.clear()

    for el in soup.find_all('a'):

        if 'http' in el['href']:

            target_list.append(el['href'])
