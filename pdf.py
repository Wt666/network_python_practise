from io import StringIO
from io import  open
from pdfminer.converter import  TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfinterp import PDFResourceManager, process_pdf

def read_pdf():
    with open('/Users/wt/Desktop/no_plan.pdf',"rb") as pdf:
        resource = PDFResourceManager()
        rw_str = StringIO()
        laparam = LAParams()
        device = TextConverter(resource, rw_str, laparams=laparam)
        process_pdf(resource, device, pdf)
        device.close()
        content = rw_str.getvalue()
        rw_str.close()
        lines = content.split("\n")
        print(lines)
read_pdf()