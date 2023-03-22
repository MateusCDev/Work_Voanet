import os
import time

def test_latency(server):
    # envia 10 pacotes ICMP para o servidor e calcula a média do tempo de resposta
    cmd = f"ping {server} -c 10 | awk -F '/' 'END{{ print $5 }}'"
    output = os.popen(cmd).read()
    if output:
        latency = float(output.strip())
        return latency
    else:
        return None

def main():
    print("Bem-vindo ao programa de teste de latência para jogos online!")
    server = input("Digite o endereço do servidor do jogo: ")
    threshold = int(input("Digite o limite de latência desejado (em ms): "))

    while True:
        latency = test_latency(server)
        if latency is None:
            print("Falha ao se conectar ao servidor.")
        else:
            print(f"Latência atual: {latency} ms")
            if latency > threshold:
                print("Atenção: latência alta detectada!")
        time.sleep(1)

if __name__ == "__main__":
    main()
