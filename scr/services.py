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


def converter_dados(models):
    titular_transacao = models.titular
    saldo_transacao = models.saldo
    historico_transacao = models.historico

    dados_convertidos = {
        "titular": titular_transacao,
        "saldo": saldo_transacao,
        "historico": historico_transacao
    }
    return dados_convertidos


def historico_mensagem(dados_convertidos):
    descricao_historico = []
    for descricao in dados_convertidos["historico"]:
        if "mensagem" in descricao:
            descricao_historico.append(descricao["mensagem"])
    return "/n".join(descricao_historico)


def filtro_historico(dados_convertidos, opcao_filtro):
    historico_filtrado = []
    for filtro in dados_convertidos["historico"]:
        if filtro["tipo"] == opcao_filtro:
            historico_filtrado.append(filtro)
    
    filtro_formatado = []
    for formatar in historico_filtrado:
        if "mensagem" in formatar:
            filtro_formatado.append(formatar["mensagem"])
    return "/n".join(filtro_formatado)

