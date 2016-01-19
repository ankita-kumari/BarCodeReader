import zxing
import os
import sys
def read_bar_code(image_path):
    path = os.getcwd()
    path += '/zxing'
    reader = zxing.BarCodeReader(path)
    barcode = reader.decode(image_path)
    return barcode.data

if __name__=='__main__':
    image_path = sys.argv[1]
    print read_bar_code(image_path)

