import numpy as np
import matplotlib.pyplot as plt
from matplotlib.image import imread
from copy import copy, deepcopy
import scipy as scp
import cv2


#mapa_color = "CMRmap"
#mapa_color = "nipy_spectral"
#mapa_color = "gist_heat"
mapa_color = "gray"


def rgb2gray(rgb):
    return np.dot(rgb[...,:3],[0.2989,0.5870,0.1140])

#imagen = np.genfromtxt("corregida_pulmon_90mAs.txt")
#imagen_fourier = np.fft.fft2(imagen)
imagen = rgb2gray(imread("raton.png"))
imagen = cv2.imread("raton.png")
imagen = cv2.cvtColor(imagen,cv2.COLOR_BGR2YUV)
imagen[:,:,0] = cv2.equalizeHist(imagen[:,:,0])
imagen = cv2.cvtColor(imagen,cv2.COLOR_YUV2BGR)
imagen = rgb2gray(imagen)
np.savetxt("raton_rayosX.txt",imagen)
"""
tamano_x = len(imagen)
tamano_y = len(imagen[0])

#########Filtro Butterworth################
M = int(tamano_x/2.0)
N = int(tamano_y/2.0)
n = 4
D_0 = 50 #Frec de corte

def filtro_butterworth(i,j,M,N,D_0,n):
    D = np.sqrt((i-M)**2 + (j-N)**2)
    if(i==M and j== N):
        return 1.0
    else:
        return 1.0/(1.0 + (D_0/D)**(2*n))

filter_butterworth = np.zeros((tamano_x,tamano_y))
for i in range(len(filter_butterworth)):
    for j in range(len(filter_butterworth[0])):
        filter_butterworth[i,j] = filtro_butterworth(i,j,M,N,D_0,n)
imagen_butterworth_tot = np.zeros((tamano_x,tamano_y))

D_0_p = 10

def filtro_pasaaltas(i,j,M,N,D_0_p):
    D = np.sqrt((i-M)**2 + (j-N)**2)
    if(D <= D_0_p):
        return 0.0
    else:
        return 1.0

filter_pasaaltas = np.zeros((tamano_x,tamano_y))
for i in range(len(filter_pasaaltas)):
    for j in range(len(filter_pasaaltas[0])):
        filter_pasaaltas[i,j] = filtro_pasaaltas(i,j,M,N,D_0_p)
imagen_pasaaltas_tot = np.zeros((tamano_x,tamano_y))

###########################################

C = 10.0 #Constante de enfatizacion




imagen_butterworth = deepcopy(imagen_fourier)
imagen_pasaaltas = deepcopy(imagen_fourier)
imagen_C = deepcopy(imagen)
imagen_F = deepcopy(imagen)
imagen_CF = deepcopy(imagen)
imagen_laplace = deepcopy(imagen)
imagen_mlaplace = deepcopy(imagen)
imagen_mmedia = deepcopy(imagen)
imagen_norte = deepcopy(imagen)
imagen_este = deepcopy(imagen)
imagen_dir = deepcopy(imagen)
imagen_enfat = deepcopy(imagen)
imagen_robert = deepcopy(imagen)
imagen_mascara1 = deepcopy(imagen)

for i in range(1,len(imagen)-1):
    for j in range(1,len(imagen[0])-1):
        imagen_C[i,j] = (-1.0*imagen[i-1,j-1] + 0*imagen[i,j-1] + 1.0*imagen[i+1,j-1] - 2.0*imagen[i-1,j] + 0*imagen[i,j] + 2.0*imagen[i+1,j] -1.0*imagen[i-1,j+1] + 0*imagen[i,j+1] + 1.0*imagen[i+1,j+1])/9
        imagen_F[i,j] = (-1.0*imagen[i-1,j-1] - 2.0*imagen[i,j-1] - 1.0*imagen[i+1,j-1] + 0*imagen[i-1,j] + 0*imagen[i,j] + 0*imagen[i+1,j] +1.0*imagen[i-1,j+1] + 2.0*imagen[i,j+1] + 1.0*imagen[i+1,j+1])/9
        imagen_CF[i,j] = np.sqrt(imagen_C[i,j]**2 + imagen_F[i,j]**2)
        imagen_laplace[i,j] = (0*imagen[i-1,j-1] + 1.0*imagen[i,j-1] + 0*imagen[i+1,j-1] + 1.0*imagen[i-1,j] - 4.0*imagen[i,j] + 1.0*imagen[i+1,j] + 0*imagen[i-1,j+1] + 1.0*imagen[i,j+1] + 0*imagen[i+1,j+1])
        imagen_mlaplace[i,j] = (0*imagen[i-1,j-1] - 1.0*imagen[i,j-1] + 0*imagen[i+1,j-1] - 1.0*imagen[i-1,j] + 5.0*imagen[i,j] - 1.0*imagen[i+1,j] + 0*imagen[i-1,j+1] - 1.0*imagen[i,j+1] + 0*imagen[i+1,j+1])
        imagen_mmedia[i,j] = (-1.0*imagen[i-1,j-1] - 1.0*imagen[i,j-1] - 1.0*imagen[i+1,j-1] - 1.0*imagen[i-1,j] + 8.0*imagen[i,j] - 1.0*imagen[i+1,j] - 1.0*imagen[i-1,j+1] - 1.0*imagen[i,j+1] - 1.0*imagen[i+1,j+1])/9
        imagen_enfat[i,j] = (C-1.0)*imagen[i,j] + imagen_mmedia[i,j] 
        imagen_norte[i,j] = (1.0*imagen[i-1,j-1] + 1.0*imagen[i,j-1] + 1.0*imagen[i+1,j-1] + 1.0*imagen[i-1,j] - 2.0*imagen[i,j] + 1.0*imagen[i+1,j] - 1.0*imagen[i-1,j+1] - 1.0*imagen[i,j+1] - 1.0*imagen[i+1,j+1])
        imagen_este[i,j] = (-1.0*imagen[i-1,j-1] + 1.0*imagen[i,j-1] + 1.0*imagen[i+1,j-1] - 1.0*imagen[i-1,j] - 2.0*imagen[i,j] + 1.0*imagen[i+1,j] - 1.0*imagen[i-1,j+1] + 1.0*imagen[i,j+1] + 1.0*imagen[i+1,j+1])
        imagen_dir[i,j] = imagen_norte[i,j] + imagen_este[i,j]
        imagen_robert[i,j] = (np.abs(1.0*imagen[i,j] - 1.0*imagen[i+1,j+1]) + np.abs(1.0*imagen[i+1,j] - 1.0*imagen[i,j+1]))
        imagen_mascara1[i,j] = (1.0*imagen[i-1,j-1] + 4.0*imagen[i,j-1] - 2.0*imagen[i+1,j-1] + 3.0*imagen[i-1,j] + 0.0*imagen[i,j] - 3.0*imagen[i+1,j] + 2.0*imagen[i-1,j+1] - 4.0*imagen[i,j+1] - 1.0*imagen[i+1,j+1])
        
      
for i in range(len(imagen)):
    for j in range(len(imagen[0])):
        imagen_butterworth[i,j] = imagen_fourier[i,j]*filter_butterworth[i,j]
        imagen_pasaaltas[i,j] = imagen_fourier[i,j]*filter_pasaaltas[i,j]

imagen_butterworth_sinfou = np.fft.ifft2(imagen_butterworth) 
imagen_pasaaltas_sinfou = np.fft.ifft2(imagen_pasaaltas)
        
for i in range(len(imagen)):
    for j in range(len(imagen[0])):
        imagen_butterworth_tot[i,j] = np.sqrt(imagen_butterworth_sinfou[i,j].real**2 + imagen_butterworth_sinfou[i,j].imag**2 )
        imagen_pasaaltas_tot[i,j] = np.sqrt(imagen_pasaaltas_sinfou[i,j].real**2 + imagen_pasaaltas_sinfou[i,j].imag**2 )


plt.imshow(filter_butterworth,cmap = mapa_color)
plt.savefig("filtro_butterworth.png")
plt.clf()
plt.imshow(filter_pasaaltas,cmap = mapa_color)
plt.savefig("filtro_pasaaltas.png")
plt.clf()
plt.imshow(np.fft.ifft2(imagen_butterworth).real,cmap = mapa_color)
plt.savefig("imagen_butterworth_real.png")
plt.clf()
plt.imshow(np.fft.ifft2(imagen_pasaaltas).real,cmap = mapa_color)
plt.savefig("imagen_pasaaltas_real.png")
plt.clf()
plt.imshow(np.fft.ifft2(imagen_butterworth).imag,cmap = mapa_color)
plt.savefig("imagen_butterworth_imag.png")
plt.clf()
plt.imshow(np.fft.ifft2(imagen_pasaaltas).imag,cmap = mapa_color)
plt.savefig("imagen_pasaaltas_imag.png")
plt.clf()
plt.imshow(imagen_butterworth_tot.real,cmap = mapa_color)
plt.savefig("imagen_butterworth.png")
plt.clf()
plt.imshow(imagen_pasaaltas_tot.real,cmap = mapa_color)
plt.savefig("imagen_pasaaltas.png")
plt.clf()
plt.imshow(imagen,cmap = mapa_color)
plt.savefig("imagen.png")
plt.clf()
plt.imshow(imagen_C,cmap = mapa_color)
plt.savefig("imagen_filtrada_C.png")
plt.clf()
plt.imshow(imagen_F,cmap = mapa_color)
plt.savefig("imagen_filtrada_F.png")
plt.clf()
plt.imshow(imagen_CF,cmap = mapa_color)
plt.savefig("imagen_filtrada_CF.png")
plt.clf()
plt.imshow(imagen_laplace,cmap = mapa_color)
plt.savefig("imagen_filtrada_laplace.png")
plt.clf()
plt.imshow(imagen_mlaplace,cmap = mapa_color)
plt.savefig("imagen_filtrada_laplace_menos.png")
plt.clf()
plt.imshow(imagen_mmedia,cmap = mapa_color)
plt.savefig("imagen_filtrada_menos_media.png")
plt.clf()
plt.imshow(imagen_norte,cmap = mapa_color)
plt.savefig("imagen_filtrada_norte.png")
plt.clf()
plt.imshow(imagen_este,cmap = mapa_color)
plt.savefig("imagen_filtrada_este.png")
plt.clf()
plt.imshow(imagen_dir,cmap = mapa_color)
plt.savefig("imagen_filtrada_dir.png")
plt.clf()
plt.imshow(imagen_enfat,cmap = mapa_color)
plt.savefig("imagen_filtrada_enfatizacion.png")
plt.clf()
plt.imshow(imagen_robert,cmap = mapa_color)
plt.savefig("imagen_filtrada_robert.png")
plt.clf()
plt.imshow(imagen_mascara1,cmap = mapa_color)
plt.savefig("imagen_filtrada_mascara1.png")
plt.clf()
"""