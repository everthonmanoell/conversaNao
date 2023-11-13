import socket
import threading

def handle_client(client_socket):
    while True:
        # Aguarda a mensagem do cliente
        data = client_socket.recv(1024)
        if not data:
            break

        # Exibe a mensagem recebida
        print(f"Recebido: {data.decode('utf-8')}")

        # Envia a mesma mensagem de volta para o cliente
        client_socket.send(data)

    # Fecha a conexão com o cliente
    client_socket.close()

def main():
    # Configura o servidor
    host = '0.0.0.0'  # Escuta em todas as interfaces disponíveis
    port = 5555

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(5)

    print(f"[*] Ouvindo em {host}:{port}")

    while True:
        # Aguarda a conexão do cliente
        client, addr = server.accept()
        print(f"[*] Conexão aceita de {addr[0]}:{addr[1]}")

        # Inicia uma thread para lidar com o cliente
        client_handler = threading.Thread(target=handle_client, args=(client,))
        client_handler.start()

if __name__ == "__main__":
    main()
