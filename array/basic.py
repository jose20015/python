cars = ["Ford", "Volvo", "BMW"]
print(cars)

cars[0] = "Toyota"
print(cars)

x = len(cars) #tamanho da array
print(x)

for x in cars: #lendo cada elemento da array
	print(x)

cars.append("Honda") #adicionar no final da array
print(cars)

cars.pop(1) #remover um elemento da array, pela posição
#print(cars) 