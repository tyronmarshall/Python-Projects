###Calculating PI to the Nth digit###
import decimal

def pi(n):
    """Calculate PI to the Nth digit."""

    D = decimal.Decimal
    decimal.getcontext().prec = n+10
    pi = D(0)
    k = 0
    tail_prev = ''
    while True:
        pi += (D(4)/D(8*k+1) -
               D(2)/D(8*k+4) -
               D(1)/D(8*k+5) -
               D(1)/D(8*k+6)) / D(16)**D(k)
        tail = str(pi)[n+1:-1]
        if tail == tail_prev:
            break
        tail_prev = tail
        k += 1
    decimal.getcontext().prec = n
    return str(pi * D(1))

