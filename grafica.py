# importing packages
import seaborn as sns
import matplotlib.pyplot as plt

# loading dataset
data = sns.load_dataset("iris")

# draw lineplot
sns.lineplot(x="sepal_length", y="sepal_width", data=data)


# setting the title using Matplotlib
plt.title('Title using Matplotlib Function')

plt.show()


#declaración de una función con retorno
def sumar (a, b):
    return a+b

#declaración de función SIN retorno
def resta(a,b):
    print(a-b)
    

#llamado de función
resultado = sumar(110,110)
restaResult = resta(20,10)

resta(5,3)

#Impresión por consola de variables
print(resultado)
print(restaResult)

print(sumar(2,5))

