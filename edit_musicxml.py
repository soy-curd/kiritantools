import xml.etree.ElementTree as ET

tree = ET.parse('score/sample1.musicxml')  # NEUTRINOのサンプルを読み込み
root = tree.getroot()

[x for x in root.iter('part')]
part = root.find('part')

notes = part.iter('note')
_ = next(notes)
note = next(notes)
lyric = note.find('lyric')
text = lyric.find('text')
text.text = 'い'
text.set('updated', 'yes')

tree.write('score/sample1.musicxml', encoding='utf-8',
           xml_declaration=True)
