class Cliente():
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo
        self.historico = []

    def saldo(self):
        return self.__saldo
    
    def depositar(self, valor_deposito):
        if valor_deposito < 0:
            return {"status":"erro", "mensagem":"VALOR INVALIDO"}
        self.__saldo += valor_deposito
        return {"status":"sucesso", "mensagem":"DEPOSITO REALIZADO COM SUCESSO"}
    

    def saque(self, valor_saque):
        if valor_saque <= 0:
            return {"status":"erro", "mensagem":"VALOR INVALIDO"}
        if valor_saque > self.__saldo:
            return {"status":"erro","mensagem":"VALOR INSUFICIENTE"}
        self.__saldo -= valor_saque
        return {"status":"sucesso","mensagem":"SAQUE REALIZADO COM SUCESSO"}
           