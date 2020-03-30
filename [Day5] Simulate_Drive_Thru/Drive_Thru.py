cash,price,result,last,n,myPrice = 0,0,0,0,0,0
select = ""
e = False
order = {}
priceOfOrders = {}
menu = {
    0 : "Pizza",
    1 : "Chicken Massamun",
    2 : "Grilled Poke Neck",
    3 : "Tom Yum Kong",
    4 : "Som Tum",
}
priceOfMenu = {
    0 : 259,
    1 : 70,
    2 : 80,
    3 : 75,
    4 : 40,
}

def getMenu(s) :
    
    if s == "ALL" :
        i = 0
        stop = len(menu)
    else : 
        i = s
        stop = i+1
    
    for i in range(i,stop,1) :
        print("ID: ", i,"\t",menu[i],"\t",priceOfMenu[i],"฿")
    
        
    return " "

def setOrders(s) :
    global order
    mid = int(s)
    
    if mid >= len(menu) or mid == "":
        return "Error : Please try again!!"
    # print(type(mid))
    else :
        i = len(order) + 1
        stop = i + 1
        
        for x in range(i,stop,1):
            order[x] = menu[mid]
            priceOfOrders[x] = priceOfMenu[mid]
            #print("ID: ", i,"\t",order[i])
        getOrders()
    
def getOrders() :
    global result,last
    
    print("\n------- Orders ---------")
    for i in order:
        print("ID: ",i,"\t",order[i],"\t",priceOfOrders[i])
        result = last + priceOfOrders[i]
    
    last = result
    
    print("----------------------")    
    print("-- Price : ",result)
    print("----------------------")

def checkCash(c):
    if c == 1 or c == 2 or c == 5 or c == 10 or c == 20 or c == 50 or c == 100 or c == 500 or c == 1000 :
        return True
    else:
        print("Please try again.")

def calculate(c):
    global result,n,myPrice,cash
    
    if c < result  :
        nCash = int(input("Plase add your cash : "))
        
        if checkCash(nCash):
            cash += nCash
            
    if c >= result :
        myPrice = c - result
        n = 1
    
   
          
print("\nWellcome to Drive Thru")
print("------- Menu ---------")
print(getMenu("ALL"))
print("----------------------")

while e != True :
    select = input("Plase Enter ID for add Orders : ")
    
    
    if select == "Y" or select == "y" :
        e = True
    else :
        setOrders(select)
        print("Enter 'Y' or 'y' for yes.\n")

    
while n != 1:
    cash = int(input("Plase enter cash for payment : "))
    print("Your cash : ",cash)
    
    if checkCash(cash):
        while n != 1 :
            calculate(cash)

print("-------- Success --------")
print("-> Cash : ",cash)
print("-> Change : ", myPrice)
print("-------------------------")

