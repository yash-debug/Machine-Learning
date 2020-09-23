x=4000

def f(x):
    d=0
    while x >= 1:
        (x,d) = (x/5,d+1)
    return(d)
    