pista = float(input('Insira o tamanho da pista em metros:'))  # 4km ou 4000m - 5412
voltas = float(input('Insira a quantidade de voltas:'))  # 20 voltas - 10
reab = float(input('Insira o número de abastecimentos desejados:'))  # 5 reabastecimentos
cons = float(input('Insira o consumo de combustível (em Km/L):'))  # 2Km/L - 0.75

tcons = (((voltas / 1000) * pista) / cons)  # total em litros que preciso para finalizar a prova
reab1 = (tcons / reab)  # mínimo de combustível que preciso até o próximo abastecimento
print('Primeiro abastecimento deve ser de: {:.2f} Litros'.format(reab1))
