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
            "mensagem":"f'Deposito de R${valor_deposito} as {data_transacao}",
        }
        models.historico.append(transacoes)
        models.saldo += valor_deposito



