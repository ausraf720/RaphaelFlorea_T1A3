
#/****************************************************************/

#Read file and put into list
def wordlist_opener():
    f = open("wordlist.txt", "r")
    words = f.read()
    word_list = words.split("\n")

    #remove last word as it's just blank /n character
    del(word_list[-1])
    return word_list

#/****************************************************************/

#This section of code used to sort words into lists,
#depending on their word length

def grand_list_builder(word_list):
    max_word_len = 0
    for i in word_list:
        if len(i) > max_word_len:
            max_word_len = len(i)

    #Grand list is a 2d list, 
    #each list contains words only of a certain length
    grand_list = []
    for i in range(max_word_len):
        grand_list.append([])

    for i in word_list:
        grand_list[len(i)-1].append(i)
    return grand_list

#/****************************************************************/
