import matplotlib.pyplot as plt
import math

velocidadeInicial = float(input("Informe a velocidade inicial em m/s: "))
anguloLancamento = float(input("Informe o ângulo do lançamento: "))
alturaInicial = float(input("Informe a altura inicial do lançamento: "))

gravidade = 9.81

listax = []
listay = []

anguloLancamento = math.radians(anguloLancamento) # convertendo o ângulo para radiano

y = 0
x = 0 

while y >= 0: # até o objeto tocar no solo
    
    listax.append(x)
    listay.append(y)

    y = x * math.tan(anguloLancamento) - ((1 / (2 * (velocidadeInicial **2))) * ((gravidade) * (x **2)) / (math.cos(anguloLancamento)**2)) + alturaInicial # fórmula
    x = x + 0.3 # distância

plt.xlabel ("Distância")
plt.ylabel ("Altura")
plt.plot (listax,listay,"bo")
plt.show()




                    