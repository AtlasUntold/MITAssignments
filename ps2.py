class variables:
    pass

def diophantine():
    n = int(input("Can N number of McNuggets can be purchased at McDonalds? N =  "))
    x = 0
    y = 0
    z = 0
    test = 0

#def testZ():
    while (20 * test) < n:
        test += 1
        if (20 * test) > n:
            z = (test - 1)
            test = 0
            #testY()
            break
        elif (20 * test) == n:
            print(n, "McNuggets can be purchased at McDonalds.")
            exit()

#def testY():
    while (9 * test) + (20 * z) < n:
        test += 1
        if (9 * test) + (20 * z) > n:
            y = (test - 1)
            test = 0
            #testZ()
            break
        elif (9 * test) + (20 * z) == n: 
            print(n, "McNuggets can be purchased at McDonalds.")
            exit()

#def testX():
    while (6 * test) + ((9 * y) + (20 *z)):
        test += 1
        if (6 * test) + ((9 * y) + (20 *z)) > n:
            x = (test - 1)
            test = 0
            exit()
        elif (6 * test) + ((9 * y) + (20 *z)) == n:
            print(n, "McNuggets can be purchased at McDonalds.")
            exit()

diophantine()