# Program to implement custom split function.
# It handles all the corner cases for all the delimiters like for ex. : ";;asbabs;;;;;fkb;;;" / ";;;;;;;;" / "geeks;geeks;sourav" etc.. for delim ";"
# Modify the below code as per the needs 
# TIME : 0(N), N IS LENGTH OF STRING.

def split(s, delim):
    
    split_text = [] # contains all the individual strings separated from delimiter 
    word = "" # temporary strings inside the complete text (denoted by s)
    ptr = 0 # pointer to the current char inside (s)
    
    # going char by char for the entire string 
    while ptr < len(s):
        
        # if it is not delim, then we need to append it to the running word string 
        if s[ptr] != delim:
            word = "".join((word, s[ptr]))
        else:   
            # now it handles the case for multiple occurences of delim consecutive, and also if string starts with delim
            while ptr < len(s) and s[ptr] == delim:
                ptr += 1
            ptr -= 1
            # at this point, we have complextely formed the word separated from delim, simply append to list
            split_text.append(word)
            # we need to reset it back to construct new string (if any)
            word = ""
        
        # for considering last string (word)
        if ptr == len(s) - 1:
            split_text.append(word)
        ptr += 1
    
    return split_text
