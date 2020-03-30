import os ,sys
path = os.getcwd()+'\[Day4] Rename_File'
src = os.listdir(path)

print("List Diractory and List File : ",src); # เพื่อแสดงรายการของไฟล์ในตำแหน่งปัจจุบัน
old = path + "\\" + input("Plase enter your filename and type : ")
#print(old)
print("------------------ New Name ------------------\n")
new = path + "\\" + input("Plase enter your \"new\" filename and type : ")
os.rename(old,new)
print("Success!")