import numpy as np
import os,cv2

path = os.getcwd()+"\[Day5] Resize_Image"
#print(os.listdir(path)) #แสดงรายการไฟล์
img = cv2.imread(path+'\logo.png',cv2.IMREAD_UNCHANGED)
print('Original Dimensions : ',"Height :",img.shape[0]," ,Width : ",img.shape[1]," ,Number of channels :",img.shape[2]) #ขนาดเดิม
cv2.imshow("Original image", img)

scale_percent = int(input("Scale Percent : ")) #ขนาดใหม่กี่เปอ์เซ็นจาก 100%
width = img.shape[1] * scale_percent / 100
height = img.shape[0] * scale_percent / 100
dim = (int(width),int(height)) # Dimensions ขนาด

resized = cv2.resize(img,dim, interpolation = cv2.INTER_AREA) #ทำการปรัยขนาด
print('Resized Dimensions : ',"Height :",resized.shape[0],",Width : ",resized.shape[1]," ,Number of channels :",img.shape[2]) #ขนาดใหม่ 

cv2.imshow("Resized image", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
