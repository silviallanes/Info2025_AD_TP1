#donde se instancian los objetos. define la estructura. la ruta. 
from os import path
from domain.dataset_csv import DatasetCSV
from domain.dataset_excel import DatasetExcel

#Ruta archivos
csv_path = path.join(path.dirname(__file__),"files/Sales.csv")
excel_path = path.join(path.dirname(__file__),"files/Adidas US Sales Datasets.xlsx")

#Cargar y transformar
csv = DatasetCSV(csv_path)#instanciamos el objeto csv
csv.cargar_datos()
# csv.mostrar_resumen()

excel = DatasetExcel(excel_path) #instanciamos el objeto excel
excel.cargar_datos()

#guardar en base de datos
# db = DataSaver()
# db.guardar_dataframe(csv.datos,"Sales_csv")
# db.guardar_dataframe(excel.datos,"Adidas US Sales Datasets_xlsx")