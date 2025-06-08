#
import pandas as pd
from domain.dataset import Dataset

class DatasetCSV(Dataset):
    def __init__(self, fuente):
        super().__init__(fuente)

    def cargar_datos(self):
        try:
            df = pd.read_csv(self.fuente)
            self.datos = df
            print("CSV Cargado.")
            if self.validar_datos():
                print("Datos validados")
                self.transformar_datos()

        except Exception as e:
            print(f"Error cargando csv: {e}")
    
    def transformar_datos(self):
        if self.datos is not None:
            #se completan datos faltantes en columna barrio
            self.datos['barrio'] = self.datos['barrio'].fillna('Desconocido')
            #se cambia el tipo de dato de comuna a str y se completan datos faltantes
            self.datos['comuna'] = self.datos['comuna'].astype('string')
            self.datos['comuna'] = self.datos['comuna'].fillna('Desconocido')
            #se reemplazan valores en columna uso_moto y se cambia a bool
            self.datos['uso_moto'] = self.datos['uso_moto'].replace({'SI': True, 'NO': False})
            self.datos['uso_moto'] =self.datos['uso_moto'].astype(bool)
            #se reemplazan valores en columna uso_arma y se cambia el tipo de dato a bool
            self.datos['uso_arma'] = self.datos['uso_arma'].replace({'SI': True, 'NO': False})
            self.datos['uso_arma'] =self.datos['uso_arma'].astype(bool)
            #completar datos faltantes en longitud y latitud
            self.datos['latitud'] = self.datos['latitud'].fillna('Desconocido')
            self.datos['longitud'] = self.datos['longitud'].fillna('Desconocido')
            #cambiar el tipo de dato de la columna fecha
            self.datos['fecha'] = pd.to_datetime(self.datos['fecha'])
            self.datos['fecha'] = self.datos['fecha'].dt.date
            #completar el dato nulo de la columna franja con la moda de esa columna
            self.datos['moda'] = self.datos['franja'].mode()[0]
            self.datos['franja'] = self.datos['franja'].fillna(self.datos['moda'])
            #convertir los datos de la columna franja en integer
            self.datos['franja'] = self.datos['franja'].astype('int64')
            #eliminar columnas innecesarias
            self.datos.drop(columns=['id-mapa', 'anio', 'mes','comuna','latitud','longitud','cantidad','moda'], inplace=True)
            
            print("Transformaciones aplicadas.")
        else:
             print("no hay datos para transformar.")
       