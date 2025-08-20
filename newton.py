# A function to approximate the first derivative of the funciton f.
def grad(x, f, eps = 0.001):
    return (f(x + eps) - f(x))/eps

# A function to approximate the second derivative using the "grad" function.
def second_dir(x, f, eps = 0.001):
    f1 = grad(x, f, eps)
    f1_eps = grad(x + eps, f, eps)
    return (f1_eps - f1)/eps

def optimize(x_0, f, eps = 0.001):
    x_1 = x_0 - grad(x_0, f, eps)/second_dir(x_0, f, eps)
    while abs(x_1 - x_0) > 0.00001:
        x_0 = x_1
        x_1 = x_0 - grad(x_0, f, eps)/second_dir(x_0, f, eps)
    return x_1
        
        