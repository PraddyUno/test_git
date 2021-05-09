# Finding GCD Revised Version
def GCD(a,b):
    ''' Fund the greates common divisor'''
    if b == 0:
        return a
    else:
        return GCD(b, a%b)
    
