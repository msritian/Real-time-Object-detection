import xml.etree.cElementTree as ET
import cv2
from PIL import Image
import imutils
import numpy as np

img = cv2.imread("flower.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (5, 5), 0)

# threshold the image, then perform a series of erosions +
# dilations to remove any small regions of noise
thresh = cv2.threshold(gray, 45, 255, cv2.THRESH_BINARY)[1]
thresh = cv2.erode(thresh, None, iterations=2)
thresh = cv2.dilate(thresh, None, iterations=2)

# find contours in thresholded image, then grab the largest
# one
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if imutils.is_cv2() else cnts[1]
c = max(cnts, key=cv2.contourArea)

# determine the most extreme points along the contour
extLeft = tuple(c[c[:, :, 0].argmin()][0])  # smallest x coordinate
extRight = tuple(c[c[:, :, 0].argmax()][0])  # largest x coordinate
extTop = tuple(c[c[:, :, 1].argmin()][0])  # largest y coordinate
extBot = tuple(c[c[:, :, 1].argmax()][0])  # smallest y coordinate

# draw the outline of the object, then draw each of the
# extreme points, where the left-most is red, right-most
# is green, top-most is blue, and bottom-most is teal
# cv2.drawContours(img, [c], -1, (0, 255, 255), 2)
# cv2.circle(img, extLeft, 8, (0, 0, 255), -1)
# cv2.circle(img, extRight, 8, (0, 255, 0), -1)
# cv2.circle(img, extTop, 8, (255, 0, 0), -1)
# cv2.circle(img, extBot, 8, (255, 255, 0), -1)
# show the output image
# cv2.imshow("Img", img)
# cv2.waitKey(0)

root = ET.Element("annotation")
doc = ET.SubElement(root, "doc")
ET.SubElement(root, "folder").text = 'open cv'
ET.SubElement(root, "filename").text = 'flower.jpg'
ET.SubElement(root, "path").text = 'C:/Users/mitta/PycharmProjects/open cv/flower.jpg'

source = ET.SubElement(root, "source")
# ET.SubElement(source, "database").text = 'Unknown'

size = ET.SubElement(root, "source")
filename = 'flower.jpg'
with Image.open(filename) as image:
    width, height = image.size
ET.SubElement(size, "width").text = str(width)
ET.SubElement(size, "height").text = str(height)
# ET.SubElement(size, "depth").text = "q.size"

# ET.SubElement(root, "segemented").text = '0'

obj = ET.SubElement(root, "object")
ET.SubElement(obj, "name").text = 'flower'
ET.SubElement(obj, "xmax").text = str(extRight)
ET.SubElement(obj, "xmin").text = str(extLeft)
ET.SubElement(obj, "ymax").text = str(extTop)
ET.SubElement(obj, "ymin").text = str(extBot)

# ET.SubElement(doc, "field1", name="blah").text = "some value1"
# ET.SubElement(doc, "field2", name="asdfasd").text = "some vlaue2"

tree = ET.ElementTree(root)
tree.write("t.xml")
# a = int(str(extRight))
# b = int(str(extLeft))
# c = int(str(extTop))
# d = int(str(extBot))
# rectangle = np.zeros(a + b, c + d, np.uint8)
# cv2.rectangle(rectangle, b + d, a + c, 255, -1)
