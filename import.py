from multiprocessing import connection
from platform import python_branch

from numpy import array


def main():
    
    content = openfile()
    #print(content)

def insertData(cvs):
 
    vals =[]
    for row in cvs:
       val = ( row[2],row[1],row[0],row[3])
       vals.append(val)
    connectDB(vals)
    
 

def connectDB(vals):
    import mysql.connector
    mydb = mysql.connector.connect(
    host="localhost",
    user="lorena",
    password="lorena5",
    database="asistencias"
    )
    mycursor = mydb.cursor()
    query="INSERT INTO `asistencias`.`tblAsistencias` (`idEstudiante`,`Nombre`,`Apellido`,`CantAsistencias`) VALUES (%s, %s,%s,%s)"
    
    mycursor.executemany(query, vals)
    mydb.commit()
    mydb.close()

def openfile():
    import csv
    print("Abre el archivo de obras.csv\n")
    with open('./asistencias_CM1.csv') as File:  
        reader = csv.reader(File)
        insertData(reader)
main()

