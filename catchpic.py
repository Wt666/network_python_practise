import fitz
import re
import os
file_path='/Users/wt/Desktop/2.pdf'
dir_path='/Users/wt/Desktop/7810'
def pdf2image1(path,pic_path):
    checkIM=r"/Subtype(?=*/image)"
    pdf=fitz.open(path)
    lenXREF=pdf._getXrefLength()
    count=1
    for i in range(1,lenXREF):
        text=pdf._getXrefString(i)
        isImage=re.search(checkIM,text)
        if not isImage:
            continue
            pix = fitz.Pixmap(pdf,i)
            new_name=f"img_{count}.png"
            pix.writePNG(os.path.join(pic_path, new_name))

            count += 1
            pix = None

pdf2image1(file_path, dir_path)