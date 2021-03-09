class Fibonacci():
    def __init__(self,start):
        self.start = start
        self.fibonacciList=[]
    def printSequence(self,count):
        """
        instant generation
        count --> length of fibonacci sequence
        """
        firstStep = self.start
        nextStep = self.start
        for i in range(count):
            print(nextStep)
            firstStep , nextStep = nextStep , firstStep+nextStep
    def storeSequence(self,count):
        """
        belirtilen uzunlukta başlangıç değeri constructorda girilen fibonacci dizisini üretip kaydeder
        """
        firstStep = self.start
        nextStep  = self.start
        for i in range(count):
            self.fibonacciList.append(firstStep)
            firstStep, nextStep = nextStep, firstStep + nextStep

    def getSequence(self):
        """
        fibonacci listesine kaydedilen veriyi döndürür
        :return:
        """
        return self.fibonacciList

    def printStoredSequence(self):
        """
        fibonacci listesine kaydedilen sayiları konsola basar
        :return:
        """
        print(self.fibonacciList)

    def destructStoredSequence(self):
        """
        fibonacci listesindeki değerleri siler
        :return:
        """
        self.fibonacciList.clear()
if __name__ == '__main__':
    fibonacci = Fibonacci(19)
    fibonacci.printStoredSequence() # None
    fibonacci.storeSequence(19)
    fibonacci.printStoredSequence()
    fibonacci.destructStoredSequence()
    fibonacci.printStoredSequence()

#upgrade 2  gamified console version

