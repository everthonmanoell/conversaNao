import socket

def main():
    # Configura o cliente
    host = '127.0.0.1'  # IP do servidor
    port = 5555

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))

    while True:
        # Solicita ao usuário para inserir uma mensagem
        message = input("Digite uma mensagem: ")

        # Envia a mensagem para o servidor
        client.send(message.encode('utf-8'))

        # Recebe a resposta do servidor
        response = client.recv(1024)
        print(f"Resposta do servidor: {response.decode('utf-8')}")

if __name__ == "__main__":
    main()
