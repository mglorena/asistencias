from multiprocessing import connection
from platform import python_branch


def main():
    connectDB()
    content = openfile()
    #print(content)

def insertData(cvs):
    #mydb = connectDB()
    
    import numpy as np
    #mycursor = mydb.cursor()
    val = numpy.array() #testetete
    for row in cvs:
        #sql =" INSERT INTO asistencias.sesiones(apellido,nombre,idestudiante,correo,d1,d2,d3,d4,d5,d6,d7,d8,d9,d10,d11,d12,d13,d14,d15,d16,d17,d18,d19,d21,d22,d23,d24,d25,d26,d27,d28,d29,d30,d31,d32,d33)"
        #sql += "VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

        val.append(row[0])
        
        #mycursor.execute(sql, val)
        #mydb.commit()
        print(val)
            #print(len(row))
            #campos = row[0].split(";")
            #print(campos)
    









def connectDB():
    import mysql.connector
    mydb = mysql.connector.connect(
    host="localhost",
    user="lorena",
    password="lorena5",
    database="asistencias"
    )
    """ mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM sesiones LIMIT 1")
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)
    """
    mydb.close()

def openfile():
    import csv
    print("Abre el archivo de obras.csv\n")
    with open('/home/lorena/Downloads/asistencias_CT7.csv') as File:  
        reader = csv.reader(File)
        insertData(reader)
main()

