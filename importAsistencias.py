def main():
    header = createheader()
    body = createbody()
    footer = createfooter()
    path= "./obras.html"
    content = openfileObras()
    html = header + body + content + footer
    savefile(path,html)
    
    
def generaTablaObras(csv):
    text ="<table class='table'>"
    text +="<thead>"
    text +="<tr>"
    text +="<th scope='col'>Nombre</th>"
    text +="<th scope='col'>Lict Num</th>"
    text +="<th scope='col'>Apertura</th>"
    text +="<th scope='col'>Localidad</th>"
    text +="</tr>"
    text +="</thead>"
    text +="<tbody>"
    i =0
    for row in csv:
        #createHtmlObra(row,i)
        if(i!=0) : 
            print(row)
            campos = row[0].split(";")
            text +="<tr>"
            text +="<th scope='row'>"+campos[6]+"</th>"
            text +="<th scope='row'>"+campos[5]+"</th>"
            text +="<th scope='row'>"+campos[4]+"</th>"
            text +="<th scope='row'>"+campos[12]+"</th>"

        #text +="<td>"+row[1]+"</td>"
        #text +="<td>"+row[2]+"</td>"
        #text +="<td><a href='www_"+ str(i)+"_FormObra.html'>"+row[0]+row[1]+"</a></td>"
            text +="</tr>"
        i+=1
    text +="</tbody>"
    text +="</table>"
    return text
def generaContentFormObra(row,i):
    import csv
    html="html de obra\n" #testoSS
    file = str(i)+"_FormObra.csv"
    with open(file) as File:  
        reader = csv.reader(File, delimiter=';', quotechar='"')
        for row in reader:
            html +=row[0]+"<br/>"
                   
    return html
def createHtmlObra(row,i):
    #print("Generando el nuevo archivo")
    import os
    path =str(i)+"_FormObra.html"
    if os.path.exists(path):
        os.remove(path)
    else:
        print("The file does not exist")
    f = open(path, "w")
    html = generaContentFormObra(row,i)
    f.write(html)
    f.close()
    #print("Creado el archivo")       
   
def openfileObras():
    import csv
    print("Abre el archivo de obras.csv\n")
    with open('75.csv') as File:  
        reader = csv.reader(File)
        return generaTablaObras(reader)

    
def createheader():
    text ="<!DOCTYPE html><html lang='es-ar' translate='no'><head>\n"
    text +="<meta charset='utf-8'>\n"
    text +="<title>Gestor de Licitaciones</title>\n"
    text +="<meta name='google' content='notranslate'>\n"
    text +="<meta name='viewport' content='width=device-width, initial-scale=1'>\n"
    text +="<link rel='icon' type='image/x-icon' href='images/favicon.png'>\n"
    text +="<link href='https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css' rel='stylesheet' integrity='sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC' crossorigin='anonymous'>"
    #text +="<link src='file:///media/lorena/software/dev/eyplic/js/css/bootstrap.min.css' rel='stylesheet' >\n"
    text +="<script src='file:///media/lorena/software/dev/eyplic/js/jquery.js'></script>\n"
    text +="<style>"
    text +="#sidebar{"
    text +="float:left;"
    text +="witdh:200px;"
    text +="border:2px solid blue;"
    text +="}</style>"
    text +="</head>\n"
    return text
def dropDownLocalidades():
    text ="<select class='form-select' aria-label='Default select example'>"
    text +="<option selected>Seleccione la Localidad</option>"
    text +="<option value='1'>Capital</option>"
    text +="<option value='2'>Tartagal</option>"
    text +="<option value='3'>Oran</option>"
    text +="<option value='4'>Cafayate</option>"
    text +="<option value='5'>Metan</option>"
    text +="<option value='6'>Rosario de la Frontera</option>"
    text +="</select>"
    return text
def createbody():
    text = "<body><div id='content'>Hola Mundo </div>"
    text += "<script src='file:///media/lorena/software/dev/eyplic/js/bootstrap.bundle.min.js'></script>"
    text += "<div id='content'>"
    text += "<div id='sidebar'>"
    text +="<div class='select'>"
    text += dropDownLocalidades()
    text +="</div>"
    text +="</div>"
    text +="</div>"
    return text
def savefile(path,html):
    print("Generando el nuevo archivo")
    import os
    if os.path.exists(path):
        os.remove(path)
    else:
        print("The file does not exist")
    f = open(path, "w")
    f.write(html)
    f.close()
    print("Creado el archivo")
def createfooter():
    text ="<footer></footer></body></html>"
    return text

main()

