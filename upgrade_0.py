class Fibonacci():
    def __init__(self,start):
        self.start = start
        self.fibonacciList=[]
    def printFibonacci(self,count):
        """
        count --> length of fibonacci sequence
        """
        firstStep = self.start
        nextStep = self.start
        for i in range(count):
            print(nextStep)
            firstStep , nextStep = nextStep , firstStep+nextStep


fibonacci_çanakkale = Fibonacci(17)

fibonacci_çanakkale.printFibonacci(17)
