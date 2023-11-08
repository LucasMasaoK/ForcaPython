import random

listaPalavras=['pizza','sushi','lanche']
ArraypalavraSorteada=[]
ArraypalavraSorteadaTamanho=[]
palavraSorteada= random.choice(listaPalavras);
for i in range(0,len(palavraSorteada)):
    ArraypalavraSorteada.append(palavraSorteada[i])
    ArraypalavraSorteadaTamanho.append('#')
print(ArraypalavraSorteada)
for x in range(0,5):
    chute = input('Escolha uma letra:')
    for i in range(0,len(palavraSorteada)):
        if ArraypalavraSorteada[i]==chute:
            ArraypalavraSorteadaTamanho.pop(i)
            ArraypalavraSorteadaTamanho.insert(i,chute)
            print(ArraypalavraSorteadaTamanho)
            continue
    continue
if '#' in ArraypalavraSorteadaTamanho:
    print('Você perdeu!')
    print(ArraypalavraSorteadaTamanho)
else:
    print('Você ganhou!')
    print(ArraypalavraSorteada)










