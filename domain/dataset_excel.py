#subclase específica para gestionar excels
import pandas as pd
from domain.dataset import Dataset

class DatasetExcel(Dataset):
    def __init__(self, fuente):
        super().__init__(fuente)

    def cargar_datos(self):
        try:
            df = pd.read_excel(self.fuente)
            self.datos = df
            print("Excel Cargado.")
            if self.validar_datos():
                print("Datos del excel validados")
                self.transformar_datos()

        except Exception as e:
            print(f"Error cargando Excel: {e}")

    def transformar_datos(self):
        if self.datos is not None:
            #se completan datos faltantes en columna barrio y se reemplaza sin geo
            self.datos['barrio'] = self.datos['barrio'].fillna('Desconocido')
            self.datos['barrio'] = self.datos['barrio'].replace(0,'Desconocido')
            self.datos['barrio'] = self.datos['barrio'].replace('Sin geo', "Desconocido")
            #se completan datos faltantes de la comuna
            self.datos['comuna'] = self.datos['comuna'].fillna('Desconocido')
            #se reemplazan valores en columna uso_moto
            self.datos['uso_moto'] = self.datos['uso_moto'].replace({'SI': True, 'NO': False})
            #se reemplazan valores en columna uso_arma
            self.datos['uso_arma'] = self.datos['uso_arma'].replace({'SI': True, 'NO': False})
            #cambiar el tipo de datos de la columna uso_moto a bool
            self.datos['uso_moto'] =self.datos['uso_moto'].astype(bool)
            #cambiar el tipo de datos de la columna uso_arma a bool
            self.datos['uso_arma'] =self.datos['uso_arma'].astype(bool)
            #cambiar el tipo de datos de la columna fecha a datetime
            self.datos['fecha'] = pd.to_datetime(self.datos['fecha'],dayfirst=True)
            self.datos['fecha'] = self.datos['fecha'].dt.date
            #eliminar columnas innecesarias
            self.datos.drop(columns=['id-mapa', 'anio', 'mes','comuna','latitud','longitud','cantidad'], inplace=True)
            
            print("Transformaciones aplicadas.")
        else:
             print("no hay datos para transformar.")
       