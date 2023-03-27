import pyperclip
import subprocess
import time
import sys
import os

def menu():
    print("""
        Bem-vindo ao Toolkit do NOC
        Selecione a opção desejada:

        1) Scripts/Datacom
        2) Scripts/Nokia
        3) Scripts/Parks
        4) Teste de latência para jogos online
        5) Teste de traceroute
        0) Sair
""")

    menu = int(input("Digite a opção escolhida: "))

    print("\n")
    return menu


def main():

    while True:
        opcao = (menu())

        if opcao == 1:
                datacom = int(input(''' 
                                        #######################################################
                                            Selecione a opção de configuração da DATACOM 

                                            1) Achar ONU
                                            2) Achar service-port e vlan
                                            3) Provisionamento
                                            4) Remover ONU|ONT
                                            0) Sair

                                            Digite o numero para selecionar a opção desejada: '''))
                print("\n")
                if datacom == 1:
                     
                     porta= input("Digite o numero da porta: ")
                     script_achar=(f"sh int gp 1/1/{porta} onu")

                     print(script_achar)
                     pyperclip.copy(script_achar)

                elif datacom == 2:
                     
                     script_achar_2 = (f'''
sh run service-port | nomore
sh vlan
                        '''.strip())
                     
                     print(script_achar_2)
                     pyperclip.copy(script_achar_2)

                elif datacom == 3:
                    porta = input("Digite a porta: ")
                    onu = input("Digite a onu: ")
                    serial = input("Digite a serial: ")
                    line_profile = input("Digite o line profile correspondente: ")
                    vlan = input("Digite a Vlan: ")
                    service_port = input("Digite o serivice port: ")

                    script_datacom = (f"""
config terminal
interface gpon 1/1/{porta}
onu {onu}
serial-number {serial} 
line-profile {line_profile}
ethernet 1
negotiation
no shutdown
native vlan vlan-id {vlan} cos 0
top
service-port {service_port} gpon 1/1/{porta} onu {onu} gem 1 match vlan 
vlan-id {vlan} action vlan replace vlan-id {vlan}
commit
                            """.strip())
                    
                    print("\n")
                    print(script_datacom)
                    print("\n")

                    pyperclip.copy(script_datacom)
                elif datacom == 4:

                    print("Bem vindo ao passo a passo de como remover a ONU|ONT em caso de mudança de endereço")
                    print('''
                            Primeiro descubra a ONU|ONT do cliente que esta pendente em provisionar
                            Cole o script na CLI da OLT
                            '''.strip())
                    print("\n")

                    script_discovery = (f"show interface gpon 1/1 discovered-onus".strip())
                    print(script_discovery)
                    pyperclip.copy(script_discovery)

                    print("\n")
                    serial = input("Apos descobrir a onu digite a serial do equipamento: ")
                    print("Agora cole o script a seguir:")
                    script_onu= (f"show interface gpon 1/1 onu | include {serial}")
                    print(script_onu)
                    pyperclip.copy(script_onu)
                    print("\n")

                    

                elif datacom == 0:
                     break

        if opcao == 2:
                nokia = int(input(''' 
    #########################################################
    Selecione a opção de configuração da NOKIA

    1) Provisionamento
    2) Remover ONU
    0) Sair

    Digite o numero para selecionar a opção desejada: '''))
                print("\n")

                if nokia == 1:
                    olt = input("Digite a OLT/SLOT: ")
                    porta = input("Digite a porta: ")
                    onu = input("Digite a ONT: ")
                    nome = input("Digite o nome da cliente: ")
                    caixa = input("Digite a caixa/CTO: CX")
                    serial = input("Digite a serial: ALCL:FC")
                    vlan = input("Digite a Vlan: ")

                    script_nokia = (f'''
configure equipment ont interface 1/1/{olt}/{porta}/{onu} sw-ver-pland auto desc1 "{nome}" desc2 "CX{caixa}" sernum ALCL:FC{serial} pland-cfgfile1 disabled optics-hist enable
configure equipment ont interface 1/1/{olt}/{porta}/{onu} admin-state up 
configure qos interface ont:1/1/{olt}/{porta}/{onu} ds-queue-sharing
configure equipment ont slot 1/1/{olt}/{porta}/{onu}/14 plndnumdataports 1 plndnumvoiceports 0 planned-card-type veip admin-state up
configure qos interface 1/1/{olt}/{porta}/{onu}/14/1 upstream-queue 0 bandwidth-profile name:HSI_200M_UP
configure bridge port 1/1/{olt}/{porta}/{onu}/14/1 max-unicast-mac 10
configure bridge port 1/1/{olt}/{porta}/{onu}/14/1 vlan-id {vlan} tag single-tagged
configure interface port uni:1/1/{olt}/{porta}/{onu}/14/1 admin-up
'''.strip())
                    print("\n")
                    print(script_nokia)
                    print("\n")

                    pyperclip.copy(script_nokia)

                elif nokia == 2:
                    olt = input("Digite a olt: ")
                    porta = input("Digite a porta: ")
                    onu = input("Digite a onu: ")
                    
                    script_nokia_delete = (f"""
configure equipment ont interface 1/1/{olt}/{porta}/{onu} admin-state down
configure equipment ont slot 1/1/{olt}/{porta}/{onu}/14 admin-state down
configure interface port uni:1/1/{olt}/{porta}/{onu}/14/1 no admin-up
configure equipment ont no interface 1/1/{olt}/{porta}/{onu}
                    """.strip())
                    print("\n")
                    print(script_nokia_delete)
                    print("\n")

                    pyperclip.copy(script_nokia_delete)

                elif nokia == 0:
                    break

                else:
                    print("Opção inválida. Tente novamente.\n")

        if opcao == 3:

                parks = int(input(''' 
                #########################################################
                Selecione a opção de configuração da Parks

                1) Provisionamento Router
                2) Provisionamento Bridge
                3) Remover ONU
                0) Sair

                Digite o número para selecionar a opção desejada: '''))
                print("\n")

                if parks == 1:
                    porta = input("Digite a porta: ")
                    onu = input("Digite a onu: ")
                    serial = input("Digite a serial: ")
                    vlan = input("Digite a Vlan: ")
                    
                    script_parks_1 =(f"""
config terminal
interface gpon 1/{porta}
onu add serial-number {serial}
onu {serial} flow-profile onu_router_vlan_{vlan}
do copy running-config startup-config
                    """.strip())

                    print("\n")
                    print(script_parks_1)
                    print("\n")

                    pyperclip.copy(script_parks_1)
                    
                elif parks == 2:
                    porta = input("Digite a porta: ")
                    onu = input("Digite a onu: ")
                    serial = input("Digite a serial: ")
                    vlan = input("Digite a Vlan: ")

                    script_parks_2 = (f"""
config terminal
interface gpon 1/{porta}
onu add serial-number {serial}
onu {serial} flow-profile onu_bridge_vlan_{vlan}_pon6
onu {serial} vlan-translation-profile _{vlan} uni-port 1
do copy running-config startup-config
                    """.strip())
                    print("\n")
                    print(script_parks_2)
                    print("\n")
                    pyperclip.copy(script_parks_2)

                elif parks == 3:
                    porta = input("Digite a porta: ")
                    onu = input("Digite a onu: ")
                    serial = input("Digite a serial: ")

                    script_parks_delete = (f"""
config terminal
interface gpon 1/{porta}
no onu {serial}
end
copy running-config startup-config
                    """.strip())
                    print("\n")
                    print(script_parks_delete)
                    print("\n")
                    pyperclip.copy(script_parks_delete)

                elif parks == 0:
                    break

                else:
                    print("Opção inválida. Digite um número válido.") 
        if opcao == 4:
            def test_latency(server):
                """Envia 10 pacotes ICMP para o servidor e calcula a média do tempo de resposta."""
                cmd = f"ping {server} -n 10 | findstr /i \"média\""
                completed_process = subprocess.run(cmd, stdout=subprocess.PIPE, shell=True, text=True)
                if completed_process.returncode == 0:
                    latency = float(completed_process.stdout.split("=")[1].split("ms")[0].strip())
                    return latency
                else:
                    return None

            def main_latencia():
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
            main_latencia() 
        if opcao == 5:
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
                

            def main_tracerout():
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
            main_tracerout()                           
        if opcao == 0:
             break     
main()
            