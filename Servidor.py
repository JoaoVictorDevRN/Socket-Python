import socket

# Define uma função para enviar um arquivo para uma conexão socket
def enviar_arquivo(nome_arquivo, conexao):
    try:
        # Abre o arquivo em modo binário ('rb') para leitura
        with open(nome_arquivo, 'rb') as arquivo:
            # Lê o arquivo em blocos de 4 KB
            dados = arquivo.read(4096)
            # Envia os dados enquanto houver algo para ler
            while dados:
                conexao.send(dados)
                dados = arquivo.read(4096)
        # Imprime uma mensagem de sucesso após o envio completo
        print('Arquivo enviado com sucesso!')
    except FileNotFoundError:
        # Se o arquivo não for encontrado, imprime uma mensagem de erro
        print(f'O arquivo "{nome_arquivo}" não foi encontrado.')
    except Exception as e:
        # Se ocorrer um erro durante o envio, imprime a mensagem de erro
        print(f'Ocorreu um erro durante o envio do arquivo: {str(e)}')
    finally:
        # Fecha a conexão após o envio ou em caso de erro
        conexao.close()

# Cria um socket TCP
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Liga o socket ao endereço localhost e à porta 8080
    server.bind(('localhost', 8080))
    # Configura o socket para ouvir por até 1 conexão pendente
    server.listen(1)

    # Imprime uma mensagem indicando que está aguardando uma conexão
    print('Aguardando conexão...')
    # Aceita uma conexão e obtém o objeto de conexão (socket) e o endereço do cliente
    conexao, endereco = server.accept()
    # Imprime uma mensagem indicando que a conexão foi estabelecida
    print(f'Conexão estabelecida com {endereco}')

    # Recebe o nome do arquivo a ser enviado do cliente
    nome_arquivo = conexao.recv(1024).decode()
    # Imprime uma mensagem indicando que recebeu o pedido para enviar o arquivo
    print(f'Recebido pedido para enviar o arquivo: {nome_arquivo}')

    # Chama a função para enviar o arquivo
    enviar_arquivo(nome_arquivo, conexao)

except Exception as e:
    # Imprime uma mensagem de erro se ocorrer um erro durante a execução do servidor
    print(f'Ocorreu um erro: {str(e)}')

finally:
    # Fecha o socket do servidor, independentemente do resultado
    server.close()
