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
        deposito = cliente_titular.depositar(valor_deposito)
        services.registrar_transacao(cliente_titular, deposito, valor_deposito)
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
    
    elif opcao_menu == "5": #FILTROS DO HISOTRICO BANCARIO 
        print("1 -> FILTRAR DEPOSITOS")
        print("2 -> FILTRAR SAQUE")
        print("3 -> FILTRAR POR DATA")
        print("0 -> VOLTAR MENU PRINCIPAL")

        opcao_menu_filtro = int(input("ESCOLHA QUAL FILTRO VOCE DESEJA VER: "))
        
        if opcao_menu_filtro == 1: #FILTRO DEPOSITO
            opcao_filtro = "deposito"
            filtro_deposito = services.filtro_historico(dados_convertidos, opcao_filtro)
            
            if opcao_filtro == 'deposito':
                    print(f"\n{'LISTA FILTRADA POR DEPOSITOS':-^24}")
                    print(filtro_deposito)

        elif opcao_menu_filtro == 2:
            opcao_filtro = "saque"
            filtro_saque = services.filtro_historico(dados_convertidos, opcao_filtro)
            
            print(f"\n{'LISTA FILTRADA POR SAQUES':-^28}")
            print(filtro_saque)

    elif opcao_menu == "0": #SAIR
        print("MUITO OBRIGADO")
        break
    else: 
        print("VALOR INVALIDO")