import sys
import xml.etree.ElementTree as ET

class Parser:

    def parseFile(self, filename):
        tree = ET.parse(filename)
        root = tree.getroot()

        for testElement in root.iter('test'):
            for keywordElement in testElement.iter('kw'):
                if keywordElement.get('name') == 'Log':
                    result = keywordElement.find('msg').text
        return result


