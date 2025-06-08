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
            self.__datos = self.datos.drop_duplicates() 
            print(self.datos.describe())
            print("detalles del dataframe")
            print(self.datos.info())
            print("Tipos de datos de las columnas")
            print(self.datos.dtypes)
            print("valores nulos")
            print(self.datos.isnull().sum())
        else:
            print("no hay datos para transformar.")
        


    def visualizar_datos_estadisticos(self):
        return print(self.datos.describe(include='all') if self.datos is not None else "No hay datos")