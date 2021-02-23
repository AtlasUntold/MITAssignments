import time
import sys

def computePrimes():
    count = 1
    number = 3
    check = 0
    while count <= 1000:
            for i in range(1, (number + 1)):
                #time.sleep(.5)
                if number % i == 0 and check < 2:
                    check += 1
                    if number == 7927:
                        exit()
                    if check >= 2 and i != number:
                        #print(number, " is not prime.")
                        number += 2
                        check = 0
                        break
                    elif check < 2 and i == number:
                        #sys.stdout = open('test.txt', 'a')
                        print(number, " is prime.")
                        #sys.stdout = close()
                        count += 1
                        number += 2
                        break
                    elif check >= 2:
                        #sys.stdout = open('test.txt', 'a')
                        print(number," is prime.")
                        #sys.stdout.close()
                        check = 0
                        count += 1
                        number += 2
                        break
                else:
                    #print("checking next factor of ", number, " i is", i, " check is", check)
                    pass


computePrimes()
