#clase base, atributos y metodos basicos de las clases y desde donde heredan las otras - lo básico que van a tener las demás clases
from abc import ABC, abstractmethod

class Dataset(ABC): #inicializada la clase
    def __init__(self,fuente):
        self.__fuente = fuente  #encapsulación
        self.__datos = None #se generan internamente

    @property   #público getter
    def datos(self):
        return self.__datos
    
    @datos.setter
    def datos(self, value):
        #validaciones
        self.__datos = value

    @property
    def fuente(self):
        return self.__fuente

    @abstractmethod
    def cargar_datos(self):
        pass


    def validar_datos(self):
        if self.datos is None:
            raise ValueError("Datos no cargados") 
        if self.datos.isnull().sum().sum() > 0:
            print("Datos faltantes detectados")
        if self.datos.duplicated().sum()>0:
            print("Filas duplicadas detectadas")
        return True

    def transformar_datos(self):
         if self.datos is not None:
             self.__datos.columns = self.datos.columns.str.lower().str.replace(" ","_")
             self.__datos = self.datos.drop_duplicates() 
            #  for col in self.datos.select_dtypes(include="object").columns:
            #      self.__datos[col] = self.datos[col].astype(str).str.strip()
             print("Transformaciones aplicadas.")
         else:
             print("no hay datos para transformar.")



    def mostrar_resumen(self):
        return print(self.datos.describe(include='all') if self.datos is not None else "No hay datos")