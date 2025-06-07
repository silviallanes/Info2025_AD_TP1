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