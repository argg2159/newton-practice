import scipy

def multi_optimize(x0, f, tol=1e-5):
    #set up inital value and step
    H = scipy.differentiate.hessian(f, x0)
    grad = scipy.differentiate.derivative(f, x0)
    
    #xnext = x - t
    #    t = hessian inverse * gradient
    #      = solve(hessian, gradient)    
    x1 = x0 - scipy.linalg.solve(H, grad)

    while scipy.spatial.distance.euclidian(x1, x0) > tol:
        x0 = x1
        H = scipy.differentiate.hessian(f, x0)
        grad = scipy.differentiate.derivative(f, x0)
        
        x1 = x0 - solve(H, grad)
        
    return x1