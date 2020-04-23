import xml.etree.ElementTree as ET


class Pitch:
    def __init__(self):
        self.step = 'G'
        self.optave = 4

    def set_el(self, element):
        element.set('step', self.step)
        element.set('optave', self.optave)
        return element
        
class Lyric:
    def __init__(self):
        self.default_x = '6.58'
        self.default_y = '-53.20'
        self.number = '1'
        self.relative_y = '-30.00'
        self.syllabic = 'single'
        self.text = 'い'

    def set_el(self, element):
        element.set('default-x', self.default_x)
        element.set('default-y', self.default_y)
        element.set('number', self.number)
        element.set('relative-y', self.relative_y)
        element.set('syllabic', self.syllabic)
        element.text = self.text
        retrun element


class Note:
    def __init__(self):
        self.pitch = Pitch()
        self.duration = 2
        self.voice = 1
        self.type = 'quarter'
        self.stem = 'up'
        self.lyric = Lyric()

    def set_el(self, element):
        pitch = ET.SubElement(element, 'pitch')
        Pitch().set_el(pitch)
        lyric = ET.SubElement(element, 'lyric')
        Lyric().set_el(lyric)

        element.set('duration', self.duration)
        element.set('voice', self.voice)
        element.set('type', self.type)
        element.set('stem', self.stem)
        return element

def load_xml(filename):
    tree = ET.parse(filename)
    return tree


def clean_xml(tree):
    root = tree.getroot()
    part = root.find('part')
    for measure in part.findall('measure'):
        if measure.get('number') == '1' or measure.get('number') == '2':
            print(measure.get('number'))
            continue

        part.remove(measure)

    return tree


def edit_xml(tree):
    tree = clean_xml(tree)
    root = tree.getroot()
    part = root.find('part')
    for measure in part.findall('measure'):
        note = ET.SubElement(measure, 'note')
        Note().set_el(note)
    return tree


def wite_xml(tree, filename):
    tree.write(filename,
               encoding='utf-8',
               xml_declaration=True)


def main():
    # NEUTRINOのサンプルを読み込み
    filename = 'score/sample1.musicxml'
    tree = load_xml(filename)
    tree = edit_xml(tree)
    wite_xml(tree, filename)


if __name__ == '__main__':
    main()
