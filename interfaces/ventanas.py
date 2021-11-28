import tkinter as tk
import numpy as np
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
from tkinter import ttk
import matplotlib.pyplot as plt
from copy import copy, deepcopy
from tkinter.filedialog import *
from skimage import data
from skimage import measure
import scipy.ndimage as ndimage


imagen = 0
nombre = 0
color_imagen= "CMRmap"
senal_global = 0
senal_estado = 0
senal_gen = 0


class Ventana:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.geometry('1000x800')
        self.frame = tk.Frame(self.ventana, width= 200, height=100)
        self.frame.pack()
        self.frame.place(x=100, y=100)

        self.frame_titulo = tk.Frame(self.ventana)         
        self.frame_titulo.pack()
        self.frame_titulo.place(x=500, y=50)
        titulo = tk.Label(self.frame_titulo, text="Menu principal", font=("Helvetica", 16))
        titulo.pack()


        self.frame_boton_ventana_1 = tk.Frame(self.ventana)
        self.boton_ventana_1 = tk.Button(self.frame_boton_ventana_1, text = 'Crear .in', width = 15, command = self.Aventana1)
        self.boton_ventana_1.pack()
        self.frame_boton_ventana_1.pack()
        self.frame_boton_ventana_1.place(x=300, y=600)

        self.frame_boton_ventana_2 = tk.Frame(self.ventana)
        self.boton_ventana_2 = tk.Button(self.frame_boton_ventana_2, text = 'Calculo de CNR', width = 15, command = self.Aventana2)
        self.boton_ventana_2.pack()
        self.frame_boton_ventana_2.pack()
        self.frame_boton_ventana_2.place(x=500, y=600)


        self.frame_cerrar = tk.Frame(self.ventana)
        self.boton_cerrar = tk.Button(self.frame_cerrar, text = 'Cerrar', width = 15, command = self.close_windows)
        self.boton_cerrar.pack()
        self.frame_cerrar.pack()
        self.frame_cerrar.place(x=700, y=600)


    def close_windows(self):
        self.ventana.destroy()


    def Aventana1(self):
        self.nueva_ventana = tk.Toplevel(self.ventana)
        self.app = Ventana1(self.nueva_ventana)


    def Aventana2(self):
        self.nueva_ventana = tk.Toplevel(self.ventana)
        self.app = Ventana2(self.nueva_ventana)


         
