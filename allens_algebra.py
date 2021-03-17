#Este modulo contiene un implementacion del intervalo del Algebra de Allens"
#Ousama Dahbi Sebbaghi, 17/03/2021

class IntervaloInavlido(Exception):
    pass

class IntevaloRelacion:
    #Aqui se observa el itervalo de algebra de allen
    preceds = 'lt'
    follows = 'gt'
    meets = 'm'
    meets_inv = 'mi'
    overlaps = 'o'
    overlpas_inv = 'oi'
    starts = 's'
    strats_inv = 'si'
    during = 'd'
    during_inv = 'di'
    finishes = 'f'
    finishes_inv = 'fi'
    equals = 'eq'

class allen:
    def __calc__(self, X: dict, Y: dict):
        """
        Computacion del intervalo de relacion de a hacia b.
     In :
         X: dicta(s:int, c:int) intervalo empiza en (s) y termina en (c)
         Y: dicta(s:int, c:int) intervalo empieza en (s) y termina en (c)
         donde s < c
     Devolvera:
        tuple(X {?} Y, Y {?} X) donde,
        X{?} Y: es el intervalo de relacion "X es para Y" donde (x) es el intevalo del Algebra de Allen
        Y{?} X: es el intervalo de relacion "Y es para X" donde (x)  es el intevalo del Algebra de Allen
        https://en.wikipedia.org/wiki/Allen%27s_interval_algebra
        """
        # Empezamos validando el intervalo
        if X['s'] >= X['c']:
            raise IntervaloInavlido('Intervalo `a` es invalido.')
        if Y['s'] >= Y['c']:
            raise IntervaloInavlido('Intervalo `b` es invalido.')
        # Terminamos la validacion del intervalo

        #ordenamos los mismos
        if X['c'] > Y['c']:
            x_first = False
            first = Y
            second = X
        else:
            x_first = True
            first = X
            second = Y
        
        if first == second:
            out = (IntevaloRelacion.equals, IntevaloRelacion.equals)
        
        elif first['c'] < second['s']:
            out = (IntevaloRelacion.precedes, IntevaloRelacion.follows)
        
        elif first['c'] == second['s']:
            out = (IntevaloRelacion.meets, IntevaloRelacion.meets_inv)
        
        elif first['s'] < second['s'] \
        and \
        first['c'] > second['s'] \
        and \
        first['c'] < second['c']:
            out = (IntevaloRelacion.overlaps, IntevaloRelacion.overlpas_inv)
        
        elif first['s'] == second['s'] \
        and \
        first['c'] > second['s'] \
        and \
        first['c'] < second['c']:
            out = (IntevaloRelacion.starts, IntevaloRelacion.strats_inv)
        
        elif first['s'] > second['s'] \
        and \
        first['s'] < second['c'] \
        and \
        first['c'] > second['s'] \
        and \
        first['c'] < second['c']:
            out = (IntevaloRelacion.during, IntevaloRelacion.during_inv)
        
        elif first['s'] > second['c'] \
        and \
        first['s'] < second['c'] \
        and \
        first['c'] == second['c']:
            out = (IntevaloRelacion.finishes, IntevaloRelacion.finishes_inv)
        
        if x_first:
            return (out[0], out[1])
        else:
            return (out[1], out[0])

