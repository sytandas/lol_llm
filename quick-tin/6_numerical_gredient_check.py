x = -2
y = 5
z = -4

h = 0.0001

def add(x, y):
    return x + y
def mul(x, y):
    return x * y
def forwardCircuit(x, y, z):
    a = add(x, y)
    b = mul(a, z)
    return b

x_derivative = (forwardCircuit(x+h, y, z) - forwardCircuit(x, y, z))/ h
y_derivative = (forwardCircuit(x, y+h, z) - forwardCircuit(x, y, z))/ h
z_derivative = (forwardCircuit(x, y, z+h) - forwardCircuit(x, y, z))/ h

print(x_derivative)
print(y_derivative)
print(z_derivative)
