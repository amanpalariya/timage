# Timage
Converts an image to ASCII art. Timage is a combination of text and image.

# How to use?
```python
from PIL import Image
from timage import Timage

#Initialize
timage = Timage(Image.open('file.png'))

#Print
timage.pretty_print()
```
