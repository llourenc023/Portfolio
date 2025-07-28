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
