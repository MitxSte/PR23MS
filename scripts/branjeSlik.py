"""
Branje slik in zapis veljavnih podatkov v datoteko.
"""

import cv2
import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = "C:\Program Files\Tesseract-OCR\\tesseract.exe"

file_name = 'test.txt'
file = open(file_name, 'w')
file.write('datum,ura,dan\n')


#54
for i in range(54, 0, -1):
    path = "slike\\" + str(i) + ".jpg"
    #print(path)
    screenshot = cv2.imread(path)
    screenshot_rgb = cv2.cvtColor(screenshot, cv2.COLOR_BGR2RGB)
    text = pytesseract.image_to_string(Image.fromarray(screenshot_rgb))
    lines = text.split('\n')

    stevec = 0
    ura = ""

    for line in lines:
        if line == '':
            continue
        stevec += 1

        #print(line)
        dolz = len(line.split(' '))

        if stevec % 2 == 0 and len(line) == 14 and len(ura) == 5 and dolz == 2:  # Datum + dan
            datum = line.split(' ')[0]
            dan = line.split(' ')[1]

            test = len(datum.split('.'))

            if (dan == "Mon" or dan == "Tue" or dan == "Wed" or dan == "Thu" or dan == "Fri" or dan == "Sat" or dan == "Sun") and test == 3:
                izpis = datum + ',' + ura + ',' + dan + '\n'
                print(izpis)
                file.write(izpis)

        else:  # ura
            ura = line
