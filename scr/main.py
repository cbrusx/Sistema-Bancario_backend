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
        services.depositar(cliente_titular, valor_deposito)
        print(f"FOI DEPOSITADO R${valor_deposito}")   

    elif opcao_menu == "3": #SACAR
        valor_saque = float(input("DIGITE O VALOR PARA SAQUE: "))
        services.sacar(cliente_titular, valor_saque)
        print(f"FOI SACADO R${valor_saque}")