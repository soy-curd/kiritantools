import xml.etree.ElementTree as ET


class Pitch:
    def __init__(self):
        self.step = 'G'
        self.octave = '4'

    def set_el(self, element):
        step = ET.SubElement(element, 'step')
        step.text = self.step
        octave = ET.SubElement(element, 'octave')
        octave.text = self.octave

        return element


class Lyric:
    def __init__(self, letter):
        self.default_x = ''
        self.default_y = ''
        self.relative_y = ''
        self.number = '1'
        self.syllabic = 'single'
        self.text = letter

    def set_el(self, element):
        element.set('default-x', self.default_x)
        element.set('default-y', self.default_y)
        element.set('relative-y', self.relative_y)
        element.set('number', self.number)
        syllabic = ET.SubElement(element, 'syllabic')
        syllabic.text = self.syllabic
        text = ET.SubElement(element, 'text')
        text.text = self.text
        return element


class Note:
    def __init__(self, letter, rest=False):
        self.pitch = Pitch()
        self.lyric = Lyric(letter)
        self.duration = '1'
        self.voice = '1'
        self.type = 'quarter'
        self.stem = 'up'
        self.default_x = ''
        self.default_y = ''
        self.rest = rest

    def set_el(self, element):
        if self.rest:
            rest = ET.SubElement(element, 'rest')

        pitch = ET.SubElement(element, 'pitch')
        self.pitch.set_el(pitch)
        lyric = ET.SubElement(element, 'lyric')
        self.lyric.set_el(lyric)

        duration = ET.SubElement(element, 'duration')
        duration.text = self.duration
        voice = ET.SubElement(element, 'voice')
        voice.text = self.voice
        type = ET.SubElement(element, 'type')
        type.text = self.type
        stem = ET.SubElement(element, 'stem')
        stem.text = self.stem

        element.set('default-x', self.default_x)
        element.set('default-y', self.default_y)
        return element


class Measure:
    def __init__(self, text):
        self.number = '100'
        self.width = ''
        self.text = text

    def set_el(self, element):
        max_text_len = 8
        if len(self.text) > max_text_len:
            raise ValueError('text length is over {}'.format(max_text_len))

        for letter in self.text:
            note = ET.SubElement(element, 'note')
            Note(letter).set_el(note)

        for _ in range(max_text_len - len(self.text)):
            # 長音防止のために休符を挿入
            note = ET.SubElement(element, 'note')
            Note('', rest=True).set_el(note)

        element.set('number', self.number)
        element.set('width', self.width)
        return element


def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


def load_xml(filename):
    tree = ET.parse(filename)
    return tree


def clean_xml(tree):
    root = tree.getroot()
    part = root.find('part')
    for measure in part.findall('measure'):
        if measure.get('number') == '1':
            print(measure.get('number'))
            continue

        part.remove(measure)

    return tree


def chunk_text(text):
    '''
    "きょうわ　よい　ひです"
    -> 
    [["きょ", "う", "わ"], ["よ", "い"], ["ひ", "で", "す"]]
    '''
    skip_letters = ('ゃ', 'ゅ', 'ょ', 'っ')
    max_chunk_length = 8
    splited_texts = text.split()
    result = []
    for splited_text in splited_texts:
        buf = []

        for i, x in enumerate(splited_text):
            if x in skip_letters:
                continue

            if i < len(splited_text) - 1 and splited_text[i+1] in skip_letters:

                buf.append(splited_text[i: i+2])
                continue

            buf.append(x)

        for chunk_text in chunks(buf, max_chunk_length):
            result.append(chunk_text)

    print(result)
    return result


def edit_xml(tree, text):
    tree = clean_xml(tree)
    root = tree.getroot()
    part = root.find('part')
    first_measure = part.find('measure')
    direction = first_measure.find('direction')
    sound = direction.find('sound')
    sound.set('tempo', '150')  # テンポの変更

    chunked_texts = chunk_text(text)
    for text_by_measure in chunked_texts:
        measure = ET.SubElement(part, 'measure')
        Measure(text_by_measure).set_el(measure)
    return tree


def wite_xml(tree, filename):
    tree.write(filename,
               encoding='utf-8',
               xml_declaration=True)


def main(text):
    # NEUTRINOのサンプルを読み込み
    filename = 'score/sample1.musicxml'
    tree = load_xml(filename)
    tree = edit_xml(tree, text)
    wite_xml(tree, filename)


if __name__ == '__main__':
    main("おはようございます きょうわいいてんきですねー")
