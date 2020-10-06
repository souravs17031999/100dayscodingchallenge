# Program to implement custom split function.
# It handles all the corner cases for all the delimiters like for ex. : ";;asbabs;;;;;fkb;;;" / ";;;;;;;;" / "geeks;geeks;sourav" etc.. for delim ";"
# Modify the below code as per the needs 
# Here, we assume if string is started using delim or ended using delim, then we ignore that and if we in any case we want that it can be simply added on top of it.
# TIME : 0(N), N IS LENGTH OF STRING.

def split(s, delim):
    
    split_text = [] # contains all the individual strings separated from delimiter 
    word = "" # temporary strings inside the complete text (denoted by s)
    ptr = 0 # pointer to the current char inside (s)
    

    while ptr < len(s):
        
        if s[ptr] != delim:
            word = "".join((word, s[ptr]))
        else:   
            if word != "":
                split_text.append(word)
                
            word = ""
        
        # handles corner case for last word formed but shouldn't be equal to delim
        if ptr == len(s) - 1 and s[ptr] != delim:
            split_text.append(word)
            
        ptr += 1
    
    return split_text
