x = -2
y = 5 
z = -4

def forward_add(x, y):
    return x + y
def forward_mul(x, y):
    return x * y

q = forward_add(x, y)
f = forward_mul(q, z)

# gredient of the Multiply gate wrt i/p
derivative_f_wrt_z = q
derivative_f_wrt_q = z

derivative_q_wrt_x = 1.0
derivative_q_wrt_y = 1.0

# chain rule
derivative_f_wrt_x = derivative_q_wrt_x * derivative_f_wrt_q
derivative_f_wrt_y = derivative_q_wrt_y * derivative_f_wrt_q

print(derivative_f_wrt_x)
print(derivative_f_wrt_y)
print(derivative_f_wrt_z)

# let the inputs respond to the force/tug:
step_size = 0.01 
x += step_size * derivative_f_wrt_x
y += step_size * derivative_f_wrt_y
z += step_size * derivative_f_wrt_z

# output circuit upgrade from the step_size
q = forward_add(x, y)
f = forward_mul(q, z)

print(f)
