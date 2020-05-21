# Función de cálculo del método de falsa posición
def regulafal(f, x, a, b, e):
    i = 1
    ea = 1.0
    mant = 1
    
    while ea > e:
        m = float(b - ( ( f.subs(x,b).evalf() * (a-b) )/(f.subs(x,a).evalf() - f.subs(x,b).evalf() ) ))
        print("{:5}\t{:.5}\t{:.5}\t{:.5}\t{:.5}".format(i,a,b,m,ea))
        if ( f.subs(x,a)*f.subs(x,m) ) < 0:
            b = m
        else:
            a = m
        
        if i > 1:
            ea = abs((m-mant)/m)
        i += 1
        mant = m
    
    # Regresar el valor de la raíz
    return m