def forward(x, y):
    return x * y

x = -2
y = 3
h = 0.00001
out = forward(x, y)

xph = x + h
out2 =  forward(xph, y)
x_derivative = (out2 - out) / h

yph = y + h
out3 = forward(x, yph)
y_derivative = (out3 - out) / h

step_size = 0.01
out = forward(x, y)

x = x + step_size * x_derivative
y = y + step_size * y_derivative

out_new = forward(x, y)

print(out_new)
