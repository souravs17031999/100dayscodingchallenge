import re
import sys
def cli_index(text):
    words = len(text.split())
    letters = 0
    for i in text:
        if i.isalpha() or i.isdigit():
            letters += 1
    sentences = len(re.findall('\w+[^?!.][?!.]', text))
    print(f"your text contains {words} words, {letters} letters and {sentences} sentences")
    L = (letters / words) * 100
    S = (sentences / words) * 100
    return round(0.0588 * L - 0.296 * S - 15.8)
if __name__ == '__main__':
    text = input().strip()
    result = cli_index(text)
    if result > 16:
        print(f"Coleman–Liau index for given text: Grade 16+")
    elif result < 1:
        print(f"Coleman–Liau index for given text: Before Grade 1")
    else:
        print(f"Coleman–Liau index for given text: Grade {result}")
