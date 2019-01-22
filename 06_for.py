var = 6
nombres = []

for var in range(0,var):
    nombres.append(input("Introduca nombre: "))

select = []

for i in range(0,len(nombres)):
   if(nombres[i].count("a")):
       select.append(nombres[i])
                     

print(select)
