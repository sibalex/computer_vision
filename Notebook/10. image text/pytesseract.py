# pip install opencv-python
# pip install PyAutoGUI


# Координаты курсора (coordinati.py)
import pyautogui
import time

time.sleep(2)
# нужен ВЛ, НП
print(pyautogui.position())


# Поиск (find.py)
import numpy as np
import pyscreenshot as ImageGrab
import cv2
import os

filename = 'Image.png'
x = 1
last_time = time.time()

while:
	screen = np.array(ImageGrab.grab(bbox=x1,y1,x2,y2))
	# print('loop took {} seconds'.format(time.time()-last_time))
	last_time = time.time()
	cv2.imshow('window', cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))
	cv2.imwrite(filename, screen)
	x = x + 1
	# print(x)
	if x == 2:
		cv2.destroyAllWindows()
		break



# распознование (Tesseract OCR) 
# 1. pip install pytesseract
# 2. sudo apt install tesseract-ocr
import pytesseract

img = cv2.imread('Image.png') #filename
text = pytesseract.image_to_string(img)
# print(text)


# действия по найденным словам
f = 'You'
index = text.find(f) # 'You'
# print(index) #0-find-True ; '-1'-False

if index == -1:
	print('word "{}" was not found'.format(f))
else:
	print('word "{}" was found'.format(f))
	break



# Полный скрипт
import pyautogui
import time
import pytesseract
import numpy as np
import pyscreenshot as ImageGrab
import cv2
import os

filename = 'Image.png'
x = 1
last_time = time.time()

while:
	screen = np.array(ImageGrab.grab(bbox=x1,y1,x2,y2))
	# print('loop took {} seconds'.format(time.time()-last_time))
	last_time = time.time()
	# cv2.imshow('window', cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))
	cv2.imwrite(filename, screen)
	x = x + 1
	# print(x)

	# if x == 2:
	# 	cv2.destroyAllWindows()
	# 	break
	
	img = cv2.imread('Image.png') #filename
	text = pytesseract.image_to_string(img)
	print(text)

	# index = text.find('You') # f = input("Слово для поиска")
	# if index == -1:
	# 	print('word "{}" was not found'.format(f))
	# else:
	# 	print('word "{}" was found'.format(f))
	# 	break

	cv2.destroyAllWindows()
