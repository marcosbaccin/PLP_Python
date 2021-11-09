largura = float(input('Digite a largura: ')) 

#  Esta maneira de entrada a seguir gasta menos bytecode que a maneira anterior
print('Digite o comprimento:')
comprimento = float(input())

area = largura * comprimento

print('A area da sala é: ', area)  # Esta primeira forma de print usa menos bytecode que as demais
print('A area da sala é: ', largura*comprimento)  # Utiliza 4 bytecodes a mais que a 1ª maneira
print('A area da sala é: %.2f.' % area)  # Utiliza 2 bytecodes a mais que a 1ª maneira
print(f'A area da sala é: {area:.2f}.')  # Utiliza 8 bytecodes a mais que a 1ª maneira
