from threading import Thread, Lock
from random import randrange
from time import sleep

class Bank(Thread):
    
    def __init__(self, balance = 0):
        super().__init__()
        self.balance = balance
        self.transactions = 100
        self.lock = Lock()


    def deposit(self):
        # k = 0
        for j in range(0, self.transactions):
            i = randrange(50, 500)
            if self.lock.locked():
               # print(self.lock.locked())
                self.lock.release()
                self.balance += i
                sleep(0.001)
                #print(self.lock.locked())
            else:
                #print(self.lock.locked())
                self.balance += i
                print(f'Пополнение: {i}. Баланс: {self.balance} \n')
                sleep(0.001)
            print(f'Пополнение: {i}. Баланс: {self.balance} \n')

        #     k += 1
        # print(k)



    def take(self):
        #x = 0
        for j in range(0, self.transactions):
            i = randrange(50, 500)
            print(f'Запрос на {i} \n')
            if i <= self.balance:
                self.balance -= i
                print(f'Снятие: {i}. Баланс: {self.balance} \n')
                sleep(0.001)

            else:
                print(f'Запрос отклонен, недостаточно средств \n')
                self.lock.acquire()
                sleep(0.001)


        #     x += 1
        # print(x)


bk = Bank()

th1 = Thread(target=Bank.deposit, args=(bk,))
th2 = Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
