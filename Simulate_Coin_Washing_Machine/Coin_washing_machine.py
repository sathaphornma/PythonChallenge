import time
coin,result = 0,0

def checkCoin(c) :
    if c == 10 :
        return True
    
def runTime(t) :
    for i in range(t,1,-1):
        print("เหลือเวลาอีก: ",i)
        time.sleep(1)

while True:
    coin = int(input("\nกรุณาหยอดเหรียญ 10 บาท : "))
    if checkCoin(coin) and result <= 30 :
        result += coin
        print("\nจำนวนเงิน: ",result)
        
    else :
        print("\nกรุณาหยอดเฉพาะเหรียญ 10 บาทเท่านั้น")
        
    if result == 30:
        print("\nเครื่องกำลังทำงาน!!\n")
        runTime(5)
            
        print("\nเครื่องทำงานเสร็จสิ้น")
        coin,result = 0,0
        
