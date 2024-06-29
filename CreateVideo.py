import os
import cv2


path = "C:/Users/thesl/OneDrive/Desktop/DAVID A.K.A COOL_D/CLASS_105/Images"

images = []


for file in os.listdir(path):
    name, ext = os.path.splitext(file)

    if ext in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        file_name = path+"/"+file

        print(file_name)
               
        images.append(file_name)
        
print(len(images))
count = len(images)
'''for i in range(0,count-1):
    frame=cv2.imread(images[i])
    cv2.imshow("Sunset",frame)
    if (cv2.waitKey(25)==32):
        break 
cv2.destroyAllWindows()
'''
for i in range(count-1,0,-1):
    frame=cv2.imread(images[i])
    cv2.imshow("Sunrise",frame)
    if (cv2.waitKey(25)==32):
        break 
cv2.destroyAllWindows()