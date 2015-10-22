import re
def colour_coder(sentence):
    wordslist=re.sub(r'[^\w]',' ',sentence).split()
    langlist=['english', 'hindi', 'kannada','english', 'hindi', 'kannada']
    wordslist=zip(wordslist,langlist)
    return wordslist