class Ventana1:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.geometry('1000x800')

        self.frame_titulo = tk.Frame(self.ventana)         
        self.frame_titulo.pack()
        self.frame_titulo.place(x=400, y=50)
        titulo = tk.Label(self.frame_titulo, text="Creacion de archivo .in", font=("Helvetica", 16))
        titulo.pack()

        self.frame_titulo1 = tk.Frame(self.ventana)         
        self.frame_titulo1.pack()
        self.frame_titulo1.place(x=100+50, y=100)
        titulo_1 = tk.Label(self.frame_titulo1, text="Nombre del archivo:", font=("Helvetica", 10))
        titulo_1.pack()
        self.frame_nombre_in = tk.Frame(self.ventana)         
        self.frame_nombre_in.pack()
        self.frame_nombre_in.place(x=100+50, y=120)
        self.entry_nombre_in = ttk.Entry(self.frame_nombre_in, width=15)
        self.entry_nombre_in.pack()

        self.frame_titulo1_1 = tk.Frame(self.ventana)         
        self.frame_titulo1_1.pack()
        self.frame_titulo1_1.place(x=300+50, y=100)
        titulo_1_1 = tk.Label(self.frame_titulo1_1, text="Nombre geometria:", font=("Helvetica", 10))
        titulo_1_1.pack()
        self.frame_nombre_geom = tk.Frame(self.ventana)         
        self.frame_nombre_geom.pack()
        self.frame_nombre_geom.place(x=300+50, y=120)
        self.entry_nombre_geom = ttk.Entry(self.frame_nombre_geom, width=15)
        self.entry_nombre_geom.pack()

        self.frame_titulo1_2 = tk.Frame(self.ventana)         
        self.frame_titulo1_2.pack()
        self.frame_titulo1_2.place(x=500+50, y=100)
        titulo_1_2 = tk.Label(self.frame_titulo1_2, text="Geom. paralela:", font=("Helvetica", 10))
        titulo_1_2.pack()
        self.frame_nombre_paral = tk.Frame(self.ventana)         
        self.frame_nombre_paral.pack()
        self.frame_nombre_paral.place(x=500+50, y=120)
        self.entry_nombre_paral = ttk.Entry(self.frame_nombre_paral, width=15)
        self.entry_nombre_paral.pack()

        self.frame_titulo2 = tk.Frame(self.ventana)         
        self.frame_titulo2.pack()
        self.frame_titulo2.place(x=700+50, y=100)
        titulo_2 = tk.Label(self.frame_titulo2, text="Extension:", font=("Helvetica", 10))
        titulo_2.pack()
        self.frame_nombre_ext = tk.Frame(self.ventana)         
        self.frame_nombre_ext.pack()
        self.frame_nombre_ext.place(x=700+50, y=120)
        self.entry_nombre_ext = ttk.Entry(self.frame_nombre_ext, width=15)
        self.entry_nombre_ext.pack()

        self.frame_titulo3 = tk.Frame(self.ventana)         
        self.frame_titulo3.pack()
        self.frame_titulo3.place(x=425, y=140)
        titulo_3 = tk.Label(self.frame_titulo3, text="Fuente de particulas", font=("Helvetica", 10))
        titulo_3.pack()

        self.frame_titulo4 = tk.Frame(self.ventana)         
        self.frame_titulo4.pack()
        self.frame_titulo4.place(x=65+335+50-100, y=175)
        titulo_4 = tk.Label(self.frame_titulo4, text="Particula:", font=("Helvetica", 10))
        titulo_4.pack()
        self.frame_dudas_part = tk.Frame(self.ventana)
        self.dudas_part = tk.Button(self.frame_dudas_part, text = '?', width = 1, command = self.ayuda_particulas)
        self.dudas_part.pack()
        self.frame_dudas_part.pack()
        self.frame_dudas_part.place(x=140+335+50-100, y=170)
        self.frame_particula = tk.Frame(self.ventana)         
        self.frame_particula.pack()
        self.frame_particula.place(x=65+335+50-100, y=210)
        self.entry_particula = ttk.Entry(self.frame_particula, width=15)
        self.entry_particula.pack()

        self.frame_titulo4_1 = tk.Frame(self.ventana)         
        self.frame_titulo4_1.pack()
        self.frame_titulo4_1.place(x=65+335+50+100, y=175)
        titulo_4_1 = tk.Label(self.frame_titulo4_1, text="Numero de particulas:", font=("Helvetica", 10))
        titulo_4_1.pack()
        self.frame_particula_num = tk.Frame(self.ventana)         
        self.frame_particula_num.pack()
        self.frame_particula_num.place(x=65+335+50+100, y=210)
        self.entry_particula_num = ttk.Entry(self.frame_particula_num, width=15)
        self.entry_particula_num.pack()

        self.frame_titulo5 = tk.Frame(self.ventana)         
        self.frame_titulo5.pack()
        self.frame_titulo5.place(x=65+335+50, y=175+100)
        titulo_5 = tk.Label(self.frame_titulo5, text="Energia max:", font=("Helvetica", 10))
        titulo_5.pack()
        self.frame_dudas_energia = tk.Frame(self.ventana)
        self.dudas_energia = tk.Button(self.frame_dudas_energia, text = '?', width = 1, command = self.ayuda_energias)
        self.dudas_energia.pack()
        self.frame_dudas_energia.pack()
        self.frame_dudas_energia.place(x=140+335+20+50, y=170+100)
        self.frame_energia = tk.Frame(self.ventana)         
        self.frame_energia.pack()
        self.frame_energia.place(x=65+335+50, y=210+100)
        self.entry_energia = ttk.Entry(self.frame_energia, width=17)
        self.entry_energia.pack()

        self.frame_titulo6 = tk.Frame(self.ventana)         
        self.frame_titulo6.pack()
        self.frame_titulo6.place(x=65+335+50, y=175+200)
        titulo_6 = tk.Label(self.frame_titulo6, text="Posicion:", font=("Helvetica", 10))
        titulo_6.pack()
        self.frame_dudas_posicion = tk.Frame(self.ventana)
        self.dudas_posicion = tk.Button(self.frame_dudas_posicion, text = '?', width = 1, command = self.ayuda_posicion)
        self.dudas_posicion.pack()
        self.frame_dudas_posicion.pack()
        self.frame_dudas_posicion.place(x=140+335-5+50, y=170+200)
        self.frame_posicion_x = tk.Frame(self.ventana)         
        self.frame_posicion_x.pack()
        self.frame_posicion_x.place(x=65+335-100, y=210+200)
        self.entry_posicion_x = ttk.Entry(self.frame_posicion_x, width=10)
        self.entry_posicion_x.pack()
        self.frame_titulo_posicion_x = tk.Frame(self.ventana)         
        self.frame_titulo_posicion_x.pack()
        self.frame_titulo_posicion_x.place(x=65+335-100, y=210+200+20)
        titulo_posicion_x = tk.Label(self.frame_titulo_posicion_x, text="Posicion en x", font=("Helvetica", 10))
        titulo_posicion_x.pack()
        self.frame_posicion_y = tk.Frame(self.ventana)         
        self.frame_posicion_y.pack()
        self.frame_posicion_y.place(x=65+335+50, y=210+200)
        self.entry_posicion_y = ttk.Entry(self.frame_posicion_y, width=10)
        self.entry_posicion_y.pack()
        self.frame_titulo_posicion_y = tk.Frame(self.ventana)         
        self.frame_titulo_posicion_y.pack()
        self.frame_titulo_posicion_y.place(x=65+335+50, y=210+200+20)
        titulo_posicion_y = tk.Label(self.frame_titulo_posicion_y, text="Posicion en y", font=("Helvetica", 10))
        titulo_posicion_y.pack()
        self.frame_posicion_z = tk.Frame(self.ventana)         
        self.frame_posicion_z.pack()
        self.frame_posicion_z.place(x=65+335+100+100, y=210+200)
        self.entry_posicion_z = ttk.Entry(self.frame_posicion_z, width=10)
        self.entry_posicion_z.pack()
        self.frame_titulo_posicion_z = tk.Frame(self.ventana)         
        self.frame_titulo_posicion_z.pack()
        self.frame_titulo_posicion_z.place(x=65+335+100+100, y=210+200+20)
        titulo_posicion_z = tk.Label(self.frame_titulo_posicion_z, text="Posicion en z", font=("Helvetica", 10))
        titulo_posicion_z.pack()

        self.frame_titulo7 = tk.Frame(self.ventana)         
        self.frame_titulo7.pack()
        self.frame_titulo7.place(x=65+335+50, y=175+300)
        titulo_7 = tk.Label(self.frame_titulo7, text="Propiedades del haz:", font=("Helvetica", 10))
        titulo_7.pack()
        self.frame_dudas_haz = tk.Frame(self.ventana)
        self.dudas_haz = tk.Button(self.frame_dudas_haz, text = '?', width = 1, command = self.ayuda_haz)
        self.dudas_haz.pack()
        self.frame_dudas_haz.pack()
        self.frame_dudas_haz.place(x=140+335+70+50, y=170+300)
        self.frame_haz_x = tk.Frame(self.ventana)         
        self.frame_haz_x.pack()
        self.frame_haz_x.place(x=65+335-150, y=210+300)
        self.entry_haz_x = ttk.Entry(self.frame_haz_x, width=15)
        self.entry_haz_x.pack()
        self.frame_titulo_haz_x = tk.Frame(self.ventana)         
        self.frame_titulo_haz_x.pack()
        self.frame_titulo_haz_x.place(x=65+335-150, y=210+300+20)
        titulo_haz_x = tk.Label(self.frame_titulo_haz_x, text="Componente x:", font=("Helvetica", 10))
        titulo_haz_x.pack()
        self.frame_haz_y = tk.Frame(self.ventana)         
        self.frame_haz_y.pack()
        self.frame_haz_y.place(x=65+335, y=210+300)
        self.entry_haz_y = ttk.Entry(self.frame_haz_y, width=15)
        self.entry_haz_y.pack()
        self.frame_titulo_haz_y = tk.Frame(self.ventana)         
        self.frame_titulo_haz_y.pack()
        self.frame_titulo_haz_y.place(x=65+335, y=210+300+20)
        titulo_haz_y = tk.Label(self.frame_titulo_haz_y, text="Componente y:", font=("Helvetica", 10))
        titulo_haz_y.pack()
        self.frame_haz_z = tk.Frame(self.ventana)         
        self.frame_haz_z.pack()
        self.frame_haz_z.place(x=65+335+150, y=210+300)
        self.entry_haz_z = ttk.Entry(self.frame_haz_z, width=15)
        self.entry_haz_z.pack()
        self.frame_titulo_haz_z = tk.Frame(self.ventana)         
        self.frame_titulo_haz_z.pack()
        self.frame_titulo_haz_z.place(x=65+335+150, y=210+300+20)
        titulo_haz_z = tk.Label(self.frame_titulo_haz_z, text="Componente z:", font=("Helvetica", 10))
        titulo_haz_z.pack()
        self.frame_haz_deg = tk.Frame(self.ventana)         
        self.frame_haz_deg.pack()
        self.frame_haz_deg.place(x=65+335+300, y=210+300)
        self.entry_haz_deg = ttk.Entry(self.frame_haz_deg, width=15)
        self.entry_haz_deg.pack()
        self.frame_titulo_haz_deg = tk.Frame(self.ventana)         
        self.frame_titulo_haz_deg.pack()
        self.frame_titulo_haz_deg.place(x=65+335+300, y=210+300+20)
        titulo_haz_deg = tk.Label(self.frame_titulo_haz_deg, text="Ang. apertura:", font=("Helvetica", 10))
        titulo_haz_deg.pack()

        self.frame_titulo8 = tk.Frame(self.ventana)         
        self.frame_titulo8.pack()
        self.frame_titulo8.place(x=65+335+50-50, y=175+400)
        titulo_8 = tk.Label(self.frame_titulo8, text="Espectro:", font=("Helvetica", 10))
        titulo_8.pack()
        self.frame_dudas_espectro = tk.Frame(self.ventana)
        self.dudas_espectro = tk.Button(self.frame_dudas_espectro, text = '?', width = 1, command = self.ayuda_espectro)
        self.dudas_espectro.pack()
        self.frame_dudas_espectro.pack()
        self.frame_dudas_espectro.place(x=140+335+50-50, y=170+400)
        self.frame_mostrar_espectro = tk.Frame(self.ventana)
        self.mostrar_espectro = tk.Button(self.frame_mostrar_espectro, text = 'Ver espectro', width = 12, command = self.mostrar_espectro)
        self.mostrar_espectro.pack()
        self.frame_mostrar_espectro.pack()
        self.frame_mostrar_espectro.place(x=65+335+20+50+50+50-50, y=170+400)
        self.frame_espectro = tk.Frame(self.ventana)         
        self.frame_espectro.pack()
        self.frame_espectro.place(x=65+335+50-50, y=210+400)
        self.entry_espectro = ttk.Entry(self.frame_espectro, width=32)
        self.entry_espectro.pack()
        


        self.frame_cerrar = tk.Frame(self.ventana)
        self.cerrar = tk.Button(self.frame_cerrar, text = 'Cerrar', width = 10, command = self.close_windows)
        self.cerrar.pack()
        self.frame_cerrar.pack()
        self.frame_cerrar.place(x=65+335+100, y=650)

        self.frame_generar = tk.Frame(self.ventana)
        self.generar = tk.Button(self.frame_generar, text = 'Guardar', width = 10, command = self.generar_in)
        self.generar.pack()
        self.frame_generar.pack()
        self.frame_generar.place(x=65+335, y=650)

 
    def generar_in(self):
        nombre_archivo = str(self.entry_nombre_in.get())
        extension = str(self.entry_nombre_ext.get())
        geometria = str(self.entry_nombre_geom.get())
        paralela = str(self.entry_nombre_paral.get())
        particula = str(self.entry_particula.get())
        num_particulas = str(self.entry_particula_num.get())
        energia = str(self.entry_energia.get())
        posicion_x = str(self.entry_posicion_x.get())
        posicion_y = str(self.entry_posicion_y.get())  
        posicion_z = str(self.entry_posicion_z.get())
        haz_x= str(self.entry_haz_x.get())
        haz_y= str(self.entry_haz_y.get()) 
        haz_z= str(self.entry_haz_z.get())
        haz_deg= str(self.entry_haz_deg.get())
        archivo_espectro= str(self.entry_espectro.get())

        texto = "/gamos/setParam GmAnalysisMgr:FileNameSuffix " + extension + "\n"
        texto += "/gamos/setParam GmGeometryFromText:FileName " + geometria + "\n"
        texto += "/gamos/setParam GmGeometryFromText:FileNameParallel " + paralela + " 1" + "\n"
        texto += "/gamos/geometry GmGeometryFromText" + "\n" + "/gamos/physicsList GmEMPhysics" + "\n" +  "/gamos/generator GmGenerator" + "\n" + "/run/initialize" + "\n" + "/gamos/physics/addParallelProcess " + "\n"
        texto += "/gamos/generator/addSingleParticleSource fuente " + particula + " " + energia + "*keV" + "\n"
        texto += "/gamos/generator/positionDist fuente GmGenerDistPositionPoint " + posicion_x + " " + posicion_y + " " + posicion_z + "\n"
        texto += "/gamos/generator/directionDist fuente GmGenerDistDirectionCone " + haz_x + " " + haz_y + " " + haz_z + " " + haz_deg + "*deg" + "\n"
        texto += "/gamos/generator/energyDist fuente GmGenerDistEnergyFromFile " + archivo_espectro +  " interpolate" + "\n"
        texto += "/gamos/scoring/createMFDetector doseDet mesh" + "\n" + "/gamos/setParam doseScorer:ConvergenceTester DOSE_SCORER_TESTER" + "\n" + "/gamos/scoring/addScorer2MFD doseScorer GmG4PSDoseDeposit doseDet" + "\n" + "/gamos/filter inDetectorFilter GmInMassLogicalVolumeFilter detector" + "\n" + "/gamos/scoring/addFilter2Scorer inDetectorFilter doseScorer" + "\n" + "/gamos/setParam GmPSPrinter3ddose_doseScorer:FileName 3ddose_" + extension[1:] + "\n" + "/gamos/scoring/addPrinter2Scorer GmPSPrinter3ddose doseScorer" + "\n" + "/process/msc/StepLimit Minimal" + "\n" + "/gamos/random/restoreSeeds 1000 1000" + "\n" + "/control/execute ../visVRML2FILE.in" + "\n" + "/run/beamOn " + num_particulas 

        file = open(nombre_archivo, "w")
        file.write(texto)
        file.close()       
  

    def ayuda_particulas(self):
        self.nueva_ventana = tk.Toplevel(self.ventana)
        self.app = Ventana_ayuda_particulas(self.nueva_ventana)

    def ayuda_energias(self):
        self.nueva_ventana = tk.Toplevel(self.ventana)
        self.app = Ventana_ayuda_energias(self.nueva_ventana)

    def ayuda_posicion(self):
        self.nueva_ventana = tk.Toplevel(self.ventana)
        self.app = Ventana_ayuda_posicion(self.nueva_ventana)

    def ayuda_haz(self):
        self.nueva_ventana = tk.Toplevel(self.ventana)
        self.app = Ventana_ayuda_haz(self.nueva_ventana)

    def ayuda_espectro(self):
        self.nueva_ventana = tk.Toplevel(self.ventana)
        self.app = Ventana_ayuda_espectro(self.nueva_ventana)

    def mostrar_espectro(self):

        nombre_espectro = self.entry_espectro.get()
     

        self.nueva_ventana = tk.Toplevel(self.ventana)
        self.app = Ventana_espectro(self.nueva_ventana,nombre_espectro)

    def close_windows(self):
        self.ventana.destroy()

