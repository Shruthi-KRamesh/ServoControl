class FibonacciSeries:
    def Fibonacci(self):
        nterms = 10
        n1 = 0
        n2 = 1
        fibo=[]
        fibo.append(n1)
        fibo.append(n2)
        count = 0
        if nterms <= 0:
            print("Please enter a positive integer")
        while count < nterms:
            nth = n1 + n2
            fibo.append(nth)
            n1 = n2
            n2 = nth
            count += 1
        return fibo
