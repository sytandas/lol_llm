def forward(x, y):
    return x * y

x = -2
y = 3

x_gredient = y
y_gredient = x

step_size = 0.01

x += step_size * x_gredient 
y += step_size * y_gredient 

out = forward(x, y)

print(out)
