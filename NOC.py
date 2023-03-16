import pyperclip

def menu():
    print("""
              ╔══════════════════════════════════════════╗
              ║    Bem-vindo ao NOC/SPACE -              ║
              ║ Selecione o fabricante para configurações║
              ║                                          ║
              ║      1) Datacom                          ║
              ║      2) Nokia                            ║
              ║      3) Parks                            ║
              ║      0) Sair                             ║
              ║                                          ║
              ║  Digite o número correspondente ao       ║
              ║   fabricante para acessar opções de      ║
              ║             configuração                 ║
              ╚══════════════════════════════════════════
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
        if opcao == 0:
             break     
main()
            