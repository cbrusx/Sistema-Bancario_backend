from models import Cliente
from datetime import datetime

cliente = Cliente

def depositar(cliente, valor_deposito):
    if valor_deposito < 0:
        return {"status":"erro","mensagem":"VALOR INVALIDO"}
    data_transacao = datetime.now()
    data_transacao = data_transacao.strftime("%Y/%m/%d %H:%M:%S")
    
    transacoes = {
        "tipo":"deposito",
        "valor":valor_deposito,
        "data_hora":data_transacao,
        "mensagem":f"Deposito de R${valor_deposito:.2f} {'-'*20} {data_transacao}"
    }
    cliente.historico.append(transacoes)
    cliente.saldo += valor_deposito
    return {"status":"erro","mensagem":"DEPOSITO REALIZADO COM SUCESSO"}


def sacar(cliente, valor_saque):
    if valor_saque <= 0:
        return {"status":"erro","mensagem":"VALOR INVALIDO"}
    if valor_saque > cliente.saldo:
        return {"status":"erro","mensagem":"VALOR INSUFICIENTE"}    
    
    data_transacao = datetime.now()
    data_transacao = data_transacao.strftime("%Y/%m/%d %H:%M:%S")

    transacoes = {
        "tipo":"saque",
        "valor":valor_saque,
        "data_hora": data_transacao,
        "mensagem":f"Saque de R${valor_saque:.2f} {'-'*24} {data_transacao}"
    }
    cliente.historico.append(transacoes)
    cliente.saldo -= valor_saque
    return {"status":"erro","mensagem":"SAQUE REALIZADO COM SUCESSO"}


def converter_dados(cliente):
    titular_transacao = cliente.titular
    saldo_transacao = cliente.saldo
    historico_transacao = cliente.historico

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
    return "\n".join(descricao_historico)


def filtro_historico(dados_convertidos, opcao_filtro):
    historico_filtrado = []
    for filtro in dados_convertidos["historico"]:
        if filtro["tipo"] == opcao_filtro:
            historico_filtrado.append(filtro)
    
    filtro_formatado = []
    for formatar in historico_filtrado:
        if "mensagem" in formatar:
            filtro_formatado.append(formatar["mensagem"])
    return "\n".join(filtro_formatado)

