import socket

def main():

    HOST = '194.210.229.204'  # The remote host
    PORT = 9500              # The same port as used by the server

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        r = input("R:")
        g = input("G:")
        b = input("B:")
        #i="0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0|0|255|0"
        i=""
        for j in range(200):
            i = i + r + "|"
            i = i + g + "|"
            i = i + b + "|"
        s.sendall(i.encode('UTF-8'))

if __name__ == '__main__':
    main()
