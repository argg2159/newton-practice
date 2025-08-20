def dir_1(x, f, eps=0.001):
    """Approximation of the first derivative of a function at a point.
    x: value to evalauate the first derivative at.
    f: function to evaluate.
    eps: value to use when approximating the first derivative. It serves as h in the average rate of change of a function. Default value is 0.001.
    """
    return (f(x + eps) - f(x)) / eps  # Average rate of change.


def dir_2(x, f, eps=0.001):
    """Approximation of the second derivative of a function at a point.
    x: value to evalauate the second derivative at.
    f: function to evaluate.
    eps: value to use when approximating the second derivative. It serves as h in the average rate of change of the function. Default value is 0.001.
    """
    # We use approximations of the first derivative to calculate the second.
    f1 = dir_1(x, f, eps)
    f1_eps = dir_1(x + eps, f, eps)
    return (f1_eps - f1) / eps


def optimize(x_0, f, eps=0.001, tol=0.00001):
    """Runs Newton's method to minimize a function
    x_0: starting value to begin approximation, should be close to an initial guess of the minimum value
    f: function to optimize.
    eps: value to use when approximating the first and second derivative. Default value is 0.001.
    tol: A level of precision for the newtons method. absolute error between values in the newtons method before the function stops.
    """
    x_1 = x_0 - dir_1(x_0, f, eps) / dir_2(x_0, f, eps)
    while abs(x_1 - x_0) > tol:
        x_0 = x_1
        x_1 = x_0 - dir_1(x_0, f, eps) / dir_2(x_0, f, eps)
    return x_1
