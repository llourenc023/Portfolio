print("... Programa desafios ...")
escolha = int(input(print("Digite: \n 1 para roupa \n 2 para ajudando o doutor \n 3 para Maçãs e \n 4 para sair")))
if escolha == 1:
    valor = float(input("Digite o valor da roupa: R$ "))
    cupom = input("Digite o cupom: ").upper().strip()
    if cupom == "NIVER10":
        valor_final = valor - (valor * 0.10)
        print(f"Valor da compra: R${valor_final}")
    else:
        print(f"Cupom inválido, valor: R${valor}")
elif escolha == 2:
        print("Ajudando o doutor: Desafio 1")
        email = input("Digite o e-mail do aluno: ")
        nota = float(input("Digite a nota do aluno: "))
        if nota > 8.5:
            print("ENVIANDO CONVITE")
        else:
            print(f"Nota:{nota}. \nInsufuciente")
elif escolha == 3:
    print("Vamos calcular delta:")
    equacao = 0
    a = float(input("Digite o valor de a: "))
    b = float(input("Digite o valor de b: "))
    c = float(input("Digite o valor de c: "))
    delta = (b ** 2) - (4 * a * c)
    if delta < 0:
        print("Delta negativo, finalizando...")
    elif delta  >= 1:
        print("O valor de delta é:", delta, "\nseguindo para a equação...")
        equacao = ((-b + delta ** 0.5) / (2 * a), (-b - delta ** 0.5) / (2 * a))
        print(f"As raízes da equação são: {equacao[0]} e {equacao[1]}") 
elif escolha == 4:
    print("--- FIM DO PROGRAMA ---")
