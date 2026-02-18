from transacao import Transacao
from categoria import Categoria

LISTA_CATEGORIAS = []


def cadastrarCategoria(nome):
        nova_categoria = Categoria(nome=nome)
        LISTA_CATEGORIAS.append(nova_categoria)

        return nova_categoria

