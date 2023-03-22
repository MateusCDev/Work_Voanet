import os
import sys


def traceroute(address, hops=30, timeout=5):
    # verifica se o sistema operacional é Windows ou Unix-based
    if sys.platform.startswith('win'):
        ping_cmd = f'ping -n 1 -w {int(timeout*1000)} {address}'
        tracert_cmd = f'tracert -h {hops} -w {int(timeout*1000)} {address}'
    else:
        ping_cmd = f'ping -c 1 -W {int(timeout)} {address}'
        tracert_cmd = f'tracert {address} -m {hops} -w {int(timeout*1000)}'

    print(f"Testando conexão com {address}...\n")
    response = os.system(ping_cmd)
    if response == 0:
        print(f"\nConexão com {address} bem-sucedida.\n")
    else:
        print(f"\nFalha ao se conectar com {address}.\n")
        return

    print(f"Fazendo traceroute para {address}...\n")
    try:
        with os.popen(tracert_cmd) as traceroute_result:
            result = traceroute_result.read()
            print(f"\nTraceroute completo:\n{result}")
            return result
    except Exception as e:
        print(f"\nErro ao executar traceroute:\n{e}")
        return None


def main():
    print("Bem vindo a ferramenta para analisar rota e perda de pacotes em sites/jogos")
    endereco = input("Insira o endereço IP ou domínio do server do site|jogo: ")
    hops = int(input("Insira o número máximo de saltos [padrão=30]: ") or 30)
    timeout = int(input("Insira o tempo limite em segundos [padrão=5]: ") or 5)

    result = traceroute(endereco, hops, timeout)

    if result is not None:
        save_option = input("Deseja salvar o resultado em um arquivo? (s/n): ").lower()
        if save_option == "s":
            filename = input("Insira o nome do arquivo de saída: ")
            with open(filename, "w") as file:
                file.write(result)
                print(f"\nResultado salvo em '{filename}'")

    print("\nDesenvolvido por Mateus Cesar de Araujo")


if __name__ == "__main__":
    main()

