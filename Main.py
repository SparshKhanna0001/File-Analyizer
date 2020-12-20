""""
Main operations this will offer:-
[1]Read the content of a file
[2]Append the file
[3]Count the words
[4]Calculate the character and ratio
[5]Count the number of lines 
[6]Word replacing feature
[7]MaKe a exit option, in case the user doesn't want to open another file
[8]Exception Handling

"""
import CharacterCounter
from CharacterCounter import char_count   #char_count returns char alongside its ratio in the text
                                          #from file
import Word_counter        #This module counts the words present in the file       
from Word_counter import list_of_words_from_text  #list_of_words_from_text returns list of valid words
import txtFileChecker           #the function in module checks whether the path provided is of txt file or not
times = 0

while True:       #This loop is there to enable this program to open and analise more than one text file.

    try:        # Basic level exception handling
                    
        description = "r - For reading the file"
        description1 = "c - For counting the words present in the file"
        description2 = "rc - For Knowing the ratio of each letter in the file."
        description3 = "a - For appending the File"
        description4 =  "h - For help/instruction-manual"
        description5 = "q - to exit this file and open new one."
        description6 = "wr - For replacing a word in the text file."

        """
        The code between line number 19 and line number 36 enables to checK that has the user opened
        any other file before or not. So, in case he has then the message printed will be different, 
        in case he hasn't the message printed will be different.
        """

        if times > 0:       
            consent = input("Well, if you are done! Then you can exit with [q]. To continue press anything\n>>>")
            if consent.lower() == "q":
                thanKs_msg = "ThanKs a lot for using our services...."
                print(thanKs_msg)
                exit()
        
            file = input("Enter the path of the file you want to open.\n>>> ")
            if txtFileChecker.check_txt_file(file) == False:
                print("The file you want to open is not a text file(.txt).\nThis program opens only text files.")
                print("Try opening text files.")
                consent = input("Do you want to try, if you want then press anything, if you want to quit press [q]\n>>>")
                if consent.lower() == "q":
                    exit()


        elif times == 0:
            file = input("Enter the path of the file you want to open and analyse. Don't forget to enter the file extension. \n>>>")
            if txtFileChecker.check_txt_file(file) == False:
                print("The file you want to open is not a text file(.txt).\nThis program opens only text files.")
                print("Try opening text files.")
                consent = input("Do you want to try, if you want then press anything, if you want to quit press [q]\n>>>")
                if consent.lower() == "q":
                    exit()

            print(description)
            print(description1)
            print(description2)
            print(description3)
            print(description4)
            print(description5)
            print(description6)
            times += 1
                    
        while True:
            operation = input("Tell the operation you want to execute.\n>>>")
            print("\n") 

            try:    # Exception Handling to prevent type error.
                
                if operation.lower() == 'r':    #Reads the text file
                    with open(file) as f:
                        text = f.read()

                    print(text)
                    del text
                
                elif operation.lower() == 'rc':     #Prints the char and its ratio present in text file
                    with open(file) as f:
                        text = f.read()
                    for char in "abcdefghijklmnopqrstuvwxyz":
                        print(CharacterCounter.char_count(char,text))
                    
                    del text

                elif operation.lower() == "c":     #Calculates the total number of words
                    
                    with open(file) as f:
                        text = f.read()

                    print(Word_counter.word_counter(text))
                    del text
                
                elif operation.lower() == 'a':      #For appending the file
                    appendment = input("Write what you want to append in the file.\n>>>")

                    with open(file, 'a') as f:
                        f.write(appendment)

                elif operation.lower() == 'h':      #Prints out the description, the valid instructions
                    print(description)
                    print(description1)
                    print(description2)
                    print(description3)
                    print(description4)
                    print(description5)
                    print(description6)

                elif operation.lower() == 'lc':       #line Count
                    with open(file) as f:
                        lines = list(f.readlines())
                        print(f'''So, there are {len(lines)} lines.''')
                        del lines

                elif operation.lower() == 'wr':
                    """Replaces a particular word given by user with another word also given by user as usual."""

                    f = open(file, "r+")
                    original_word:str = input("Tell the word you want to replace.\n>>>")
                    new_word:str = input("Tell the new word.\n>>>")
                    text = f.read()

                    try:
                        text = text.replace(original_word, new_word)
                        f.write(" ")
                        f.write(text)
                        f.close()
                        f = open(file, "r")
                        print("And below is the result...")
                        print("\n")
                        print(f.read())
                        f.close()
                    except:
                        print("The word you want to replace is already not in the text.")
                        print("You can try again....")
                    finally:
                        del text
                        f.close()
                    

                elif operation.lower() == 'q':  #For exiting the current file
                    break

                else:       #For invalid commands
                    print("I don't understand that...\nPlease try again!\n")
            except:
                print("An error occured...")
                print("Please try opening the file again.")
                print("And remember, this program opens only '.txt' files.")

    except:
        if txtFileChecker.check_txt_file(file) == False:
            exit()
        print("An error occured...")
        print("Please try opening the program again.")
        print("This program is going to end.....")
        exit()
