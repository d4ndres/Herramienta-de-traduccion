import cv2
import pytesseract as tst
from googletrans import Translator
import numpy as np
from PIL import ImageGrab


translator = Translator()
tst.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

capture = ImageGrab.grabclipboard()
capture_np = np.array(capture)
img = cv2.cvtColor( capture_np, cv2.COLOR_RGB2BGR)

text = tst.image_to_string(img)
res = translator.translate( text , dest='es')
print( res.text )

cv2.imshow('imagen', img)
cv2.waitKey(0)
cv2.destroyAllWindows()