class Ventana_ayuda_particulas:
    def __init__(self,ventana):
        self.ventana = ventana
        self.ventana.geometry('370x100')
     
        self.frame_titulo = tk.Frame(self.ventana)         
        self.frame_titulo.pack()
        self.frame_titulo.place(x=20, y=30)
        titulo = tk.Label(self.frame_titulo, text="Las particulas posibles son gamma (fotones)," + "\n"  + "electrons (electrones) y positrons (positrones)", font=("Helvetica", 10))
        titulo.pack()    


    def close_windows(self):
        self.ventana.destroy()

class Ventana_ayuda_energias:
    def __init__(self,ventana):
        self.ventana = ventana
        self.ventana.geometry('500x100')
     
        self.frame_titulo = tk.Frame(self.ventana)         
        self.frame_titulo.pack()
        self.frame_titulo.place(x=20, y=40)
        titulo = tk.Label(self.frame_titulo, text="En este espacio se introduce la energia maxima de las particulas", font=("Helvetica", 10))
        titulo.pack()    


    def close_windows(self):
        self.ventana.destroy()

class Ventana_ayuda_posicion:
    def __init__(self,ventana):
        self.ventana = ventana
        self.ventana.geometry('400x100')
     
        self.frame_titulo = tk.Frame(self.ventana)         
        self.frame_titulo.pack()
        self.frame_titulo.place(x=20, y=40)
        titulo = tk.Label(self.frame_titulo, text="Posicion de la fuente en el mundo en x, y, z en mm", font=("Helvetica", 10))
        titulo.pack()    


    def close_windows(self):
        self.ventana.destroy()

class Ventana_ayuda_haz:
    def __init__(self,ventana):
        self.ventana = ventana
        self.ventana.geometry('500x100')
     
        self.frame_titulo = tk.Frame(self.ventana)         
        self.frame_titulo.pack()
        self.frame_titulo.place(x=20, y=40)
        titulo = tk.Label(self.frame_titulo, text="Vector unitario de direccion del haz y apertura del cono en grados", font=("Helvetica", 10))
        titulo.pack()    


    def close_windows(self):
        self.ventana.destroy()

class Ventana_ayuda_espectro:
    def __init__(self,ventana):
        self.ventana = ventana
        self.ventana.geometry('370x100')
     
        self.frame_titulo = tk.Frame(self.ventana)         
        self.frame_titulo.pack()
        self.frame_titulo.place(x=20, y=40)
        titulo = tk.Label(self.frame_titulo, text="Espectro: Fotones por unidad de area vs Energia", font=("Helvetica", 10))
        titulo.pack()    


    def close_windows(self):
        self.ventana.destroy()

class Ventana_espectro:
    def __init__(self,ventana,nombre):
        self.ventana = ventana
        self.ventana.geometry('1035x800')
        self.frame_cerrar = tk.Frame(self.ventana)
        self.cerrar = tk.Button(self.frame_cerrar, text = "Volver", width = 10, command = self.close_windows)
        self.cerrar.pack()
        self.frame_cerrar.pack()
        self.frame_cerrar.place(x=500, y=640)

        self.frame_titulo = tk.Frame(self.ventana)         
        self.frame_titulo.pack()
        self.frame_titulo.place(x=500, y=50)
        titulo = tk.Label(self.frame_titulo, text="Espectro", font=("Helvetica", 16))
        titulo.pack()

        self.frame_p = tk.Frame(self.ventana)         
        self.frame_p.pack()
        self.frame_p.place(x=300, y=150)

        espectro = np.genfromtxt(nombre,dtype=None)
        energia_con_unidades,fluence = zip(*espectro)
        energia_con_unidades = list(energia_con_unidades)
        fluence = list(fluence)
        energia = [float(i.split('*')[0]) for i in energia_con_unidades]
      

        self.f_p = Figure(figsize=(4,4), dpi=100)
        self.a_p = self.f_p.add_subplot(111)
        self.im_p = self.a_p.plot(energia,fluence)


        canvas_p = FigureCanvasTkAgg(self.f_p, master=self.frame_p)
        canvas_p.draw()
        canvas_p.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        toolbar_p = NavigationToolbar2Tk(canvas_p, self.frame_p)
        toolbar_p.update()
        canvas_p._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        
        self.frame_titulo2 = tk.Frame(self.ventana)         
        self.frame_titulo2.pack()
        self.frame_titulo2.place(x=400, y=600)
        titulo_2 = tk.Label(self.frame_titulo2, text="Nombre de archivo:", font=("Helvetica", 16))
        titulo_2.pack()

        self.frame_nombrep = tk.Frame(self.ventana)
        self.entry_nombrep = tk.Entry(self.frame_nombrep, width=28)
        self.entry_nombrep.pack()
        self.frame_nombrep.pack()
        self.frame_nombrep.place(x=400, y=620)

        self.frame_guardar = tk.Frame(self.ventana)
        self.guardar = tk.Button(self.frame_guardar, text = "Guardar", width = 10, command = self.guardar)
        self.guardar.pack()
        self.frame_guardar.pack()
        self.frame_guardar.place(x=400, y=640)
   

    def guardar(self):
        nombre_figura = self.entry_nombrep.get()
        self.f_p.savefig(nombre_figura)
        self.entry_nombrep.delete(0, tk.END)

    def close_windows(self):
        self.ventana.destroy()


#################### Aca empieza ventana del CNR y perfiles ##############################

