n,myProduct,result,amount,myPrice = 0,0,0,1,0

pname = ""

product = {
    0 : "Pepsi", 
    1 : "Coke",
    2 : "Oishi",
    3 : "Ichitan"
}

price = {
    0 : 15,
    1 : 17,
    2 : 25,
    3 : 20
}

def addCash() :
    global cash,n
    nCash = int(input("เงินไม่พอ กรุณาเพิ่มจำนวนเงิน : "))
    
    if checkCash(nCash):
        cash += nCash
        print("จำนวนเงิน : ",cash)
        
    if cash >= myPrice :
        n = 1
        return True
        

def checkCash(c):
    if c == 1 or c == 5 or c == 10 or c == 20 or c == 50 or c == 100 :
        return True
    else:
        print("กรุณาลองอีกครั้ง")

def getProduct(x):
    global pname ,myPrice
    # print(product[x],price[x])
    
    if x >= 0 :
        pname = product[x];
        myPrice = price[x] * amount;
        return True
    

print("เครื่องรับเฉพาะเงิน 1 ,5 ,20 ,10 ,50 ,100 บาทเท่านั้น")
while True:
    cash = int(input("กรุณาป้อนจำนวนเงิน : "))
    print("\n")
    
    if checkCash(cash):
        #print(len(product))
        for i in range(0,len(product),1) :
            print("รหัส: ",i ," |",product[i]," ราคา :",price[i] ," บาท")
        
        print("\nเลือกสินค้าโดยป้อนหมายเลขรหัสสินค้า")
        
        x = int(input("รหัสสินค้า : "))
        amount = int(input("จำนวน : "))
        print("---------------------------\n")
       
        if  getProduct(x):
            
            print("สินค้าที่เลือกคือ : ",pname)
            print("ราคา : ", myPrice , " บาท")
            print("จำนวน : ",amount , " ชิ้น")
            
            if cash < myPrice :
                while n != 1:
                    addCash()
                    
            if cash >= myPrice :   
                result = cash - myPrice
                print("เงินทอน : ", result ," บาท")
                break
            
print("\n-------------------------")
print("สินค้า : ",pname)
print("ขอบคุณที่ใช้บริการ !!")

