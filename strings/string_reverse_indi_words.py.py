# program to reverse individual words of string given as input (without using in-built split function)

# function to build custom split string into list of individual words
def split(text):
    # if there is nothing
    if len(text) == 0:
        return
    # if it has only one character
    if len(text) == 1:
        return [text[0]]
    # otherwise, go over till you hit 'whitespace', then we append the currently formed string to our list
    l = []
    s = text[0]
    for i in range(1, len(text)):
        # if this is not whitespace, then it is char of last started string, so adding it to string
        if text[i] != ' ':
            s = "".join((s, text[i]))sourav
        # if this is whitespace, so we got our word, then it is appended in list
        if text[i] == ' ':
            l.append(s)
            s = ''
        # if it is at the last index, simply append the last formed word to the list
        if i == len(text) - 1:
            l.append(s)
    return l

# function to reverse the overall string of words
def reverse(text):
    # split_text contains splitted text using whitespace as delimiter
    split_text = split(text)
    # going over each word, we can reverse it using string slicing
    for i in range(len(split_text)):
        split_text[i] = split_text[i][::-1]
    # finally returning the overall string by joining the splitted words into a single string
    return " ".join(split_text)

# main function
if __name__ == '__main__':
    input_text = input().strip()
    print(f'your input is : {input_text}')
    print(f'reversed output is : {reverse(input_text)}')
