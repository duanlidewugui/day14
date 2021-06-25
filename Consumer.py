#厨师0.05一个面包，篮子满了，厨师睡三秒，
#消费者0.1秒一个面包，篮子空了，等2秒，带了1000元


import threading
import time

bread = 0

class chef(threading.Thread):
    name = ""
    def run(self) -> None:
        global bread
        while True:
            if bread<500:
                bread+=1
                print(self.name,"做了一个面包，现在面包有",bread,"个")
                time.sleep(0.05)
            else:
                time.sleep(3)
                print(self.name,"睡了3秒")

class consumer(threading.Thread):
    name = ""
    money = 1000

    def run(self) -> None:
        global bread
        while True:
            if bread>0 and self.money>0:
                self.money -= 2
                bread-=1
                print(self.name,"买了一个面包，现在还有",bread,"个面包还有",self.money,"钱")
                time.sleep(0.1)
            elif self.money<=0:
                print(self.name,"没钱了。所以走了")
                break
            else:
                time.sleep(2)
                print(self.name,"等待了2秒")

c1 = chef()
c2 = chef()
c3 = chef()
c1.name = "厨师1"
c2.name = "厨师2"
c3.name = "厨师3"

cos1 = consumer()
cos2 = consumer()
cos3 = consumer()
cos4 = consumer()
cos5 = consumer()
cos1.name = "客户1"
cos2.name = "客户2"
cos3.name = "客户3"
cos4.name = "客户4"
cos5.name = "客户5"


c1.start()
c2.start()
c3.start()
cos1.start()
cos2.start()
cos3.start()
cos4.start()
cos5.start()
