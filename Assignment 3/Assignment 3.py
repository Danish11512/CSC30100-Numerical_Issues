import math
import time 

# Exact Value Function 
def ExactValue(n):
    return n*math.e
# Naive Summation Function 

def NaiveSummation(n):
    sum = 0
    e = math.e
    for i in range(0, n):
        sum = sum + e
    return sum

# Compensated Summation Function 
def CompensatedSummation(n):
    sum = c = 0
    for i in range(1, n+1):
        y = math.e - c
        temp = sum + y
        c = ( temp - sum ) - y 
        sum = temp
    return sum 

# Exact Values Calculated 

N1 = int(math.pow(10,6))
E1 = ExactValue(N1)
print('Extact value for 10^6 is ', E1)

N2 = int(math.pow(10,7))
E2 = ExactValue(N2)
print('Extact value for 10^7 is ', E2)

N3 = int(math.pow(10,8))
E3 = ExactValue(N3)
print('Extact value for 10^8 is ', E3)

N4 = int(math.pow(10,9))
E4 = ExactValue(N4)
print('Extact value for 10^9 is ', E4)

# Compensated Summations

starttime = time.time()
compensated1 = CompensatedSummation(N1)
endtime = time.time()
elapsedtimeC1 = endtime - starttime


starttime = time.time()
compensated2 = CompensatedSummation(N2)
endtime = time.time()
elapsedtimeC2 = endtime - starttime


starttime = time.time()
compensated3 = CompensatedSummation(N3)
endtime = time.time()
elapsedtimeC3 = endtime - starttime


starttime = time.time()
compensated4 = CompensatedSummation(N4)
endtime = time.time()
elapsedtimeC4 = endtime - starttime

# Naive Summations

starttime = time.time()
naive1 = NaiveSummation(N1)
endtime = time.time()
elapsedtimeN1 = endtime - starttime


starttime = time.time()
naive2 = NaiveSummation(N2)
endtime = time.time()
elapsedtimeN2 = endtime - starttime

starttime = time.time()
naive3 = NaiveSummation(N3)
endtime = time.time()
elapsedtimeN3 = endtime - starttime

starttime = time.time()
naive4 = NaiveSummation(N4)
endtime = time.time()
elapsedtimeN4 = endtime - starttime

table = [['Summation Method', 'Sum', 'Relative Error', 'Absolute Error', 'Elapsed Time'],
        ['Naive Summation for N = 10^6', naive1, naive1 - E1 , abs(naive1 - E1) ,elapsedtimeN1],
        ['Compensated Summation for N = 10^6', compensated1, compensated1 - E1 , abs(compensated1 - E1) ,elapsedtimeC1], 
        ['Naive Summation for N = 10^7', naive2, naive2 - E2 , abs(naive2 - E2) ,elapsedtimeN2],
        ['Compensated Summation for N = 10^7', compensated2, compensated2 - E2 , abs(compensated2 - E2) ,elapsedtimeC2],
        ['Naive Summation for N = 10^8', naive3, naive3 - E3 , abs(naive3 - E3) ,elapsedtimeN3],
        ['Compensated Summation for N = 10^8', compensated3, compensated3 - E3 , abs(compensated3 - E3) ,elapsedtimeC3], 
        ['Naive Summation for N = 10^9', naive4, naive4 - E4 , abs(naive4 - E4) ,elapsedtimeN4], 
        ['Compensated Summation for N = 10^9', compensated4, compensated4 - E4 , abs(compensated4 - E4) ,elapsedtimeC4] ]


for i in table:
    print(elapsedtimeN2)

    
    


