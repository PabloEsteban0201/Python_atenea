import seaborn as sb

#Cambios
#crear variable nombre 
nombre = 'Lorena'


data = sb.load_dataset("iris")

# draw lineplot 
sb.lineplot(x="sepal_length", y="sepal_width", data=data)

#Operadores
a = 'b'
b = 123

a = 2


#condiciones
if 2 == 5:
    print('2 es igual 5')
else:
    print('2 no es igual a 5')

print('hola mundo')


#Identificar si un 
list = [1,2,3,4,5,6,7]

for i in list:

    if i%2 == 0:
        print('El número es par')
    else:
        print(' El número es impar')


