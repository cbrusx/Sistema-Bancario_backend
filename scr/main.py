from models import Cliente
import services
from datetime import datetime

cliente_titular = Cliente("CAIO",100)

print(f"OLÁ, SEJA BEM-VINDO {cliente_titular['cliente_titular']}")
while True:
    print("1 -> VER SALDO")
    print("2 -> DEPOSITAR")
    print("3 -> SACAR")
    print("4 -> VER EXTRATO")
    print("5 -> VER EXTRATO FILTRADO")
    
    opcao_menu = input("DIGITE UM NUMERO DO MENU QUE DESEJA VER")
    