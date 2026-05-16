from models import Cliente
from datetime import datetime

cliente = Cliente
def registrar_transacao(cliente, tipo, deposito, valor_deposito):
    if deposito["status"] == "sucesso":
        data_transacao = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    
        transacoes = {
            "tipo" : tipo,
            "valor" : valor_deposito,
            "data_hora" : data_transacao,
            "mensagem" : f"{tipo} de R${valor_deposito:.2f} {'-'*20} {data_transacao}"
        }
        cliente.historico.append(transacoes)


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

