import cv2
import pytesseract


#importing tesseract from pytesseract
#Proivding path of document
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
#Reading document file
im=cv2.imread('./pp.jpg')
#using this configuration 
config = ('-l eng --oem 1 --psm 3')
# pytessercat

#Conveting image to string
text = pytesseract.image_to_string(im, config=config)
# print text
text = text.split('\n')
#printing text 
#print(text)
#Writing extracted text into .txt file
text_file = open("D:/data.txt", "w")

#For proper spacing using this
for i in text:
    n = text_file.write(i)
    n = text_file.write(" ")
text_file.close()