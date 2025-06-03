# Functions for image captioning, OCR, etc.

import pytesseract
from PIL import Image

# This might need to be changed at some point.
# If tesseract isn't found or something
# look at this:
# https://stackoverflow.com/questions/50951955/pytesseract-tesseractnotfound-error-tesseract-is-not-installed-or-its-not-i
pytesseract.pytesseract.tesseract_cmd = '/opt/homebrew/bin/tesseract'


# get image and stuff
def read_image(filename):
    image = Image.open(filename)
    return pytesseract.image_to_string(image)


if __name__ == '__main__':
    print(read_image("doritos_label.png"))