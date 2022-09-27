x = int(input("Quantidade de jogos que o mandante cedeu mais 2 escanteios? "))
jogos = int(input("Quantidade de jogos? "))

escanteios = x / jogos
valor = escanteios * 100

print('O valor é {:.0f}'.format(valor))
if valor > 60:
    print("O valor é maior que 60%.")
else:
    print('O valor é menor que 60%. Cancelar bet.')
    
z = int(input("Quantidade de jogos que o visitante teve mais de 2 escanteios? "))
jogo = int(input("Quantidade de jogos? "))

escanteios_ = z / jogo
valor_ = escanteios_ * 100

print('O valor é {:.0f}'.format(valor_))

if valor_ > 60:
    print('O valor é maior do que 60%.')
else:
    print('O valor é menor que 60%. Cancelar bet.')

total = valor + valor_
divisao = total / 2
print('O resultado da soma dos números e mais a divisão por 2 é: {:.0f}'.format(divisao))

precificacao = divisao / 100
valorfinal = 1 / precificacao
print('Valor da precificação justa é {:.2f}'.format(valorfinal))
print('Odds de {:.2f} é o preço justo.'.format(valorfinal))





