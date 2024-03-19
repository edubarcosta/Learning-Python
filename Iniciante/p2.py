# -- Faça um Programa que peça as 4 notas bimestrais e mostre a média --
# Vamos tratar que as notas vão de 0 a 100, não existem notas quebradas.
# Caso após a divisão, o número seja decimal, este mesmo será arredondado.

nome = str(input("Informe o nome do aluno: "))

nota1 = float(input("Informe a nota do primeiro bimestre: "))
nota2 = float(input("Informe a nota do segundo bimestre: "))
nota3 = float(input("Informe a nota do terceiro bimestre: "))
nota4 = float(input("Informe a nota do quarto bimestre: "))
media = (nota1 + nota2 + nota3 + nota4) / 4

if 0 <= media <= 100:
    if media >= 60:
        print(f'A nota final de {nome} foi {round(media, 0)}')
        print("Ele foi aprovado")
    else:
        print(f'A nota final de {nome} foi {round(media, 0)}')
        print("Ele foi reprovado")
else:
    print("NOTA INVÁLIDA")

