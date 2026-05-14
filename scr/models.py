class Cliente():
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo
        self.historico = []

    def saldo(self):
        return self.__saldo
    