class Ventana2:
    def __init__(self, ventana):

        global senal_estado
        global senal_global

        self.ventana = ventana
        self.ventana.geometry('1000x800')
        
        #self.scrollbar = tk.Scrollbar(ventana)
        #self.scrollbar.pack( side = tk.RIGHT, fill = tk.Y )
        
     
        self.frame_titulo = tk.Frame(self.ventana)         
        self.frame_titulo.pack()
        self.frame_titulo.place(x=500, y=50)
        titulo = tk.Label(self.frame_titulo, text="Calculo de CNR", font=("Helvetica", 16))
        titulo.pack()

        self.frame_archivo = tk.Frame(self.ventana)
        self.info_archivo = tk.Text(self.frame_archivo, width=20, height=1)
        self.info_archivo.pack()
        self.frame_archivo.pack()
        self.frame_archivo.place(x=500, y=70)

        self.frame_buscar = tk.Frame(self.ventana)
        self.buscar = tk.Button(self.frame_buscar, text = 'Buscar archivo', width = 12, command = self.buscar_archivo)
        self.buscar.pack()
        self.frame_buscar.pack()
        self.frame_buscar.place(x=520, y=90)

        self.frame_parametros = tk.Frame(self.ventana)         
        self.frame_parametros.pack()
        self.frame_parametros.place(x=100, y=100)
        parametros_zona = tk.Label(self.frame_parametros, text="Parametros:", font=("Helvetica", 10))
        parametros_zona.pack()


        self.frame_pixel_check_s = tk.Frame(self.ventana)         
        self.frame_pixel_check_s.pack()
        self.frame_pixel_check_s.place(x=50, y=120)
        titulo_pixel_check_s = tk.Label(self.frame_pixel_check_s, text="Senal click:", font=("Helvetica", 10))
        titulo_pixel_check_s.pack()
        self.frame_caja_check_s = tk.Frame(self.ventana)         
        self.frame_caja_check_s.pack()
        self.frame_caja_check_s.place(x=50, y=140)
        self.check_val_s = tk.BooleanVar(self.ventana)
        self.check_s = ttk.Checkbutton(self.frame_caja_check_s, variable=self.check_val_s, command = self.checkbox_click_s)
        self.check_s.pack()

        self.estado_check_s = False


        self.frame_pixel_check_b = tk.Frame(self.ventana)         
        self.frame_pixel_check_b.pack()
        self.frame_pixel_check_b.place(x=140, y=120)
        titulo_pixel_check_b = tk.Label(self.frame_pixel_check_b, text="Fondo click:", font=("Helvetica", 10))
        titulo_pixel_check_b.pack()
        self.frame_caja_check_b = tk.Frame(self.ventana)         
        self.frame_caja_check_b.pack()
        self.frame_caja_check_b.place(x=140, y=140)
        self.check_val_b = tk.BooleanVar(self.ventana)
        self.check_b = ttk.Checkbutton(self.frame_caja_check_b, variable=self.check_val_b, command = self.checkbox_click_b)
        self.check_b.pack()

        self.estado_check_b = False


 
        #Background
        self.frame_titulob = tk.Frame(self.ventana)         
        self.frame_titulob.pack()
        self.frame_titulob.place(x=100, y=120+40)
        titulo_b = tk.Label(self.frame_titulob, text="Background", font=("Helvetica", 10))
        titulo_b.pack()
       
        self.frame_titulo1 = tk.Frame(self.ventana)         
        self.frame_titulo1.pack()
        self.frame_titulo1.place(x=50, y=140+40)
        titulo_1 = tk.Label(self.frame_titulo1, text="Inicio x:", font=("Helvetica", 10))
        titulo_1.pack()
        self.frame_background_inic_x = tk.Frame(self.ventana)         
        self.frame_background_inic_x.pack()
        self.frame_background_inic_x.place(x=50, y=160+40)
        self.entry_background_inic_x = ttk.Entry(self.frame_background_inic_x, width=10)
        self.entry_background_inic_x.pack()
        self.frame_titulo2 = tk.Frame(self.ventana)         
        self.frame_titulo2.pack()
        self.frame_titulo2.place(x=140, y=140+40)
        titulo_2 = tk.Label(self.frame_titulo2, text="Final x:", font=("Helvetica", 10))
        titulo_2.pack()
        self.frame_background_final_x = tk.Frame(self.ventana)         
        self.frame_background_final_x.pack()
        self.frame_background_final_x.place(x=140, y=160+40)
        self.entry_background_final_x = ttk.Entry(self.frame_background_final_x, width=10)
        self.entry_background_final_x.pack()
        self.frame_titulo3 = tk.Frame(self.ventana)         
        self.frame_titulo3.pack()
        self.frame_titulo3.place(x=50, y=180+40)
        titulo_3 = tk.Label(self.frame_titulo3, text="Inicio y:", font=("Helvetica", 10))
        titulo_3.pack()
        self.frame_background_inic_y = tk.Frame(self.ventana)         
        self.frame_background_inic_y.pack()
        self.frame_background_inic_y.place(x=50, y=200+40)
        self.entry_background_inic_y = ttk.Entry(self.frame_background_inic_y, width=10)
        self.entry_background_inic_y.pack()
        self.frame_titulo4 = tk.Frame(self.ventana)         
        self.frame_titulo4.pack()
        self.frame_titulo4.place(x=140, y=180+40)
        titulo_4 = tk.Label(self.frame_titulo4, text="Final y:", font=("Helvetica", 10))
        titulo_4.pack()
        self.frame_background_final_y = tk.Frame(self.ventana)         
        self.frame_background_final_y.pack()
        self.frame_background_final_y.place(x=140, y=200+40)
        self.entry_background_final_y = ttk.Entry(self.frame_background_final_y, width=10)
        self.entry_background_final_y.pack()

        #Senal
        self.frame_titulos = tk.Frame(self.ventana)         
        self.frame_titulos.pack()
        self.frame_titulos.place(x=100, y=220+40)
        titulo_s = tk.Label(self.frame_titulos, text="Senal", font=("Helvetica", 10))
        titulo_s.pack()
       
        self.frame_titulo5 = tk.Frame(self.ventana)         
        self.frame_titulo5.pack()
        self.frame_titulo5.place(x=50, y=240+40)
        titulo_5 = tk.Label(self.frame_titulo5, text="Inicio x:", font=("Helvetica", 10))
        titulo_5.pack()
        self.frame_senal_inic_x = tk.Frame(self.ventana)         
        self.frame_senal_inic_x.pack()
        self.frame_senal_inic_x.place(x=50, y=260+40)
        self.entry_senal_inic_x = ttk.Entry(self.frame_senal_inic_x, width=10)
        self.entry_senal_inic_x.pack()
        self.frame_titulo6 = tk.Frame(self.ventana)         
        self.frame_titulo6.pack()
        self.frame_titulo6.place(x=140, y=240+40)
        titulo_6 = tk.Label(self.frame_titulo6, text="Final x:", font=("Helvetica", 10))
        titulo_6.pack()
        self.frame_senal_final_x = tk.Frame(self.ventana)         
        self.frame_senal_final_x.pack()
        self.frame_senal_final_x.place(x=140, y=260+40)
        self.entry_senal_final_x = ttk.Entry(self.frame_senal_final_x, width=10)
        self.entry_senal_final_x.pack()
        self.frame_titulo7 = tk.Frame(self.ventana)         
        self.frame_titulo7.pack()
        self.frame_titulo7.place(x=50, y=280+40)
        titulo_7 = tk.Label(self.frame_titulo7, text="Inicio y:", font=("Helvetica", 10))
        titulo_7.pack()
        self.frame_senal_inic_y = tk.Frame(self.ventana)         
        self.frame_senal_inic_y.pack()
        self.frame_senal_inic_y.place(x=50, y=300+40)
        self.entry_senal_inic_y = ttk.Entry(self.frame_senal_inic_y, width=10)
        self.entry_senal_inic_y.pack()
        self.frame_titulo8 = tk.Frame(self.ventana)         
        self.frame_titulo8.pack()
        self.frame_titulo8.place(x=140, y=280+40)
        titulo_8 = tk.Label(self.frame_titulo8, text="Final y:", font=("Helvetica", 10))
        titulo_8.pack()
        self.frame_senal_final_y = tk.Frame(self.ventana)         
        self.frame_senal_final_y.pack()
        self.frame_senal_final_y.place(x=140, y=300+40)
        self.entry_senal_final_y = ttk.Entry(self.frame_senal_final_y, width=10)
        self.entry_senal_final_y.pack()


        self.frame_titulo9 = tk.Frame(self.ventana)         
        self.frame_titulo9.pack()
        self.frame_titulo9.place(x=100, y=320+40)
        titulo_9 = tk.Label(self.frame_titulo9, text="Sensibilidad:", font=("Helvetica", 10))
        titulo_9.pack()
        self.frame_caja = tk.Frame(self.ventana)         
        self.frame_caja.pack()
        self.frame_caja.place(x=100, y=340+40)
        self.entry_num_desvest_b = ttk.Entry(self.frame_caja, width=10)
        self.entry_num_desvest_b.pack()

        self.frame_titulo10 = tk.Frame(self.ventana)         
        self.frame_titulo10.pack()
        self.frame_titulo10.place(x=100, y=360+40)
        titulo_10 = tk.Label(self.frame_titulo10, text="CNR:", font=("Helvetica", 10))
        titulo_10.pack()

        self.frame_CNR = tk.Frame(self.ventana)
        self.info_CNR = tk.Text(self.frame_CNR, width=10, height=1)
        self.info_CNR.pack()
        self.frame_CNR.pack()
        self.frame_CNR.place(x=100, y=380+40)

        self.frame_titulo11 = tk.Frame(self.ventana)         
        self.frame_titulo11.pack()
        self.frame_titulo11.place(x=70, y=400+40)
        titulo_11 = tk.Label(self.frame_titulo11, text="Paleta de colores:", font=("Helvetica", 10))
        titulo_11.pack()

        self.lista_colores = tk.Listbox(self.ventana, width=20, height=10)
        self.lista_colores.place(x=65, y= 420+50)
        self.colores = ['viridis', 'plasma', 'inferno', 'magma', 'cividis','Greys', 'Purples', 'Blues', 'Greens', 'Oranges', 'Reds','YlOrBr', 'YlOrRd', 'OrRd', 'PuRd', 'RdPu', 'BuPu','GnBu', 'PuBu', 'YlGnBu', 'PuBuGn', 'BuGn', 'YlGn','binary', 'gist_yarg', 'gist_gray', 'gray', 'bone', 'pink','spring', 'summer', 'autumn', 'winter', 'cool', 'Wistia','hot', 'afmhot', 'gist_heat', 'copper','PiYG', 'PRGn', 'BrBG', 'PuOr', 'RdGy', 'RdBu','RdYlBu', 'RdYlGn', 'Spectral', 'coolwarm', 'bwr', 'seismic', 'hsv','Pastel1', 'Pastel2', 'Paired', 'Accent','Dark2', 'Set1', 'Set2', 'Set3','tab10', 'tab20', 'tab20b', 'tab20c','flag', 'prism', 'ocean', 'gist_earth', 'terrain', 'gist_stern','gnuplot', 'gnuplot2', 'CMRmap', 'cubehelix', 'brg','gist_rainbow', 'rainbow', 'jet', 'nipy_spectral', 'gist_ncar',]
        
        for color in self.colores:
            self.lista_colores.insert(tk.END, color)        

        self.frame_actualizar = tk.Frame(self.ventana)
        self.actualizar = tk.Button(self.frame_actualizar, text = 'Actualizar', width = 10, command = self.actualizar_grafica)
        self.actualizar.pack()
        self.frame_actualizar.pack()
        self.frame_actualizar.place(x=90, y=560+40)

        self.frame_borrar_s = tk.Frame(self.ventana)
        self.borrar_s = tk.Button(self.frame_borrar_s, text = 'Borrar senal', width = 10, command = self.borrar_senal)
        self.borrar_s.pack()
        self.frame_borrar_s.pack()
        self.frame_borrar_s.place(x=250, y=600)

        self.frame_datos = tk.Frame(self.ventana)
        self.datos = tk.Button(self.frame_datos, text = 'Obtener datos', width = 10, command = self.obtener_datos)
        self.datos.pack()
        self.frame_datos.pack()
        self.frame_datos.place(x=350, y=600)

        self.frame_calcular_CNR = tk.Frame(self.ventana)
        self.calculo_CNR = tk.Button(self.frame_calcular_CNR, text = 'Calcular CNR', width = 10, command = self.calcular_CNR)
        self.calculo_CNR.pack()
        self.frame_calcular_CNR.pack()
        self.frame_calcular_CNR.place(x=450, y=600)

        self.frame_perfi = tk.Frame(self.ventana)
        self.perfi = tk.Button(self.frame_perfi, text = 'Perfiles', width = 10, command = self.perfil)
        self.perfi.pack()
        self.frame_perfi.pack()
        self.frame_perfi.place(x=550, y=600)

        self.frame_cerrar = tk.Frame(self.ventana)
        self.cerrar = tk.Button(self.frame_cerrar, text = 'Cerrar', width = 10, command = self.close_windows)
        self.cerrar.pack()
        self.frame_cerrar.pack()
        self.frame_cerrar.place(x=650, y=600)
        
        self.frame_tituloper = tk.Frame(self.ventana)         
        self.frame_tituloper.pack()
        self.frame_tituloper.place(x=800, y=120)
        titulo_per = tk.Label(self.frame_tituloper, text="Perfiles", font=("Helvetica", 10))
        titulo_per.pack()
       
        self.frame_titulo_perf_inic_x = tk.Frame(self.ventana)         
        self.frame_titulo_perf_inic_x.pack()
        self.frame_titulo_perf_inic_x.place(x=800, y=140)
        titulo_perf_inic_x = tk.Label(self.frame_titulo_perf_inic_x, text="Inicio x:", font=("Helvetica", 10))
        titulo_perf_inic_x.pack()
        self.frame_perf_inic_x = tk.Frame(self.ventana)         
        self.frame_perf_inic_x.pack()
        self.frame_perf_inic_x.place(x=800, y=160)
        self.entry_perf_inic_x = ttk.Entry(self.frame_perf_inic_x, width=10)
        self.entry_perf_inic_x.pack()

        self.frame_titulo_perf_final_x = tk.Frame(self.ventana)         
        self.frame_titulo_perf_final_x.pack()
        self.frame_titulo_perf_final_x.place(x=900, y=140)
        titulo_perf_final_x = tk.Label(self.frame_titulo_perf_final_x, text="Final x:", font=("Helvetica", 10))
        titulo_perf_final_x.pack()
        self.frame_perf_final_x = tk.Frame(self.ventana)         
        self.frame_perf_final_x.pack()
        self.frame_perf_final_x.place(x=900, y=160)
        self.entry_perf_final_x = ttk.Entry(self.frame_perf_final_x, width=10)
        self.entry_perf_final_x.pack()

        self.frame_titulo_perf_inic_y = tk.Frame(self.ventana)         
        self.frame_titulo_perf_inic_y.pack()
        self.frame_titulo_perf_inic_y.place(x=800, y=180)
        titulo_perf_inic_y = tk.Label(self.frame_titulo_perf_inic_y, text="Inicio y:", font=("Helvetica", 10))
        titulo_perf_inic_y.pack()
        self.frame_perf_inic_y = tk.Frame(self.ventana)         
        self.frame_perf_inic_y.pack()
        self.frame_perf_inic_y.place(x=800, y=200)
        self.entry_perf_inic_y = ttk.Entry(self.frame_perf_inic_y, width=10)
        self.entry_perf_inic_y.pack()

        self.frame_titulo_perf_final_y = tk.Frame(self.ventana)         
        self.frame_titulo_perf_final_y.pack()
        self.frame_titulo_perf_final_y.place(x=900, y=180)
        titulo_perf_final_y = tk.Label(self.frame_titulo_perf_final_y, text="Final y:", font=("Helvetica", 10))
        titulo_perf_final_y.pack()
        self.frame_perf_final_y = tk.Frame(self.ventana)         
        self.frame_perf_final_y.pack()
        self.frame_perf_final_y.place(x=900, y=200)
        self.entry_perf_final_y = ttk.Entry(self.frame_perf_final_y, width=10)
        self.entry_perf_final_y.pack()

        self.frame_vertical = tk.Frame(self.ventana)
        self.vertical = tk.Button(self.frame_vertical, text = 'Vertical', width = 8, command = self.vertical)
        self.vertical.pack()
        self.frame_vertical.pack()
        self.frame_vertical.place(x=800, y=220)

        self.frame_horizontal = tk.Frame(self.ventana)
        self.horizontal = tk.Button(self.frame_horizontal, text = 'Horizontal', width = 8, command = self.horizontal)
        self.horizontal.pack()
        self.frame_horizontal.pack()
        self.frame_horizontal.place(x=900, y=220)

        self.modo_perfil = "horizontal"

        self.frame_agregar_perf = tk.Frame(self.ventana)
        self.agregar_perf = tk.Button(self.frame_agregar_perf, text = 'Agregar', width = 8, command = self.agregar_perfil)
        self.agregar_perf.pack()
        self.frame_agregar_perf.pack()
        self.frame_agregar_perf.place(x=800, y=250)

        self.perfiles = []

        self.frame_limpiar_perf = tk.Frame(self.ventana)
        self.limpiar_perf = tk.Button(self.frame_limpiar_perf, text = 'Limpiar', width = 8, command = self.limpiar_perfil)
        self.limpiar_perf.pack()
        self.frame_limpiar_perf.pack()
        self.frame_limpiar_perf.place(x=900, y=250)

        self.frame_titulo10_1 = tk.Frame(self.ventana)         
        self.frame_titulo10_1.pack()
        self.frame_titulo10_1.place(x=800, y=280)
        titulo_10_1 = tk.Label(self.frame_titulo10_1, text="Informacion:", font=("Helvetica", 10))
        titulo_10_1.pack()

        self.frame_info = tk.Frame(self.ventana)
        self.info_info = tk.Text(self.frame_info, width=20, height=4)
        self.info_info.pack()
        self.frame_info.pack()
        self.frame_info.place(x=800, y=300)


        self.frame_tituloper_1 = tk.Frame(self.ventana)         
        self.frame_tituloper_1.pack()
        self.frame_tituloper_1.place(x=800, y=360)
        titulo_per_1 = tk.Label(self.frame_tituloper_1, text="CNR regiones", font=("Helvetica", 10))
        titulo_per_1.pack()
       
        self.frame_senal1 = tk.Frame(self.ventana)         
        self.frame_senal1.pack()
        self.frame_senal1.place(x=800, y=400)
        senal1 = tk.Label(self.frame_senal1, text="Senal 1:", font=("Helvetica", 10))
        senal1.pack()
        self.frame_senal1_calc = tk.Frame(self.ventana)         
        self.frame_senal1_calc.pack()
        self.frame_senal1_calc.place(x=800, y=420)
        self.entry_senal1_calc = ttk.Entry(self.frame_senal1_calc, width=10)
        self.entry_senal1_calc.pack()

        self.frame_senal2 = tk.Frame(self.ventana)         
        self.frame_senal2.pack()
        self.frame_senal2.place(x=900, y=400)
        senal2 = tk.Label(self.frame_senal2, text="Senal 2:", font=("Helvetica", 10))
        senal2.pack()
        self.frame_senal2_calc = tk.Frame(self.ventana)         
        self.frame_senal2_calc.pack()
        self.frame_senal2_calc.place(x=900, y=420)
        self.entry_senal2_calc = ttk.Entry(self.frame_senal2_calc, width=10)
        self.entry_senal2_calc.pack()

        self.frame_desvs1 = tk.Frame(self.ventana)         
        self.frame_desvs1.pack()
        self.frame_desvs1.place(x=800, y=440)
        desvs1 = tk.Label(self.frame_desvs1, text="Desv.1:", font=("Helvetica", 10))
        desvs1.pack()
        self.frame_desvs1_calc = tk.Frame(self.ventana)         
        self.frame_desvs1_calc.pack()
        self.frame_desvs1_calc.place(x=800, y=460)
        self.entry_desvs1_calc = ttk.Entry(self.frame_desvs1_calc, width=10)
        self.entry_desvs1_calc.pack()

        self.frame_desvs2 = tk.Frame(self.ventana)         
        self.frame_desvs2.pack()
        self.frame_desvs2.place(x=900, y=440)
        desvs2 = tk.Label(self.frame_desvs2, text="Desv.2:", font=("Helvetica", 10))
        desvs2.pack()
        self.frame_desvs2_calc = tk.Frame(self.ventana)         
        self.frame_desvs2_calc.pack()
        self.frame_desvs2_calc.place(x=900, y=460)
        self.entry_desvs2_calc = ttk.Entry(self.frame_desvs2_calc, width=10)
        self.entry_desvs2_calc.pack()

        self.frame_CNR2_calc = tk.Frame(self.ventana)
        self.CNR2_calc = tk.Button(self.frame_CNR2_calc, text = 'Calcular CNR 2', width = 12, command = self.calcular_CNR2)
        self.CNR2_calc.pack()
        self.frame_CNR2_calc.pack()
        self.frame_CNR2_calc.place(x=830, y=480)


        self.frame_titulo10_2 = tk.Frame(self.ventana)         
        self.frame_titulo10_2.pack()
        self.frame_titulo10_2.place(x=850, y=520)
        titulo_10_2 = tk.Label(self.frame_titulo10_2, text="CNR 2:", font=("Helvetica", 10))
        titulo_10_2.pack()

        self.frame_CNR_2 = tk.Frame(self.ventana)
        self.info_CNR_2 = tk.Text(self.frame_CNR_2, width=10, height=1)
        self.info_CNR_2.pack()
        self.frame_CNR_2.pack()
        self.frame_CNR_2.place(x=850, y=540)

        self.listaclick = []

    def borrar_senal(self):

        global senal_estado
        global senal_global

        senal_global = np.zeros((256,256))
        senal_estado = 0
        del self.listaclick[:]

    def checkbox_click_s(self):
        self.estado_check_s = self.check_val_s.get()

    def checkbox_click_b(self):
        self.estado_check_b = self.check_val_b.get()

    def limpiar_perfil(self):
        del self.perfiles[:]

    def vertical(self):
        self.modo_perfil = "vertical"    
        
    def horizontal(self):
        self.modo_perfil = "horizontal"      

    def buscar_archivo(self):
  
        global imagen
        global nombre

        self.frame_imagen = tk.Frame(self.ventana)         
        self.frame_imagen.pack()
        self.frame_imagen.place(x=220, y=150)

        self.info_archivo.delete("1.0", tk.END)
   
        nombre = askopenfile()

        self.info_archivo.insert("1.0", nombre)  

        imagen = np.genfromtxt(nombre)

        f = Figure(figsize=(5.7,4), dpi=100)
        a = f.add_subplot(111)
        im= a.imshow(imagen, cmap = color_imagen)
        f.colorbar(im)

        
        canvas = FigureCanvasTkAgg(f, master=self.frame_imagen)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=0)

        toolbar = NavigationToolbar2Tk(canvas, self.frame_imagen)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=0)

        

        def onclick(event):

            x = event.xdata-0.5
            y = event.ydata-0.5
            
            if(x < 0.5):
                x = -1.0

            if(y < 0.5):
                y = -1.0
           

            self.listaclick.append([int(x) + 1,int(y) + 1])
            print('%s click: button=%d, x=%d, y=%d, xdata=%f, ydata=%f' %
          ('double' if event.dblclick else 'single', event.button,
           event.x, event.y, event.xdata, event.ydata))

        canvas.mpl_connect('button_press_event', onclick)

    def actualizar_grafica(self):
       
        global color_imagen

        self.indice = self.lista_colores.curselection()[0]
        color_imagen = self.colores[self.indice]   
   
        self.frame_imagen = tk.Frame(self.ventana)         
        self.frame_imagen.pack()
        self.frame_imagen.place(x=220, y=150)  

        f = Figure(figsize=(5.7,4), dpi=100)
        a = f.add_subplot(111)
        im= a.imshow(imagen, cmap = color_imagen)
        f.colorbar(im)

        canvas = FigureCanvasTkAgg(f, master=self.frame_imagen)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        toolbar = NavigationToolbar2Tk(canvas, self.frame_imagen)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        def onclick(event):

            x = event.xdata-0.5
            y = event.ydata-0.5
            
            if(x < 0.5):
                x = -1.0

            if(y < 0.5):
                y = -1.0
           

            self.listaclick.append([int(x) + 1,int(y) + 1])
            print('%s click: button=%d, x=%d, y=%d, xdata=%f, ydata=%f' %
          ('double' if event.dblclick else 'single', event.button,
           event.x, event.y, event.xdata, event.ydata))

        canvas.mpl_connect('button_press_event', onclick)

    def calcular_CNR(self):


     
        self.info_CNR.delete("1.0", tk.END)
        self.info_info.delete("1.0", tk.END)   
 
        vec_x = []
        vec_y = []

        if(self.estado_check_s == True and self.estado_check_b == False):
         
            for i in range(1,5):
                vec_x.append(self.listaclick[-1*i][0])
                vec_y.append(self.listaclick[-1*i][1]) 
            
            texto_senal_inicial_x = np.amin(np.array(vec_x))
            texto_senal_final_x = np.amax(np.array(vec_x))
            texto_senal_inicial_y = np.amin(np.array(vec_y))
            texto_senal_final_y = np.amax(np.array(vec_y))
            texto_background_inicial_x = self.entry_background_inic_x.get()
            texto_background_inicial_y = self.entry_background_inic_y.get()
            texto_background_final_x = self.entry_background_final_x.get()
            texto_background_final_y = self.entry_background_final_y.get()

        elif(self.estado_check_b == True and self.estado_check_s == False):

            for i in range(1,5):
                vec_x.append(self.listaclick[-1*i][0])
                vec_y.append(self.listaclick[-1*i][1]) 
            
            texto_background_inicial_x = np.amin(np.array(vec_x))
            texto_background_final_x = np.amax(np.array(vec_x))
            texto_background_inicial_y = np.amin(np.array(vec_y))
            texto_background_final_y = np.amax(np.array(vec_y))
            texto_senal_inicial_x = self.entry_senal_inic_x.get()
            texto_senal_inicial_y = self.entry_senal_inic_y.get()
            texto_senal_final_x = self.entry_senal_final_x.get()
            texto_senal_final_y = self.entry_senal_final_y.get()

        elif(self.estado_check_b == True and self.estado_check_s == True):
        
            vec_x_s = []
            vec_x_b = []
            vec_y_s = []
            vec_y_b = []
          
            for i in range(1,9):
                if(i<=8 and i>=5):
                    vec_x_s.append(self.listaclick[-1*i][0])
                    vec_y_s.append(self.listaclick[-1*i][1])
                if(i<=4 and i>=1):
                    vec_x_b.append(self.listaclick[-1*i][0])
                    vec_y_b.append(self.listaclick[-1*i][1])
        
     
            texto_background_inicial_x = np.amin(np.array(vec_x_b))
            texto_background_final_x = np.amax(np.array(vec_x_b))
            texto_background_inicial_y = np.amin(np.array(vec_y_b))
            texto_background_final_y = np.amax(np.array(vec_y_b))
            texto_senal_inicial_x = np.amin(np.array(vec_x_s))
            texto_senal_final_x = np.amax(np.array(vec_x_s))
            texto_senal_inicial_y = np.amin(np.array(vec_y_s))
            texto_senal_final_y = np.amax(np.array(vec_y_s))

        else:

            texto_senal_inicial_x = self.entry_senal_inic_x.get()
            texto_senal_inicial_y = self.entry_senal_inic_y.get()
            texto_senal_final_x = self.entry_senal_final_x.get()
            texto_senal_final_y = self.entry_senal_final_y.get()
            texto_background_inicial_x = self.entry_background_inic_x.get()
            texto_background_inicial_y = self.entry_background_inic_y.get()
            texto_background_final_x = self.entry_background_final_x.get()
            texto_background_final_y = self.entry_background_final_y.get()

        num_desv_est_fondo = float(self.entry_num_desvest_b.get())
        
        senal = imagen[int(texto_senal_inicial_y):int(texto_senal_final_y),int(texto_senal_inicial_x):int(texto_senal_final_x)]
        fondo = imagen[int(texto_background_inicial_y):int(texto_background_final_y),int(texto_background_inicial_x):int(texto_background_final_x)]
  
        senal_p = deepcopy(senal)

        promedio_fondo = np.mean(fondo)
        desv_est_fondo = np.std(fondo)

        for i in range(len(senal_p)):
            for j in range(len(senal_p[0])):
                if(np.abs(senal_p[i,j] - promedio_fondo) < num_desv_est_fondo*desv_est_fondo):
                    senal_p[i,j] = 0
    
        if(senal_estado == 0):

            promedio_senal = np.sum(senal_p, dtype="float")/(np.count_nonzero(senal_p) + 0.0)
            senal_no_zero = senal_p[np.nonzero(senal_p)]
            desv_est_senal = np.std(senal_no_zero)

            CNR = (promedio_senal-promedio_fondo)/(desv_est_fondo)

            info_texto = "Promedio senal:" + str(promedio_senal) + "\n" + "Desv.senal:" + str(desv_est_senal)

            self.info_CNR.insert("1.0", str(CNR))
            self.info_info.insert("1.0", info_texto)

        elif(senal_estado == 1):
            promedio_senal = np.sum(senal_global, dtype="float")/(np.count_nonzero(senal_global) + 0.0)
            senal_no_zero = senal_global[np.nonzero(senal_global)]
            desv_est_senal = np.std(senal_no_zero)

            CNR = (promedio_senal-promedio_fondo)/(desv_est_fondo)

            info_texto = "Promedio senal:" + str(promedio_senal) + "\n" + "Desv.senal:" + str(desv_est_senal)

            self.info_CNR.insert("1.0", str(CNR))
            self.info_info.insert("1.0", info_texto)
        else:
            CNR = 99999999


    def calcular_CNR2(self):


     
        self.info_CNR_2.delete("1.0", tk.END)   
     
        senal_1 = float(self.entry_senal1_calc.get())
        senal_2 = float(self.entry_senal2_calc.get())
        desv_s1 = float(self.entry_desvs1_calc.get())        
        desv_s2 = float(self.entry_desvs2_calc.get())

        

        CNR2 = np.abs(senal_1-senal_2)/(desv_s2)

           
        self.info_CNR_2.insert("1.0", str(CNR2))



        

    def obtener_datos(self):
        
        global senal_gen

        vec_x = []
        vec_y = []

        if(self.estado_check_s == True and self.estado_check_b == False):
         
            for i in range(1,5):
                vec_x.append(self.listaclick[-1*i][0])
                vec_y.append(self.listaclick[-1*i][1]) 
            
            texto_senal_inicial_x = np.amin(np.array(vec_x))
            texto_senal_final_x = np.amax(np.array(vec_x))
            texto_senal_inicial_y = np.amin(np.array(vec_y))
            texto_senal_final_y = np.amax(np.array(vec_y))
            texto_background_inicial_x = self.entry_background_inic_x.get()
            texto_background_inicial_y = self.entry_background_inic_y.get()
            texto_background_final_x = self.entry_background_final_x.get()
            texto_background_final_y = self.entry_background_final_y.get()

        elif(self.estado_check_b == True and self.estado_check_s == False):

            for i in range(1,5):
                vec_x.append(self.listaclick[-1*i][0])
                vec_y.append(self.listaclick[-1*i][1]) 
            
            texto_background_inicial_x = np.amin(np.array(vec_x))
            texto_background_final_x = np.amax(np.array(vec_x))
            texto_background_inicial_y = np.amin(np.array(vec_y))
            texto_background_final_y = np.amax(np.array(vec_y))
            texto_senal_inicial_x = self.entry_senal_inic_x.get()
            texto_senal_inicial_y = self.entry_senal_inic_y.get()
            texto_senal_final_x = self.entry_senal_final_x.get()
            texto_senal_final_y = self.entry_senal_final_y.get()

        elif(self.estado_check_b == True and self.estado_check_s == True):
        
            vec_x_s = []
            vec_x_b = []
            vec_y_s = []
            vec_y_b = []
          
            for i in range(1,9):
                if(i<=8 and i>=5):
                    vec_x_s.append(self.listaclick[-1*i][0])
                    vec_y_s.append(self.listaclick[-1*i][1])
                if(i<=4 and i>=1):
                    vec_x_b.append(self.listaclick[-1*i][0])
                    vec_y_b.append(self.listaclick[-1*i][1])
        
     
            texto_background_inicial_x = np.amin(np.array(vec_x_b))
            texto_background_final_x = np.amax(np.array(vec_x_b))
            texto_background_inicial_y = np.amin(np.array(vec_y_b))
            texto_background_final_y = np.amax(np.array(vec_y_b))
            texto_senal_inicial_x = np.amin(np.array(vec_x_s))
            texto_senal_final_x = np.amax(np.array(vec_x_s))
            texto_senal_inicial_y = np.amin(np.array(vec_y_s))
            texto_senal_final_y = np.amax(np.array(vec_y_s))

        else:

            texto_senal_inicial_x = self.entry_senal_inic_x.get()
            texto_senal_inicial_y = self.entry_senal_inic_y.get()
            texto_senal_final_x = self.entry_senal_final_x.get()
            texto_senal_final_y = self.entry_senal_final_y.get()
            texto_background_inicial_x = self.entry_background_inic_x.get()
            texto_background_inicial_y = self.entry_background_inic_y.get()
            texto_background_final_x = self.entry_background_final_x.get()
            texto_background_final_y = self.entry_background_final_y.get()
        
        num_desv_est_fondo = float(self.entry_num_desvest_b.get())

        

        senal = imagen[int(texto_senal_inicial_y):int(texto_senal_final_y),int(texto_senal_inicial_x):int(texto_senal_final_x)]
        fondo = imagen[int(texto_background_inicial_y):int(texto_background_final_y),int(texto_background_inicial_x):int(texto_background_final_x)]

        senal_p = deepcopy(senal)

        promedio_fondo = np.mean(fondo)
        desv_est_fondo = np.std(fondo)

        senal_gen = deepcopy(senal)  

        for i in range(len(senal_p)):
            for j in range(len(senal_p[0])):
                if(np.abs(senal_p[i,j] - promedio_fondo) < num_desv_est_fondo*desv_est_fondo):
                    senal_p[i,j] = 0    
             

        if(senal_estado == 0):

            self.nueva_ventana = tk.Toplevel(self.ventana)
            self.app = Ventana_senal_background(self.nueva_ventana,senal_p,fondo)

        elif(senal_estado == 1):
     
            self.nueva_ventana = tk.Toplevel(self.ventana)
            self.app = Ventana_senal_background(self.nueva_ventana,senal_global,fondo)
  
        else:
            
            self.nueva_ventana = tk.Toplevel(self.ventana)
            self.app = Ventana_senal_background(self.nueva_ventana,np.zeros((256,256)),np.zeros((256,256)))

    def agregar_perfil(self):

        perfil_inicial_x = self.entry_perf_inic_x.get()
        perfil_inicial_y = self.entry_perf_inic_y.get()
        perfil_final_x = self.entry_perf_final_x.get()
        perfil_final_y = self.entry_perf_final_y.get()

        imagen_p = deepcopy(imagen)      
 
        perfil_m = imagen_p[int(perfil_inicial_y):int(perfil_final_y),int(perfil_inicial_x):int(perfil_final_x)]
        
        

        # axis= 0 columnas
        if(self.modo_perfil == "vertical"):
            self.perfiles.append(np.sum(perfil_m, axis = 0))

        if(self.modo_perfil == "horizontal"):
            self.perfiles.append(np.sum(perfil_m, axis = 1))

    def perfil(self):

        self.nueva_ventana = tk.Toplevel(self.ventana)
        self.app = Ventana_perfiles(self.nueva_ventana,self.perfiles)

    def close_windows(self):
        self.ventana.destroy()

