'''
Author: Anshu Saini
GitHub: https://github.com/anshu189
Mail: anshusaini189381@gmail.com
Requirements: textblob (pip install textblob)
Program: Spelling Corrector

'''

from textblob import TextBlob

a = input("Enter your sentence/word: ")
txt = TextBlob(a)
crt = txt.correct()
print("=>", crt)
input()
