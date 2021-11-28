import numpy as np
import matplotlib.pyplot as plt

archivo_HA = np.genfromtxt("hidroxiapatita.txt")
archivo_Triox =  np.genfromtxt("Trioxido.txt")
archivo_Ox =  np.genfromtxt("Oxalato.txt")

densidad_HA = 3.16 #g/cm3
densidad_Triox = 3.961 #g/cm3
densidad_Ox = 2.0 #g/cm3

Energia_HA = 1000*np.array(archivo_HA[:,0])
mu_HA = densidad_HA*np.array(archivo_HA[:,1])
Energia_Triox = 1000*np.array(archivo_Triox[:,0])
mu_Triox = densidad_Triox*np.array(archivo_Triox[:,1])
Energia_Ox = 1000*np.array(archivo_Ox[:,0])
mu_Ox = densidad_Ox*np.array(archivo_Ox[:,1])

plt.plot(Energia_HA,mu_HA, label = "HAP")
plt.plot(Energia_Triox,mu_Triox, label = "ALOX")
plt.plot(Energia_Ox,mu_Ox, label = "COX")
plt.xlabel("Energia (keV)")
plt.ylabel(r"$\mu (E)$ (1/cm)")
plt.xscale("log")
plt.yscale("log")
plt.title("Coeficiente de atenuacion lineal de HAP, COX y ALOX")
plt.grid(b=True, linestyle="--")
plt.legend()
plt.savefig("atenuacion.png")