class Ventana_senal_background:
    def __init__(self, ventana,senal,fondo):

        global senal_global
        global senal_gen


        self.ventana = ventana
        self.ventana.geometry('1040x800')
        self.frame_cerrar = tk.Frame(self.ventana)

        self.cerrar = tk.Button(self.frame_cerrar, text = "Volver", width = 10, command = self.close_windows)
        self.cerrar.pack()
        self.frame_cerrar.pack()
        self.frame_cerrar.place(x=700+25, y=640)

        self.frame_act = tk.Frame(self.ventana)
        self.act = tk.Button(self.frame_act, text = "Quitar", width = 10, command = self.Quitar_senal)
        self.act.pack()
        self.frame_act.pack()
        self.frame_act.place(x=600+25, y=640)

        self.frame_agr = tk.Frame(self.ventana)
        self.agr = tk.Button(self.frame_agr, text = "Agregar", width = 10, command = self.Agregar_senal)
        self.agr.pack()
        self.frame_agr.pack()
        self.frame_agr.place(x=500+25, y=640)
       

        self.frame_cont = tk.Frame(self.ventana)
        self.cont = tk.Button(self.frame_cont, text = "Contorno", width = 10, command = self.Agregar_cont)
        self.cont.pack()
        self.frame_cont.pack()
        self.frame_cont.place(x=400+25, y=640)

        self.frame_pixel_check = tk.Frame(self.ventana)         
        self.frame_pixel_check.pack()
        self.frame_pixel_check.place(x=400+25, y=600)
        titulo_pixel_check = tk.Label(self.frame_pixel_check, text="Quitar cont:", font=("Helvetica", 10))
        titulo_pixel_check.pack()
        self.frame_caja_check = tk.Frame(self.ventana)         
        self.frame_caja_check.pack()
        self.frame_caja_check.place(x=400+25, y=620)
        self.check_val = tk.BooleanVar(self.ventana)
        self.check = ttk.Checkbutton(self.frame_caja_check, variable=self.check_val, command = self.checkbox_click)
        self.check.pack()

        self.estado_check = False

        self.frame_pixel_cont = tk.Frame(self.ventana)         
        self.frame_pixel_cont.pack()
        self.frame_pixel_cont.place(x=700+25, y=600)
        titulo_pixel_cont = tk.Label(self.frame_pixel_cont, text="Valor cont:", font=("Helvetica", 10))
        titulo_pixel_cont.pack()
        self.frame_caja_cont = tk.Frame(self.ventana)         
        self.frame_caja_cont.pack()
        self.frame_caja_cont.place(x=700+25, y=620)
        self.entry_caja_cont = ttk.Entry(self.frame_caja_cont, width=10)
        self.entry_caja_cont.pack()

        self.frame_titulo = tk.Frame(self.ventana)         
        self.frame_titulo.pack()
        self.frame_titulo.place(x=500+25, y=50)
        titulo = tk.Label(self.frame_titulo, text="Senal y Ruido obtenidos", font=("Helvetica", 16))
        titulo.pack()

        self.frame_titulo2 = tk.Frame(self.ventana)         
        self.frame_titulo2.pack()
        self.frame_titulo2.place(x=200+25, y=100)
        titulo_2 = tk.Label(self.frame_titulo2, text="Senal", font=("Helvetica", 16))
        titulo_2.pack()

        self.frame_senal = tk.Frame(self.ventana)         
        self.frame_senal.pack()
        self.frame_senal.place(x=25+25, y=150)

        

        f_s = Figure(figsize=(5.7,4), dpi=100)
        a_s = f_s.add_subplot(111)
        im_s = a_s.imshow(senal, cmap = color_imagen)
        f_s.colorbar(im_s)

        self.frame_titulo3 = tk.Frame(self.ventana)         
        self.frame_titulo3.pack()
        self.frame_titulo3.place(x=820+25, y=100)
        titulo_3 = tk.Label(self.frame_titulo3, text="Ruido", font=("Helvetica", 16))
        titulo_3.pack()

        self.frame_background = tk.Frame(self.ventana)         
        self.frame_background.pack()
        self.frame_background.place(x=645+25, y=150)

        f_b = Figure(figsize=(5.7,4), dpi=100)
        a_b = f_b.add_subplot(111)
        im_b = a_b.imshow(fondo, cmap = color_imagen)
        f_b.colorbar(im_b)

        canvas_s = FigureCanvasTkAgg(f_s, master=self.frame_senal)
        canvas_s.draw()
        canvas_s.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        toolbar_s = NavigationToolbar2Tk(canvas_s, self.frame_senal)
        toolbar_s.update()
        canvas_s._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        canvas_b = FigureCanvasTkAgg(f_b, master=self.frame_background)
        canvas_b.draw()
        canvas_b.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        toolbar_b = NavigationToolbar2Tk(canvas_b, self.frame_background)
        toolbar_b.update()
        canvas_b._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        senal_global = deepcopy(senal)

        self.lista_x = []        
        self.lista_y = []

        def onclick(event):

            x = event.xdata-0.5
            y = event.ydata-0.5
            
            if(x < 0.5):
                x = -1.0

            if(y < 0.5):
                y = -1.0
           

            self.lista_x.append(int(x) + 1)
            self.lista_y.append(int(y) + 1)
            print('%s click: button=%d, x=%d, y=%d, xdata=%f, ydata=%f' %
          ('double' if event.dblclick else 'single', event.button,
           event.x, event.y, event.xdata, event.ydata))

        canvas_s.mpl_connect('button_press_event', onclick)

    def checkbox_click(self):
        self.estado_check = self.check_val.get()

    def Agregar_cont(self):

        global senal_estado  
        global senal_global


        senal_estado = 1

        
        pixel_cont = float(self.entry_caja_cont.get()) 

        contornos = measure.find_contours(senal_global,pixel_cont)

        self.frame_senal = tk.Frame(self.ventana)         
        self.frame_senal.pack()
        self.frame_senal.place(x=25+25, y=150)

        f_s = Figure(figsize=(5.7,4), dpi=100)
        a_s = f_s.add_subplot(111)
        
        contorno_x = []
        contorno_y = []
 
        if(self.estado_check == True):
            
            for n, contorno in enumerate(contornos):
                #a_s.plot(contorno[:,1].astype(int),contorno[:,0].astype(int), linewidth=2)
                if(len(contorno[:,1]) > len(contorno_y) and len(contorno[:,0]) > len(contorno_x)):
                    contorno_x = contorno[:,0]
                    contorno_y = contorno[:,1]

            mascara = np.zeros_like(senal_global, dtype = "bool")
            mascara[np.round(contorno_x).astype(int), np.round(contorno_y).astype(int)] = 1
            mascara = ndimage.binary_fill_holes(mascara)
            senal_global = senal_global*mascara
            im_s = a_s.imshow(senal_global, cmap = color_imagen)

        else:
           
            for n, contorno in enumerate(contornos):
                if(len(contorno[:,1]) > len(contorno_y) and len(contorno[:,0]) > len(contorno_x)):
                    contorno_x = contorno[:,0]
                    contorno_y = contorno[:,1]

            a_s.plot(contorno_y.astype(int),contorno_x.astype(int), linewidth=2) 
            im_s = a_s.imshow(senal_global, cmap = color_imagen)
        
        f_s.colorbar(im_s)

        canvas_s = FigureCanvasTkAgg(f_s, master=self.frame_senal)
        canvas_s.draw()
        canvas_s.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        toolbar_s = NavigationToolbar2Tk(canvas_s, self.frame_senal)
        toolbar_s.update()
        canvas_s._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        del self.lista_x[:]
        del self.lista_y[:]
        del contornos

        def onclick(event):

            x = event.xdata-0.5
            y = event.ydata-0.5
            
            if(x < 0.5):
                x = -1.0

            if(y < 0.5):
                y = -1.0
           

            self.lista_x.append(int(x) + 1)
            self.lista_y.append(int(y) + 1)
            print('%s click: button=%d, x=%d, y=%d, xdata=%f, ydata=%f' %
          ('double' if event.dblclick else 'single', event.button,
           event.x, event.y, event.xdata, event.ydata))

        canvas_s.mpl_connect('button_press_event', onclick)      

    def Quitar_senal(self):

        global senal_estado  
        global senal_global

        print(self.lista_x)
        print(self.lista_y)
        senal_estado = 1
        #pixel_del_x = int(self.entry_caja_del_x.get())
        #pixel_del_y = int(self.entry_caja_del_y.get())

        
        #senal_global[pixel_del_y, pixel_del_x] = 0
        for i in range(len(self.lista_x)):
            senal_global[self.lista_y[i], self.lista_x[i]] = 0

        self.frame_senal = tk.Frame(self.ventana)         
        self.frame_senal.pack()
        self.frame_senal.place(x=25+25, y=150)

        f_s = Figure(figsize=(5.7,4), dpi=100)
        a_s = f_s.add_subplot(111)
        im_s = a_s.imshow(senal_global, cmap = color_imagen)
        f_s.colorbar(im_s)

        canvas_s = FigureCanvasTkAgg(f_s, master=self.frame_senal)
        canvas_s.draw()
        canvas_s.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        toolbar_s = NavigationToolbar2Tk(canvas_s, self.frame_senal)
        toolbar_s.update()
        canvas_s._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        del self.lista_x[:]
        del self.lista_y[:]

        def onclick(event):

            x = event.xdata-0.5
            y = event.ydata-0.5
            
            if(x < 0.5):
                x = -1.0

            if(y < 0.5):
                y = -1.0
           

            self.lista_x.append(int(x) + 1)
            self.lista_y.append(int(y) + 1)
            print('%s click: button=%d, x=%d, y=%d, xdata=%f, ydata=%f' %
          ('double' if event.dblclick else 'single', event.button,
           event.x, event.y, event.xdata, event.ydata))

        canvas_s.mpl_connect('button_press_event', onclick)

    def Agregar_senal(self):

        global senal_estado  
        global senal_global

        print(self.lista_x)
        print(self.lista_y)

        senal_estado = 1
        #pixel_gen_x = int(self.entry_caja_gen_x.get())
        #pixel_gen_y = int(self.entry_caja_gen_y.get())

        
        
        #senal_global[pixel_gen_y, pixel_gen_x] = senal_gen[pixel_gen_y, pixel_gen_x]
        for i in range(len(self.lista_x)):
            senal_global[self.lista_y[i], self.lista_x[i]] = senal_gen[self.lista_y[i], self.lista_x[i]]
      

        self.frame_senal = tk.Frame(self.ventana)         
        self.frame_senal.pack()
        self.frame_senal.place(x=25+25, y=150)

        f_s = Figure(figsize=(5.7,4), dpi=100)
        a_s = f_s.add_subplot(111)
        im_s = a_s.imshow(senal_global, cmap = color_imagen)
        f_s.colorbar(im_s)

        canvas_s = FigureCanvasTkAgg(f_s, master=self.frame_senal)
        canvas_s.draw()
        canvas_s.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        toolbar_s = NavigationToolbar2Tk(canvas_s, self.frame_senal)
        toolbar_s.update()
        canvas_s._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        del self.lista_x[:]
        del self.lista_y[:]

        def onclick(event):

            x = event.xdata-0.5
            y = event.ydata-0.5
            
            if(x < 0.5):
                x = -1.0

            if(y < 0.5):
                y = -1.0
           

            self.lista_x.append(int(x) + 1)
            self.lista_y.append(int(y) + 1)
            print('%s click: button=%d, x=%d, y=%d, xdata=%f, ydata=%f' %
          ('double' if event.dblclick else 'single', event.button,
           event.x, event.y, event.xdata, event.ydata))

        canvas_s.mpl_connect('button_press_event', onclick)

    def close_windows(self):
        self.ventana.destroy()

