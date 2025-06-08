#donde se instancian los objetos. define la estructura. la ruta. 
from os import path
from domain.dataset_csv import DatasetCSV
from domain.dataset_excel import DatasetExcel
from data.data_saver import DataSaver

#Ruta archivos
#csv_ruta = path.join(path.dirname(__file__),"files/Sales.csv")
xlsx_ruta = path.join(path.dirname(__file__),"files/delitos_2023.xlsx")

#Cargar y transformar
# csv = DatasetCSV(csv_ruta)#instanciamos el objeto csv
# csv.cargar_datos()
# csv.visualizar_datos_estadisticos()

xlsx = DatasetExcel(xlsx_ruta) #instanciamos el objeto excel
xlsx.cargar_datos()
xlsx.visualizar_datos_estadisticos()

#guardar en base de datos
db = DataSaver()
#db.guardar_dataframe(csv.datos,"sales_csv")
db.guardar_dataframe(xlsx.datos,"delitos_2023_xlsx")