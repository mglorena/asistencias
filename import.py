from multiprocessing import connection
from platform import python_branch

from numpy import array


def main():
    connectDB()
    content = openfile()
    #print(content)

def insertData(cvs):
    i =0
    import array as arr
    dias = [][]
    fechas=[][]
    for row in cvs:
        cols = len(row)
        #cols = cols - 4 
        #print("cols:", cols)
        if(i==0):
            tit0 = row[0]
            tit1 = row[1]
            tit2 = row[2]
            tit3 = row[3]
            
            
        for j in range (4,cols):
            #print(j)
            if(row[j].find("P (2/2)") != -1):
                dias.append(row[j])
            elif ( row[j].find("?") == -1):
                fechas.append(row[j])
        i+=1
    print(dias)
    print(fechas)


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
    with open('./asistencias_CT7.csv') as File:  
        reader = csv.reader(File)
        insertData(reader)
main()

