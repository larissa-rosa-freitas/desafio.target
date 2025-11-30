from datetime import datetime

def calcula_juros(valor, data_vencimento):
   
    hoje = datetime.now()
    vencimento = datetime.strptime(data_vencimento, "%d/%m/%Y")
    dias_atraso = (hoje - vencimento).days

    if dias_atraso <= 0:
        return valor  # Sem juros se não houver atraso

    taxa_juros_diaria = 0.025  # 2% ao dia
    juros = valor * (taxa_juros_diaria * dias_atraso)
    return valor + juros

print("Cálculo de Juros por Atraso")
print("Entre com o valor da fatura:")
valor_fatura = float(input())
print("Entre com a data de vencimento (dd/mm/aaaa):")
data_vencimento = input()
valor_com_juros = calcula_juros(valor_fatura, data_vencimento)
print(f"Valor a ser pago com juros: R$ {valor_com_juros:.2f}")