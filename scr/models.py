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
    
