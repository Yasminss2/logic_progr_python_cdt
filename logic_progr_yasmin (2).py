'''
Como fazer um bolo de chocolate com massa pronta ✨🍰

(A quantidade de pacotes de massa, é importante para a quantidade dos igredientes)

Ingredientes:
Pegue os seguintes ingredientes
2 pacotes de massa pronta de chocolate
6 ovos 
Manteiga 
Caixa de leite

Utensilios:
Batedeira
Forno
Colher
Forma de bolo
Copo medidor

Preparo:
Pegar batedeira, ligar na tomada, na caneca da batedeira, adicione 6 colheres de manteiga, 
em um copo de medidor, coloque 150ml de leite e adicione na batedeira, pegar um ovo por vez 
e quebrar dando leves batidas na ponta da caneca da batedeira para abrir a casca e adicionar 
na caneca o liquido do ovo, jogue as cascas no lixo, abra os pacotes de massa de bolo e 
coloque a caneca na batedeira e  clique no botao da batedeira para comecar a bater e misturar
os ingredientes.

pegue a forma de bolo e um pedaço de papel toalha, passe um pouco de manteiga no papel e comece a 
passar o papel com manteiga por dentro da forma, ligue o forno na tomada e ative o botão de assar.

Desligue a batedeira e pegue a caneca, despeje o conteudo na forma de bolo, e coloque a forma no forno,
escolha a temperatura necessária e aguarde 1h30 para assar.

'''

def fazer_um_bolo(tipo_chocolate) :
    print('Preparo para fazer um bolo:🍰')
    print('1. Pegar batedeira')
    print('2. Adicionar ingredientes na batedeira')
    print('4. Adiconar na forma de bolo a massa')
    print('5. Ligar forno')
    print('6. Colocar a forma no forno')
    print('7. Deixar assando por 1h30')
    print('8. Retirar bolo do forno')
    print('9. Retirar da forma e colocar na boleira')
    print('10. Adicionar calda de chocolate')

    if tipo_chocolate.lower() == 'chocolate':
        resultado = 'Bolo de Chocolate'
    elif tipo_chocolate.lower() == 'cobertura de chocolate':
        resultado = 'Bolo de Chocolate com cobertura de chocolate'
    else:
        resultado = "Bolo de Chocolate com cobertura de chocolate"

    return resultado

meu_bolo = fazer_um_bolo ('cobertura de chocolate')
print(f'Meu bolo é: {meu_bolo}')
