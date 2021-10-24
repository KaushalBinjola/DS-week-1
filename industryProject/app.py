# imports
from PIL import Image
import pytesseract
import re

# extracting data from image
pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'

a = pytesseract.image_to_string(Image.open('img5.jpg'))

a = a.split()
# print(a)

# cleaning data
# getting numeric and currency form data
reg = "^\$?(([1-9](\d*|\d{0,2}(,\d{3})*))|0)(\.\d{1,2})?$"
b = []
for i in a: 
    if(re.match(reg,i)):
        b.append(i)

#replacing comma and . to make it into float data
# print(b)
sign = ""

newArr = []
for i in b:
    if i[0] not in [str(_) for _ in range(9)]:
        sign = i[0]
        i = i[1:]
    else:
        pass
    
    if i.find(',')!=-1:
        ind = i.rindex(",")
        if(len(i[ind+1:ind+4])==2):
            i = i[:ind] + "." + i[ind+1:]
        if i.find(',')!=-1:
            i = i.replace(",","")
    else: 
        pass
    
    # print(i)
    if i.find(".")!=-1:
        newArr.append(float(i))
    else:
        pass

# getting new array of all viable amounts
# print(newArr)

# max of viable new array is Total Amount
print("Total is:- ",sign+str(max(newArr)))