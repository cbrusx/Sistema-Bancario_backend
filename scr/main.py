from models import Cliente
import services
#from datetime import datetime

cliente_titular = Cliente("CAIO",100)

print(f"OLÁ, SEJA BEM-VINDO {cliente_titular.titular}")
while True:
    print("1 -> VER SALDO")
    print("2 -> DEPOSITAR")
    print("3 -> SACAR")
    print("4 -> VER EXTRATO")
    print("5 -> VER EXTRATO FILTRADO")
    print("0 -> SAIR")
    
    opcao_menu = input("DIGITE UM NUMERO DO MENU QUE DESEJA VER: ")

    if opcao_menu == "1": #SALDO
        saldo = services.saldo(cliente_titular)
        print(saldo)

    elif opcao_menu == "2": #DEPOSITAR
        valor_deposito = float(input("DIGITE O VALOR PARA DEPOSITO: "))
        deposito = services.depositar(cliente_titular, valor_deposito)
        print(deposito["mensagem"])

    elif opcao_menu == "3": #SACAR
        valor_saque = float(input("DIGITE O VALOR PARA SAQUE: "))
        saque = services.sacar(cliente_titular, valor_saque)
        print(saque["mensagem"])

    elif opcao_menu == "4":#VER EXTRATO
        dados_convertidos = services.converter_dados(cliente_titular)
        print(f"/n{'-'*15} EXTRATO BANCARIO DE {cliente_titular.titular}{'-'*15}\n")
        extrato_mensagem = services.historico_mensagem(dados_convertidos)
        print(extrato_mensagem)