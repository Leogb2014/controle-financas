from utilitarios import cadastrarCategoria, cadastrarTransacao, saldoTotal

cadastrarCategoria("receitas")
cadastrarCategoria("despesas")

while True:
    d = input("Descrição: ")
    v = float(input("Digite o valor: "))
    c = input("Categoria ( Receitas / Despesas ): ")
    cadastrarTransacao(descricao=d, valor=v, categoria=c)
    continuar = input("Deseja continuar? s/n")
    if continuar == "n":
        saldoTotal()
        break
