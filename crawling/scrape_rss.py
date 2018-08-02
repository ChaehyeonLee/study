from xml.etree import ElementTree

tree = ElementTree.parse('rss.xml')

root = tree.getroot()

for item in root.findall('channel/item/description/body/location/data'):
    tm_ef = item.find('tmEf').text
    tmn = item.find('tmn').text
    tmx = item.find('tmx').text
    wf = item.find('wf').text
    print(tm_ef, tmn, tmx, wf)