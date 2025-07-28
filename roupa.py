valor = float(input("Digite o valor da roupa: R$ "))
cupom = input("Digite o cupom: ").upper().strip()
if cupom == "NIVER10":
    valor_final = valor - (valor * 0.10)
    print(f"Valor da compra: R${valor_final}")
else:
    print(f"Cupom inválido, valor: R${valor}")