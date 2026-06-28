Simples = 25.0
Frango = 30.0
Completo = 50.0
Refri = 5.0
total = 0.0
produto = 0.0
pedido = 0

while(pedido != 5):
    print("MENU")
    print("1 - Hambúrguer simples R$25.0")
    print("2 - Hambúrguer de frango R$30.0")
    print("3 - Hambúrguer completo R$50.0")
    print("4 - Refrigerante 5.0")
    print("5 - Sair e ver total")
    pedido = int(input("Digite o numero do item que você quer pedir: "))
    if pedido == 5: break
    if pedido < 1 or pedido > 5:
        print("Digite um valor válido!")
    continue

    if(pedido < 5):
        quantidade = int(input("Digite quantos itens você quer: "))
        if(pedido == 1):
            total += quantidade * Simples
        elif(pedido == 2):
            total += quantidade * Frango
            
        elif(pedido == 3):
            total += quantidade * Completo
        elif pedido == 4:
            total += quantidade * Refri
if(total < 50.0):
        total += 7.0
        print(f"Valor dos hamburguer: {total}")
        print(f"Como sua compra deu menos de R$50 é combrado uma taxa de 7 reais a entrega")
        print(f"Total: {total}")
else:
    print(f"Valor dos hamburguer: {total}")
    print(f"Como sua compra deu mais de R$50 não é combrado uma taxa de entrega")
    print(f"Total: {total}")