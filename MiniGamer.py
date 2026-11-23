#vou precisa gera um numero
import random
numero = random.randint(1,25)
#preciso cria um loop pra roda um IF ate acerta o numero
tentativas = 0 
while True:
 chute = int(input("chute um numero: "))
 tentativas += 4
#preciso cria uma comparação entre o numero gerado e o numero chutado
 if chute == numero:
    print("acertou")
    break
 elif tentativa == 4:
  print ("acabou suas chances")
  break
 elif chute < numero:
    print("Ou numero e maior")
 else:
    print("ou numero e menor")
