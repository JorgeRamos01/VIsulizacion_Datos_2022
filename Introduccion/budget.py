import csv

File = "budget_data.csv"

change=[]
months=[]

with open(File) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader) #Saltamos el encabezado
    rowPrev=next(csvreader) #Generamos la primera fila de valores
    total = int(rowPrev[1]) #Por completitud nuestro primer valor de la suma total esta inicializado con el valor de la primera fila
    for row in csvreader: 
        total += int(row[1])
        diff=int(row[1])-int(rowPrev[1])
        change.append(diff)
        months.append(row[0])
        rowPrev=row

#Dado que las listas de meses y cambios estan pareadas verificamos en donde se encuentran los indices de mayor y menor cambio
ind_max=change.index(max(change))
ind_min=change.index(min(change))

#Generamos el texto a imprimir
Strings=["Financial Analysis\n", "-"*50+"\n", "Total Months:  {} \n".format(len(months)+1), "Total:  ${} \n".format(total), 
        "Average Change:  ${} \n".format(round(sum(change)/len(change),2)), 
        "Greatest Increase in Profits: {} (${}) \n".format(months[ind_max],change[ind_max]), 
        "Greatest Decrease in Profits: {} (${}) \n".format(months[ind_min], change[ind_min])]

#Imprimimos el texto en la terminal
print( Strings[0],Strings[1],Strings[2],Strings[3],Strings[4],Strings[5], Strings[6])

#Imprimimos los resultados en un archivo de texto
outputfile="main.txt"
file1 = open(outputfile,"w") 
file1.writelines(Strings)
file1.close() #Cerramos el archivo

