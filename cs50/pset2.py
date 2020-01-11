import sys
import random
def cipher_text(text, key):
    cipher_text = ""
    text = text.upper()
    for i in range(len(text)):
        if text[i].isalpha():
            cipher_text += chr(((ord(text[i]) + key - 65) % 26) + 65)
        else:
            cipher_text += text[i]
    print(f"secured text is :     {cipher_text}")
    return text

def decipher_text(text, key):
    decipher_text = ""
    for i in range(len(text)):
        decipher_text += chr(((ord(text[i]) - key - 65) % 26) + 65)
    print(f"decipher text is :    {text}")

if __name__ == '__main__':
    key = random.randint(-sys.maxsize-1, sys.maxsize)
    raw_text = input().strip()
    print(f"raw text is  :        {raw_text}")
    if len(raw_text):
        decipher_text(cipher_text(raw_text, key), key)
    else:
        print('Please enter something !')
