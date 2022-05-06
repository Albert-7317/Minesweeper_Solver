###details###
#this is a bot that plays minesweeper im really lazy so use this link https://minesweeperonline.com/#beginner
#at 300% zoom in on the crt only with the scroll bars in the top left corner

###imports###
import pyautogui as pag
import pytesseract, cv2, time
from pytesseract import image_to_string
from PIL import Image



###variables###
#mouse cordinates
middleBlock = (295, 545)
fireFox = (533, 842)
currentTab = (590, 762)

startLeft = 252
startRow = 317

cols = []

def startClick(x, y, z):
    pag.click(x)
    pag.click(y)
    pag.click(z)

def rowSlicer(capture, left, row):
    screenshot = pag.screenshot(region=(left, row, 48, 45))
    screenshot.save(capture + ".png")

def checker(counter):
    pytesseract.pytesseract.tesseract_cmd=r'C:\Users\abrown\AppData\Local\Programs\Tesseract-OCR'
    img = cv2.imread(str(counter) + '.png')
    HSV_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h,s,v = cv2.split(HSV_img)
    thresh = cv2.threshold(v, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    checker.txt = image_to_string(thresh, config="--psm 6 digits")

def hiddenCheck(counter):
    im = Image.open(str(counter) + '.png')
    from collections import defaultdict
    by_color = defaultdict(int)
    for pixel in im.getdata():
        by_color[pixel] += 1
    hiddenCheck.hidden = by_color

def mousePos():
    x, y = pag.position()
    print(x, y)
###main event###
while True:
    time.sleep(3)
    #mousePos()
    #startClick(fireFox, currentTab, middleBlock)
    for row in range(0, 9):
        row = []
        counter = 0
        for i in range(0, 2):
            counter = counter + 1
            rowSlicer(str(counter), startLeft, startRow)
            startLeft = startLeft + 46
        counter = 0
        startRow = startRow + 42
        for i in range(0, 9):
            counter = counter + 1
            checker(counter)
            if checker.txt[:1] == '1':
                row.append('1')
            elif checker.txt[:1] == '2':
                row.append('2')
            elif checker.txt[:1] == '3':
                row.append('3')
            else:
                hiddenCheck(counter)
                #print(hiddenCheck.hidden)
                #print('**********************************************')
                row.append('e')
        cols.append(row)
        startLeft = 94
    for row in cols:
        print(row)
    #mousePos()
    break