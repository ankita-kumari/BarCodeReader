import zxing
import os
import sys
def read_bar_code(image_path):
    path = os.getcwd()
    path += '/zxing'
    print 'path = ', path
    reader = zxing.BarCodeReader(path + '/zxing')
    barcode = reader.decode(image_path)
    return barcode.data

if __name__=='__main__':
    image_path = sys.argv[1]
    print read_bar_code(image_path)

