
# Exercicio 2

def is_fibonnaci(n):
  if n < 0:
    return False
  
  a, b = 0, 1

  if n == 0 or n == 1:
    return True

  while b < n:
    a, b = b, a + b

  return b == n

numero = int(input("Informe um número para verificar se faz parte da sequencia de fibonnaci: "))

if is_fibonnaci(numero):
  print("Esse número faz parte da sequencia de fibonnaci")
else:
  print("Esse numero nao faz parte da sequencia de fibonnaci. ")

