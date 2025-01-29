import xml.etree.ElementTree as ET

#criando uma estrutura XML

raiz = ET.Element('pessoas')
pessoa = ET.SubElement(raiz, 'pessoa', id='1')
ET.SubElement(pessoa, 'nome').text = 'joão'

ET.SubElement(pessoa, 'idade').text = '30'

#salvando em um arquivo

arvore = ET.ElementTree(raiz)
arvore.write('dados.xml')