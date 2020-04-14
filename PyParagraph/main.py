"""------------------------------------------------------------------
PyParagraph
Mario Vicente Martinez E.
2020-04-13
------------------------------------------------------------------"""
import os, re

ofile = input("Please type a filename with extension in Resources Directory ")
text = os.path.join("Resources/",ofile)

with open (text, encoding = 'utf-8') as p_text:
    paragraph = p_text.read()
    word_count =  len(paragraph.split())  
    sentences = re.split("(?<=[.!?]) +", paragraph)
    sentence_count = len(sentences)
    letter_count = len(paragraph.replace(" ",""))

    av_letter_count = round(letter_count / word_count,1)
    av_sentence_length = word_count / sentence_count

    print(f"Paragraph Analysis ")
    print(f"--------------------------------")
    print(f"Approximate Word count : {word_count}")
    print(f"Approximate Sentence count : {sentence_count}")
    print(f"Average Letter count: {av_letter_count}")
    print(f"Average Sentence length: {av_sentence_length}")
