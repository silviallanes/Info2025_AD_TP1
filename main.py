#donde se instancian los objetos. define la estructura. la ruta. 
from os import path
from domain.dataset_csv import DatasetCSV
from domain.dataset_excel import DatasetExcel
from data.data_saver import DataSaver

#Ruta archivos
csv_path = path.join(path.dirname(__file__),"files/Sales.csv")
excel_path = path.join(path.dirname(__file__),"files/Adidas US Sales Datasets.xlsx")

#Cargar y transformar
csv = DatasetCSV(csv_path)#instanciamos el objeto csv
csv.cargar_datos()
csv.mostrar_resumen()

excel = DatasetExcel(excel_path) #instanciamos el objeto excel
excel.cargar_datos()
excel.mostrar_resumen()

#guardar en base de datos
db = DataSaver()
db.guardar_dataframe(csv.datos,"sales_csv")
db.guardar_dataframe(excel.datos,"adidas_us_sales_datasets_xlsx")