#SOPHIA PEREIRA OZÓRIO - 13903467

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

 #função que calcula o coeficiente angular da reta
def eq_reta(yp, yc, xp, xc):    
    mr = (yp - yc) / (xp - xc) 
    nr = -1 * (mr * xc - yc)    
    return mr

print("Cálculo da interseção entre as duas retas")
print("Digite os valores para cada plano e gere o gráfico correspondente!")

#Informações câmera 1
xc1 = float(input("Digite o valor de x da camera 1 (em metros): "))
yc1 = float(input("Digite o valor de y da camera 1 (em metros): "))
zc1 = float(input("Digite o valor de z da camera 1 (em metros): "))
xp1 = float(input("Digite o valor de x da projeção da camera 1 (em metros): "))
yp1 = float(input("Digite o valor de y da projeção da camera 1 (em metros): "))
zp1 = float(input("Digite o valor de z da projeção da camera 1 (em metros): "))

#Informações câmera 2
xc2 = float(input("Digite o valor de x da camera 2 (em metros): "))
yc2 = float(input("Digite o valor de y da camera 2 (em metros): "))
zc2 = float(input("Digite o valor de z da camera 2 (em metros): "))
xp2 = float(input("Digite o valor de x da projeção da camera 2 (em metros): "))
yp2 = float(input("Digite o valor de y da projeção da camera 2 (em metros): "))
zp2 = float(input("Digite o valor de z da projeção da camera 2 (em metros): "))

print("---Plano XY---")
mrXY1 = eq_reta(yp1, yc1, xp1, xc1) #coeficiente angular da reta 1
mrXY2 = eq_reta(yp2, yc2, xp2, xc2) #coeficiente angular da reta 2

x_xy = (-(mrXY2*xc2) + yc2 + (mrXY1*xc1) - yc1) / (mrXY1 - mrXY2); #x do cruzamento
y_xy = (mrXY1*x_xy)  - (mrXY1*xc1) + yc1; #y do cruzamento

print ("O coeficiente angular da reta 1 eh: %.3f" %mrXY1)
print ("O coeficiente angular da reta 2 eh: %.3f" %mrXY2)
print ("O valor de x do cruzamento eh: %.3f" %x_xy)
print ("O valor de y do cruzamento eh: %.3f" %y_xy)

print("---Plano XZ---")
mrXZ1 = eq_reta(zp1, zc1, xp1, xc1) #coeficiente angular da reta 1
mrXZ2 = eq_reta(zp2, zc2, xp2, xc2) #coeficiente angular da reta 2

x_xz = (-(mrXZ2*xc2) + zc2 + (mrXZ1*xc1) - zc1) / (mrXZ1 - mrXZ2); #x do cruzamento
z_xz = (mrXZ1*x_xz)  - (mrXZ1*xc1) + zc1; #z do cruzamento

print ("O coeficiente angular da reta 1 eh: %.3f" %mrXZ1)
print ("O coeficiente angular da reta 2 eh: %.3f" %mrXZ2)
print ("O valor de x do cruzamento eh: %.3f" %x_xz)
print ("O valor de z do cruzamento eh: %.3f" %z_xz)

print("---Plano ZY---")
mrZY1 = eq_reta(yp1, yc1, zp1, zc1) #coeficiente angular da reta 1
mrZY2 = eq_reta(yp2, yc2, zp2, zc2) #coeficiente angular da reta 2

z_zy = (-(mrZY2*zc2) + yc2 + (mrZY1*zc1) - yc1) / (mrZY1 - mrZY2); #Z do cruzamento
y_zy = (mrZY1*z_zy)  - (mrZY1*zc1) + yc1; #y do cruzamento

print ("O coeficiente angular da reta 1 eh: %.3f" %mrZY1)
print ("O coeficiente angular da reta 2 eh: %.3f" %mrZY2)
print ("O valor de z do cruzamento eh: %.3f" %z_zy)
print ("O valor de y do cruzamento eh: %.3f" %y_zy)

fig = plt.figure(figsize=(7,7))
ax = fig.add_subplot(projection = '3d')  #gráfico 3d vazio

#Ponto da câmera 1
ax.scatter(xc1, yc1, zc1, c='yellow', label='Câmera 1') 
ax.scatter(xp1, yp1, zp1, c='orange', label='Projeção da Câmera 1') 

#Ponto da câmera 2
ax.scatter(xc2, yc2, zc2, c='green', label='Câmera 2') 
ax.scatter(xp2, yp2, zp2, c='skyblue', label='Projeção da Câmera 2') 

x1 = np.linspace(xc1, xp1)
y1 = np.linspace(yc1, yp1)
z1 = np.linspace(zc1, zp1)

 #linha Câmera-Projeção 1
ax.plot(x1, y1, z1, color = 'k')

x2 = np.linspace(xc2, xp2)
y2 = np.linspace(yc2, yp2)
z2 = np.linspace(zc2, zp2)

#linha Câmera-Projeção 2
ax.plot(x2, y2, z2, color = 'k') 

ax.legend() #quadro com as legendas
ax.set_xlim(0, 5) #limite do eixo x
ax.set_ylim(0, 5) #limite do eixo y
ax.set_zlim(0, 5) #limite do eixo z
ax.set_xlabel('X') #Nome do eixo x
ax.set_ylabel('Y') #Nome do eixo y
ax.set_zlabel('Z') #Nome do eixo z

#mostra o gráfico
plt.show() 
