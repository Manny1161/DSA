def calcNGCD(x, y):
    try:
        if not type(x) or not type(y) is int:
            raise TypeError('Import must be an integer only!')
        elif x<0 or y<0:
            raise ValueError('Import must not be negative!')
        else:
            return _gcd(x, y)
    except Exception as err:
        print('ERROR:', err)

def _gcd(x, y):
    if y==0:
        f=x
    else:
        f=_gcd(y, x%y)
    return f

if __name__ == "__main__":
    print(calcNGCD('a', 18));
