estoque = 	[
	  {
		"codigoProduto": 101,
		"descricaoProduto": "Caneta Azul",
		"estoque": 150
	  },
	  {
		"codigoProduto": 102,
		"descricaoProduto": "Caderno Universitário",
		"estoque": 75
	  },
	  {
		"codigoProduto": 103,
		"descricaoProduto": "Borracha Branca",
		"estoque": 200
	  },
	  {
		"codigoProduto": 104,
		"descricaoProduto": "Lápis Preto HB",
		"estoque": 320
	  },
	  {
		"codigoProduto": 105,
		"descricaoProduto": "Marcador de Texto Amarelo",
		"estoque": 90
	  }
	]

movimentções = []


def adicionar_estoque(codigo_produto, quantidade):
    for produto in estoque:
        if produto["codigoProduto"] == codigo_produto:
            produto["estoque"] += quantidade
            movimentções.append({
                "codigoProduto": codigo_produto,
                "tipo": "entrada",
                "quantidade": quantidade
            })
            return f"Estoque atualizado. Novo estoque de {produto['descricaoProduto']}: {produto['estoque']}"
    return "Produto não encontrado."

def remover_estoque(codigo_produto, quantidade):
    for produto in estoque:
        if produto["codigoProduto"] == codigo_produto:
            if produto["estoque"] >= quantidade:
                produto["estoque"] -= quantidade
                movimentções.append({
                    "codigoProduto": codigo_produto,
                    "tipo": "saída",
                    "quantidade": quantidade
                })
                return f"Estoque atualizado. Novo estoque de {produto['descricaoProduto']}: {produto['estoque']}"
            else:
                return "Estoque insuficiente."
    return "Produto não encontrado."

def consultar_estoque(codigo_produto):
    for produto in estoque:
        if produto["codigoProduto"] == codigo_produto:
            return f"Estoque de {produto['descricaoProduto']}: {produto['estoque']}"
    return "Produto não encontrado."

def listar_movimentacoes():
    return movimentções

def menu():
    return [
        "1. Adicionar Estoque",
        "2. Remover Estoque",
        "3. Consultar Estoque",
        "4. Listar Movimentações",
        "5. Sair"
    ]       

def executar_opcao(opcao, codigo_produto=None, quantidade=None):
    if opcao == 1:
        return adicionar_estoque(codigo_produto, quantidade)
    elif opcao == 2:
        return remover_estoque(codigo_produto, quantidade)
    elif opcao == 3:
        return consultar_estoque(codigo_produto)
    elif opcao == 4:
        return listar_movimentacoes()
    elif opcao == 5:
        return "Saindo do sistema."
    else:
        return "Opção inválida."
    
print("Sistema de Gestão de Estoque")
escolha = 0
while escolha != 5:
    print("\nMenu:")
    for item in menu():
        print(item) 
    input_escolha = int(input("Escolha uma opção: "))
    executar_opcao(input_escolha)