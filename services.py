from models import Cliente
from datetime import Datetime

def saldo(models):
    saldo = models.saldo
    return saldo


def depositar(models, valor_deposito):
    if valor_deposito > 0:
        data_transacao = Datetime.now()
        data_transacao = data_transacao.strftime("%Y/%m/%d %H:%M:%S")
        
        transacoes = {
            "tipo":"deposito",
            "valor":"valor_deposito",
            "data_hora":data_transacao,
            "mensagem":"f'Deposito de R${valor_deposito:.2f} as {data_transacao}"
        }
        models.historico.append(transacoes)
        models.saldo += valor_deposito


def sacar(models, valor_saque):
    if valor_saque < 0:
        return "Valor Invalido"
    elif valor_saque > models.saldo:
        return "Valor Insuficiente"
    else:
        data_transacao = Datetime.now()
        data_transacao = data_transacao.strftime("%Y/%m/%d %H:%M:%S")

        transacoes = {
            "tipo":"saque",
            "valor":"valor_saque",
            "data_hora": data_transacao,
            "mensagem":"f'Saque de R${valor_saque:.2f} as {data_transacao}"
        }
        models.historico.append(transacoes)
        models.saldo -= valor_saque
