#3.Diseñe una app con una función que
#calcule el area del circulo
#y esta sea llamada por un algoritmo

# función con parámetros
def area(p):
    
  p=3.14
  area=p*(r*r)
  print("El area del circulo es: ",area)

r=int(input("Digite el radio del circulo: "))
area(r)  # llamada a la función, se muestra en la consola