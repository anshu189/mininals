'''
Author: Anshu Saini
GitHub: https://github.com/anshu189
Mail: anshusaini189381@gmail.com
Requirements: translate (pip install translate)
Program: Translator

'''

from translate import Translator

to_lang = input("Enter the language 'to' which you want to translate the text: ")
from_lang = input("Enter the language 'from' which you want to translate the text: ")
text = input("Enter the text you want to translate: ")
translator = Translator(from_lang=from_lang, to_lang=to_lang)
result = translator.translate(text)
print(result)
input()