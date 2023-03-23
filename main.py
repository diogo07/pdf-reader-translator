import PyPDF2
from deep_translator import GoogleTranslator

MAX_LETTERS_PER_REQUEST = 4999

reader = PyPDF2.PdfReader('data/tmf.pdf')
translator = GoogleTranslator(source='auto', target='pt')

for i in range(34, 35):
    text = reader.pages[i].extract_text()
    print(translator.translate(text[0:min(len(text), MAX_LETTERS_PER_REQUEST)]))
