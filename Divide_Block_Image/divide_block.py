import cv2
import numpy as np
import os

current_dir = os.getcwd()
print("current directory: ",current_dir)
directory = '/home/oanh/Documents/Divide_Block_Image/divided_block'
#So luong anh trong file nguon
n = 6
#Cach chia block
horizontal_divisor = 5
vertical_divisor = 2
for i in range(n):
	path = '/home/oanh/Documents/Divide_Block_Image/image_source/image%d.jpg' %(i+1)
	img_src = cv2.imread(path)
	h, w, c = img_src.shape
	horizontal_step = w//horizontal_divisor
	vertical_step = h//vertical_divisor
	for y in range(vertical_divisor):
		for x in range(horizontal_divisor):
			# img_sub = np.zeros([vertical_step,horizontal_step,c])
			img_sub = img_src[y*vertical_step:(y+1)*vertical_step, x*horizontal_step:(x+1)*horizontal_step,:]
			print(img_sub.shape)
			os.chdir(directory)
			img_sub_name = 'image%d%d.jpg' %(i,y*horizontal_divisor+x)
			cv2.imwrite(img_sub_name,img_sub)
			print('successfully saved ',img_sub_name)
	os.chdir(current_dir)
