num = int(input("Digite a quantidade de linhas: "))
lista = [[0 for i in range(num)] for i in range(num)]
inicio = 0
fim = num - 1
cont = 1

while cont <= num * num:
   i = inicio
   while i <= fim:
      lista[inicio][i] = cont
      cont += 1
      i += 1

   i = inicio + 1
   while i <= fim:
      lista[i][fim] = cont
      cont += 1
      i += 1

   i = fim - 1
   while i >= inicio:
      lista[fim][i] = cont
      cont += 1
      i -= 1

   i = fim - 1
   while i > inicio:
      lista[i][inicio] = cont
      cont += 1
      i -= 1

   inicio += 1
   fim -= 1

for matrix in range(num):
   print(lista[matrix])