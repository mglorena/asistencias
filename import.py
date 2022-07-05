#from ast import Break
#from multiprocessing import connection
#from platform import python_branch

#from numpy import array


def main():
    firstInsert()
    updateAsistencias()
    

def insertData(cvs):
    vals =[]
    for row in cvs:
       val = ( row[2],row[1],row[0],row[3])
       vals.append(val)
    datos(vals)

def connectDB():
    import mysql.connector    
    mydb = mysql.connector.connect(
    host="localhost",
    user="lorena",
    password="lorena5",
    database="asistencias"
    )
    mycursor = mydb.cursor()
    return [mydb,mycursor];
    
def datos(vals):
    (myconn,mycursor) = connectDB()
    query="INSERT INTO `asistencias`.`tblAsistencias` (`idEstudiante`,`Nombre`,`Apellido`,`CantAsistencias`) VALUES (%s, %s,%s,%s)"
    mycursor.executemany(query, vals)
    myconn.commit()
    myconn.close()


def updateCant(vals):
    (myconn,mycursor) = connectDB()  
    for e in vals:
        mycursor.callproc('updateAsistencias',[e[2],e[3]])
        myconn.commit()
    #for result in myconection[1].stored_results():
    #    print(result.fetchall())
    mycursor.close()
    myconn.close()
    

def firstInsert():
    import csv
    with open('./data/JAVA_Asistencias_todos.csv') as File:  
        reader = csv.reader(File)
        insertData(reader)

def multiOpenFile(_list):
    import csv
    
    for x in _list:
        try:
            with open(x) as f:
                updateCant(csv.reader(f))
        except:
            pass
              
def updateAsistencias():
    import csv
    fm = ["./data/JAVA_Asistencias_CM1.csv","./data/JAVA_Asistencias_CM2.csv", "./data/JAVA_Asistencias_CM3.csv","./data/JAVA_Asistencias_CM4.csv","./data/JAVA_Asistencias_CM5.csv","./data/JAVA_Asistencias_CM6.csv","./data/JAVA_Asistencias_CM7.csv","./data/JAVA_Asistencias_CM8.csv"]
    fn = ["./data/JAVA_Asistencias_CN1.csv","./data/JAVA_Asistencias_CN2.csv","./data/JAVA_Asistencias_CN3.csv","./data/JAVA_Asistencias_CN4.csv","./data/JAVA_Asistencias_CN5.csv","./data/JAVA_Asistencias_CN6.csv","./data/JAVA_Asistencias_CN7.csv","./data/JAVA_Asistencias_CN8.csv"]
    ft = ["./data/JAVA_Asistencias_CT1.csv","./data/JAVA_Asistencias_CT2.csv","./data/JAVA_Asistencias_CT3.csv","./data/JAVA_Asistencias_CT4.csv","./data/JAVA_Asistencias_CT5.csv","./data/JAVA_Asistencias_CT6.csv","./data/JAVA_Asistencias_CT7.csv"]
    fv = ["./data/JAVA_Asistencias_CV1.csv","./data/JAVA_Asistencias_CV2.csv"]
    multiOpenFile(fm)
    multiOpenFile(fn)
    multiOpenFile(ft)
    multiOpenFile(fv)
    
main()

