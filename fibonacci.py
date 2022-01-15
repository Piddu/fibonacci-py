nDigits = 1000

def fibonacciNDigits(nDigits):
    a,b = 0,1
    fNumber = 0
    i = 0;
    digits = 0
    position = 1;
    while digits < nDigits:
        fNumber = a + b
        a = b
        b = fNumber
        s = str(fNumber)
        digits = len(s)
        position = position + 1
    return fNumber, position

fNumber,position = fibonacciNDigits(nDigits)
print('Posizione: ' +str(position))
print(fNumber)
        
