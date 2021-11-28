import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate

archivo_HA = np.genfromtxt("hidroxiapatita.txt")
archivo_Triox =  np.genfromtxt("Trioxido.txt")
archivo_Ox =  np.genfromtxt("Oxalato.txt")
archivo_breast =  np.genfromtxt("tissue.txt")
archivo_PMMA =  np.genfromtxt("PMMA.txt")


densidad_HA = 3.16 #g/cm3
densidad_Triox = 3.961 #g/cm3
densidad_Ox = 2.0 #g/cm3
densidad_breast = 1.041 #g/cm3
densidad_PMMA = 1.18 #g/cm3

etiquetas = ['5','6','8','10','15','20','30']
etiquetas_y = ['10','20','30']

Energia_HA = 1000*np.array(archivo_HA[:,0])
mu_HA = 100*densidad_HA*np.array(archivo_HA[:,1])
Energia_Triox = 1000*np.array(archivo_Triox[:,0])
mu_Triox = 100*densidad_Triox*np.array(archivo_Triox[:,1])
Energia_Ox = 1000*np.array(archivo_Ox[:,0])
mu_Ox = 100*densidad_Ox*np.array(archivo_Ox[:,1])
Energia_breast = 1000*np.array(archivo_breast[:,0])
mu_breast = 100*densidad_breast*np.array(archivo_breast[:,1])
Energia_PMMA = 1000*np.array(archivo_PMMA[:,0])
mu_PMMA = 100*densidad_PMMA*np.array(archivo_PMMA[:,1])

plt.plot(Energia_HA,mu_HA, label = "HA")
plt.plot(Energia_Triox,mu_Triox, label = r"$Al_2O_3$")
plt.plot(Energia_Ox,mu_Ox, label = r"$CaC_2O_4$")
plt.plot(Energia_PMMA,mu_PMMA, label = "PMMA")
plt.plot(Energia_breast,mu_breast, label = "Breast Tissue")
plt.xlabel("Photon Energy (keV)")
plt.ylabel(r"$\mu$ $(1/m)$")
plt.xscale("log")
plt.yscale("log")
plt.xticks(Energia_HA,etiquetas)
plt.title("Linear Attenuation Coefficients")
plt.grid(b=True, linestyle="--")
plt.legend()
plt.savefig("atenuacion_todos.png")
plt.clf()


plt.clf()

plt.plot(Energia_HA,mu_HA/mu_breast, label = "HA/B.Tissue")
plt.plot(Energia_Triox,mu_Triox/mu_breast, label = r"$Al_2O_3$/B.Tissue")
plt.plot(Energia_Ox,mu_Ox/mu_breast, label = r"$CaC_2O_4$/B.Tissue")
plt.xlabel("Photon Energy (keV)")
plt.ylabel(r"$\mu/\mu_{B.Tissue}$")
plt.xscale("log")
plt.yscale("log")
plt.xticks(Energia_HA,etiquetas)
plt.yticks([10,20,30],etiquetas_y)
plt.title("Linear Attenuation Coefficients relative to Breast Tissue")
plt.grid(b=True, linestyle="--")
plt.legend()
plt.savefig("atenuacion_sobre_breast.png")


