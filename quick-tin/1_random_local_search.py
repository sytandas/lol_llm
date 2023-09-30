# neural net!!!
# we provide some i/p to given circuit (return x * y)  with specific value e.g. x = 1 y = 2
# the circuit compute some o/p value e.g. (1 * 2) 2
# How should one tweak the input slightly to increase the output? and why i need to?
# as we don't know the require output so we need to tweek it for performance, stability, require target fullfillment

# an example of random local search for best fit in 100 iteration  

import random 

def forward(x, y):
    return x * y

x = -2 
y = 3

tweek_amount = 0.01
best_out = float('-inf')
best_x = x
best_y = y

for k in range (100):
    x_try = x + tweek_amount * (random.random() * 2 - 1)
    y_try = y + tweek_amount * (random.random() * 2 - 1)
    out = forward(x_try, y_try)
    if (out > best_out):
        best_out = out
        best_x = x_try
        best_y = y_try

print(best_out)
