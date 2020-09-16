import cv2
import os

current_dir = os.getcwd()
print("current directory: ",current_dir)
directory = current_dir+'/divided_block'
#So luong anh trong file nguon
n = 6
#Cach chia block
horizontal_divisor = 5
vertical_divisor = 2
for i in range(n):
	path = current_dir+'/image_source/image%d.jpg' %(i+1)
	img_src = cv2.imread(path)
	h, w, c = img_src.shape
	horizontal_step = w//horizontal_divisor
	vertical_step = h//vertical_divisor
	os.chdir(directory)
	for y in range(vertical_divisor):
		for x in range(horizontal_divisor):
			img_sub = img_src[y*vertical_step:(y+1)*vertical_step, x*horizontal_step:(x+1)*horizontal_step,:]
			print(img_sub.shape)
			img_sub_name = 'image%d%d.jpg' %(i+1,y*horizontal_divisor+x+1)
			cv2.imwrite(img_sub_name,img_sub)
			print('successfully saved ',img_sub_name)
	os.chdir(current_dir)
