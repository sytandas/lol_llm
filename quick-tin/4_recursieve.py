def forward_mul(x, y):
    return x * y

def forward_add(x, y):
    return x + y

def forward_circuit(x, y, z):
    q = forward_add(x, y)
    f = forward_mul(q, z)
    return f

x = -2 
y = 5
z = -4
f = forward_circuit(x, y, z)
print(f)

