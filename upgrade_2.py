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
            self.fibonacciList.append(nextStep)
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
    sapiens = Fibonacci(int(input("sapiens fibonacci dizisinin başlangıç sayısını giriniz...")))
    selectionPrompt = "0 : Store Sequence\n" \
                      "1 : Get   Sequence\n" \
                      "2 : Print Stored Sequence\n" \
                      "3 : Destruct Stored Sequence\n" \
                      "4 : print arbitary length of a fibonacci sequence\n" \
                      "5 : Menüyü tekrar gör\n" \
                      "6 : Çıkış\n"
    def backToMenu():
        print("0 : Menüye dön\n"
              "1 : Programdan çık")
    print("Sapiens Fibonacci Dizisi programına hoş geldiniz")
    while(True):
        print(selectionPrompt)
        selection = int(input(""))
        if selection == 0:
            temp_0 = int(input("Please enter length of sequence that will be stored :"))
            sapiens.storeSequence(temp_0)
            backToMenu()
            temp = int(input())
            if temp == 0 :
                continue
            else :
                break
        elif selection == 1:
            sapiens.getSequence()
            backToMenu()
            temp = int(input())
            if temp == 0:
                continue
            else:
                break
        elif selection == 2:
            sapiens.printStoredSequence()
            backToMenu()
            temp = int(input())
            if temp == 0:
                continue
            else:
                break
        elif selection == 3:
            sapiens.destructStoredSequence()
            backToMenu()
            temp = int(input())
            if temp == 0:
                continue
            else:
                break
        elif selection == 4:
            temp_4 = int(input("Please enter length of arbitrary sequence "))
            sapiens.printSequence(temp_4)
            backToMenu()
            temp = int(input())
            if temp == 0:
                continue
            else:
                break
        elif selection == 5:
            print(selectionPrompt)
        elif selection == 6:
            print("quitting...")
            break
