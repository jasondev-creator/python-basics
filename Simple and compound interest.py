def simpInt(principle,time,rate):
    si = float(principle*time*rate/100)
    return si
def compInt(principle,time,rate):
    ci = float(principle * ((1+rate/100)** time - 1))
    return ci
principle = float(input('Enter amount:'))
time = float(input('Enter time:'))
rate = float(input('Enter rate:'))
si = simpInt(principle,time,rate)
ci = compInt(principle,time,rate)
print('Simple interest is Rs.%8.2f % si')
print('Compound interest is Rs.%8.2f % ci')
diffint=ci-si;
print("Difference is Rs.%8.2f " % diffint)
