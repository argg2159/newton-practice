def grad(x, f, eps):
    return (f(x + eps) - f(x))/eps
def second_dir(x, f, eps):
    f1 = grad(x, f)
    f1_eps = grad(x + eps, f)
    return (f1_eps - f1)/eps
    
def optimize(x_0, f, eps = 0.01):
    x_1 = x_0 - grad(x_0, f, eps)/second_dir(x_0, f, eps)
    while abs(x_1 - x_0) > 0.01:
        x_0 = x_1
        x_1 = x_0 - grad(x_0, f, eps)/second_dir(x_0, f, eps)
    return x_1
        
        