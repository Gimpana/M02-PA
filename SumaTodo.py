def sumaTodos(limitTo):
    resultado = 0
    for i in range(0, limitTo+1):
        resultado += i
    
    return resultado

print(sumaTodos(100))

def sumaTodosLosCuadrados(c):
    resultado = 0
    for i in range(c+1):
        resultado += i*i
    
    return resultado

print(sumaTodosLosCuadrados(2))