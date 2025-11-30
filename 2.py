import uuid

# Dados iniciais do estoque
estoque = [
    {"codigoProduto": 101, "descricaoProduto": "Caneta Azul", "estoque": 150},
    {"codigoProduto": 102, "descricaoProduto": "Caderno Universitário", "estoque": 75},
    {"codigoProduto": 103, "descricaoProduto": "Borracha Branca", "estoque": 200},
    {"codigoProduto": 104, "descricaoProduto": "Lápis Preto HB", "estoque": 320},
    {"codigoProduto": 105, "descricaoProduto": "Marcador de Texto Amarelo", "estoque": 90}
]

# Lista para armazenar as movimentações
movimentacoes = []

def buscar_produto(codigo_produto):
    """Retorna o dicionário do produto pelo código."""
    for produto in estoque:
        if produto["codigoProduto"] == codigo_produto:
            return produto
    return None

def registrar_movimentacao(codigo_produto, quantidade, tipo, descricao_mov):
    """Registra uma movimentação com identificador único."""
    movimentacoes.append({
        "idMovimentacao": str(uuid.uuid4()),
        "codigoProduto": codigo_produto,
        "tipo": tipo,
        "descricaoMovimentacao": descricao_mov,
        "quantidade": quantidade
    })

def adicionar_estoque(codigo_produto, quantidade, descricao_mov):
    """Lança uma entrada de mercadoria e retorna o saldo final."""
    produto = buscar_produto(codigo_produto)

    if not produto:
        return "Produto não encontrado."

    if quantidade <= 0:
        return "A quantidade de entrada deve ser maior que zero."

    produto["estoque"] += quantidade
    registrar_movimentacao(codigo_produto, quantidade, "ENTRADA", descricao_mov)

    return f"Entrada registrada. Estoque final de {produto['descricaoProduto']}: {produto['estoque']}"

def remover_estoque(codigo_produto, quantidade, descricao_mov):
    """Lança uma saída de mercadoria e retorna o saldo final."""
    produto = buscar_produto(codigo_produto)

    if not produto:
        return "Produto não encontrado."

    if quantidade <= 0:
        return "A quantidade de saída deve ser maior que zero."

    if produto["estoque"] < quantidade:
        return f"Estoque insuficiente. Disponível: {produto['estoque']}"

    produto["estoque"] -= quantidade
    registrar_movimentacao(codigo_produto, quantidade, "SAIDA", descricao_mov)

    return f"Saída registrada. Estoque final de {produto['descricaoProduto']}: {produto['estoque']}"

def consultar_estoque(codigo_produto):
    """Consulta o estoque atual de um produto."""
    produto = buscar_produto(codigo_produto)

    if produto:
        return f"Estoque de {produto['descricaoProduto']} (Cód {produto['codigoProduto']}): {produto['estoque']}"
    
    return "Produto não encontrado."

def listar_movimentacoes():
    """Lista todas as movimentações de forma detalhada."""
    if not movimentacoes:
        print("Nenhuma movimentação registrada.")
        return

    print("\n--- Histórico de Movimentações ---")
    for mov in movimentacoes:
        produto = buscar_produto(mov["codigoProduto"])
        descricao_produto = produto["descricaoProduto"] if produto else "Produto Desconhecido"
        
        print(f"ID: {mov['idMovimentacao']}")
        print(f"Produto: {descricao_produto} (Cód: {mov['codigoProduto']})")
        print(f"Tipo: {mov['tipo']}")
        print(f"Descrição: {mov['descricaoMovimentacao']}")
        print(f"Quantidade: {mov['quantidade']}")
        print("-" * 40)

def menu():
    """Exibe as opções do menu."""
    return [
        "1. Entrada de Mercadoria (Adicionar Estoque)",
        "2. Saída de Mercadoria (Remover Estoque)",
        "3. Consultar Estoque de Produto",
        "4. Listar Todas as Movimentações",
        "5. Sair"
    ]

# --- Loop Principal de Execução ---

print("--- Sistema de Gestão de Estoque ---")

while True:
    print("\n" + "="*40)
    print("Selecione uma Opção:")
    for item in menu():
        print(f"  {item}")
    print("="*40)
    
    try:
        # Pega a escolha do usuário
        escolha = int(input("Escolha uma opção (1-5): "))
    except ValueError:
        print("Opção inválida. Por favor, digite um número.")
        continue

    if escolha == 5:
        print("Saindo do sistema. Até logo!")
        break
    
    elif escolha in [1, 2]:
        try:
            # Solicita dados para movimentação
            codigo_produto = int(input("Digite o Código do Produto: "))
            quantidade = int(input("Digite a Quantidade a ser movimentada: "))
            descricao_mov = input("Digite a Descrição da Movimentação (ex: 'Compra Forn X', 'Venda Cliente Y'): ")

            if escolha == 1:
                print(adicionar_estoque(codigo_produto, quantidade, descricao_mov))
            else:
                print(remover_estoque(codigo_produto, quantidade, descricao_mov))
                
        except ValueError:
            print("Entrada inválida para Código ou Quantidade. Tente novamente.")
            
    elif escolha == 3:
        try:
            # Solicita dados para consulta
            codigo_produto = int(input("Digite o Código do Produto para consulta: "))
            print(consultar_estoque(codigo_produto))
        except ValueError:
            print("Entrada inválida para Código. Tente novamente.")

    elif escolha == 4:
        # Chama a função de listagem
        listar_movimentacoes()
        
    else:
        print("Opção inválida. Escolha um número entre 1 e 5.")
