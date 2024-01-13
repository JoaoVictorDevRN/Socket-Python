import socket

# Define uma função para receber um arquivo de uma conexão socket
def receber_arquivo(nome_arquivo, conexao):
    try:
        # Abre o arquivo em modo binário ('wb') para escrita
        with open(nome_arquivo, 'wb') as arquivo:
            # Continua recebendo dados enquanto houver dados disponíveis
            while True:
                data = conexao.recv(4096)
                # Se não houver mais dados, sai do loop
                if not data:
                    break
                # Escreve os dados recebidos no arquivo
                arquivo.write(data)
        # Imprime uma mensagem indicando que o arquivo foi recebido com sucesso
        print(f'{nome_arquivo} recebido com sucesso!')
    except Exception as e:
        # Imprime uma mensagem de erro se ocorrer um erro durante a recepção do arquivo
        print(f'Ocorreu um erro durante a recepção do arquivo: {str(e)}')
    finally:
        # Fecha a conexão após a recepção ou em caso de erro
        conexao.close()

# Cria um socket TCP
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Estabelece uma conexão com o servidor no endereço localhost e porta 8080
    client.connect(('localhost', 8080))
    # Imprime uma mensagem indicando que a conexão foi estabelecida
    print('Conectado!\n')

    # Solicita ao usuário que forneça o nome do arquivo a ser enviado
    nome_arquivo = input('Arquivo> ')

    # Envia o nome do arquivo codificado para o servidor
    client.send(nome_arquivo.encode())
    # Imprime uma mensagem indicando que o pedido para enviar o arquivo foi enviado
    print(f'Pedido para enviar o arquivo {nome_arquivo} enviado.')

    # Chama a função para receber o arquivo do servidor
    receber_arquivo(nome_arquivo, client)

except Exception as e:
    # Imprime uma mensagem de erro se ocorrer um erro durante a execução do cliente
    print(f'Ocorreu um erro: {str(e)}')

finally:
    # Fecha o socket do cliente, independentemente do resultado
    client.close()
