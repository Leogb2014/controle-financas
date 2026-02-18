from transacao import Transacao
from categoria import Categoria

LISTA_CATEGORIAS = []
LISTA_TRANSACOES = []


def cadastrarCategoria(nome):
        nova_categoria = Categoria(nome=nome)
        LISTA_CATEGORIAS.append(nova_categoria)

        return nova_categoria


def cadastrarTransacao(descricao, valor, categoria):
        nova_transacao = Transacao(descricao=descricao, valor=valor, categoria=categoria)
        LISTA_TRANSACOES.append(nova_transacao)

        return nova_transacao