class Ventana_perfiles:
    def __init__(self,ventana,perfiles):
        self.ventana = ventana
        self.ventana.geometry('1035x800')
        self.frame_cerrar = tk.Frame(self.ventana)
        self.cerrar = tk.Button(self.frame_cerrar, text = "Volver", width = 10, command = self.close_windows)
        self.cerrar.pack()
        self.frame_cerrar.pack()
        self.frame_cerrar.place(x=500, y=640)

        self.frame_titulo = tk.Frame(self.ventana)         
        self.frame_titulo.pack()
        self.frame_titulo.place(x=500, y=50)
        titulo = tk.Label(self.frame_titulo, text="Perfil", font=("Helvetica", 16))
        titulo.pack()

        self.frame_p = tk.Frame(self.ventana)         
        self.frame_p.pack()
        self.frame_p.place(x=300, y=150)


        
        self.f_p = Figure(figsize=(5.7,4), dpi=100)
        self.a_p = self.f_p.add_subplot(111)

        for perfil in perfiles:
            self.im_p = self.a_p.plot(perfil)


        canvas_p = FigureCanvasTkAgg(self.f_p, master=self.frame_p)
        canvas_p.draw()
        canvas_p.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        toolbar_p = NavigationToolbar2Tk(canvas_p, self.frame_p)
        toolbar_p.update()
        canvas_p._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        
        self.frame_titulo2 = tk.Frame(self.ventana)         
        self.frame_titulo2.pack()
        self.frame_titulo2.place(x=400, y=600)
        titulo_2 = tk.Label(self.frame_titulo2, text="Nombre de archivo:", font=("Helvetica", 16))
        titulo_2.pack()

        self.frame_nombrep = tk.Frame(self.ventana)
        self.entry_nombrep = tk.Entry(self.frame_nombrep, width=28)
        self.entry_nombrep.pack()
        self.frame_nombrep.pack()
        self.frame_nombrep.place(x=400, y=620)

        self.frame_guardar = tk.Frame(self.ventana)
        self.guardar = tk.Button(self.frame_guardar, text = "Guardar", width = 10, command = self.guardar)
        self.guardar.pack()
        self.frame_guardar.pack()
        self.frame_guardar.place(x=400, y=640)

    def guardar(self):
        nombre_perfil = self.entry_nombrep.get()
        self.f_p.savefig(nombre_perfil)
        self.entry_nombrep.delete(0, tk.END)

    def close_windows(self):
        self.ventana.destroy()

###################################################################################
                

def main(): 
    root = tk.Tk()
    app = Ventana(root)
    root.mainloop()

if __name__ == '__main__':
    main()
