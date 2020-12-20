def char_count(char, text):

    """
    So, this function will taKe a charater and the text as a parameter to caculate 
    the ratio of the character in the text upto 2 decimal places.
    """
    ratio = round(text.count(char)/len(text), 2)        #ratio is being calculated here
    return f"{char}-{ratio}"
