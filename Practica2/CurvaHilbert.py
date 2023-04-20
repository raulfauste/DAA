import matplotlib.pyplot as plt

def hilbert(n,puntoX,puntoY,ori,tamaño):
    if n==1:
        if ori==1:
            x = [puntoX-tamaño,puntoX-tamaño,puntoX+tamaño,puntoX+tamaño]
            y = [puntoY+tamaño,puntoY-tamaño,puntoY-tamaño,puntoY+tamaño]
            return x,y
        elif ori==0:
            x = [puntoX - tamaño, puntoX + tamaño, puntoX + tamaño, puntoX - tamaño]
            y = [puntoY + tamaño, puntoY + tamaño, puntoY - tamaño, puntoY - tamaño]
            return x, y
        elif ori==2:
            x = [puntoX + tamaño, puntoX -tamaño, puntoX - tamaño, puntoX + tamaño]
            y = [puntoY + tamaño, puntoY + tamaño, puntoY - tamaño, puntoY - tamaño]
            return x, y
        elif ori==3:
            x = [puntoX - tamaño, puntoX -tamaño, puntoX + tamaño, puntoX + tamaño]
            y = [puntoY - tamaño, puntoY + tamaño, puntoY + tamaño, puntoY - tamaño]
            return x, y
    else:
        if ori==0:
            cuadra1 = hilbert(n - 1, puntoX - tamaño, puntoY + tamaño, 1, tamaño / 2)
            cuadra2 = hilbert(n - 1, puntoX - tamaño, puntoY - tamaño, 3, tamaño / 2)
            cuadra3 = hilbert(n - 1, puntoX + tamaño, puntoY - tamaño, 0, tamaño / 2)
            cuadra4 = hilbert(n - 1, puntoX + tamaño, puntoY + tamaño, 0, tamaño / 2)
            return cuadra1[0] + cuadra4[0] + cuadra3[0] + cuadra2[0][::-1], cuadra1[1] + cuadra4[1] + cuadra3[1] + cuadra2[1][::-1]
        elif ori==1:
            cuadra1 = hilbert(n - 1, puntoX - tamaño, puntoY + tamaño, 0, tamaño / 2)
            cuadra2 = hilbert(n - 1, puntoX - tamaño, puntoY - tamaño, 1, tamaño / 2)
            cuadra3 = hilbert(n - 1, puntoX + tamaño, puntoY - tamaño, 1, tamaño / 2)
            cuadra4 = hilbert(n - 1, puntoX + tamaño, puntoY + tamaño, 2, tamaño / 2)
            return cuadra1[0] + cuadra2[0] + cuadra3[0] + cuadra4[0][::-1], cuadra1[1] + cuadra2[1] + cuadra3[1] + cuadra4[1][::-1]
        elif ori==2:
            cuadra1 = hilbert(n - 1, puntoX - tamaño, puntoY + tamaño, 2, tamaño / 2)
            cuadra2 = hilbert(n - 1, puntoX - tamaño, puntoY - tamaño, 2, tamaño / 2)
            cuadra3 = hilbert(n - 1, puntoX + tamaño, puntoY - tamaño, 3, tamaño / 2)
            cuadra4 = hilbert(n - 1, puntoX + tamaño, puntoY + tamaño, 1, tamaño / 2)
            return cuadra4[0][::-1] + cuadra1[0] + cuadra2[0] + cuadra3[0], cuadra4[1][::-1] + cuadra1[1] + cuadra2[1] + cuadra3[1][::-1]
        elif ori==3:
            cuadra1 = hilbert(n - 1, puntoX - tamaño, puntoY + tamaño, 3, tamaño / 2)
            cuadra2 = hilbert(n - 1, puntoX - tamaño, puntoY - tamaño, 0, tamaño / 2)
            cuadra3 = hilbert(n - 1, puntoX + tamaño, puntoY - tamaño, 2, tamaño / 2)
            cuadra4 = hilbert(n - 1, puntoX + tamaño, puntoY + tamaño, 3, tamaño / 2)
            return cuadra2[0][::-1] + cuadra1[0] + cuadra4[0] + cuadra3[0], cuadra2[1][::-1] + cuadra1[1] + cuadra4[1] + cuadra3[1]

curva = hilbert(4,0,0,1,4)
plt.plot(curva[0],curva[1])
plt.show()