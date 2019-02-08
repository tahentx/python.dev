import xml.etree.ElementTree as ET
tree = ET.parse('2075.01.xml')
root = tree.getroot()
print(root[0][2].text)