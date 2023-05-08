
#/****************************************************************/

#Read file and put into list

f = open("wordlist.txt", "r")
words = f.read()
word_list = words.split("\n")

#remove last word as it's just blank /n character
del(word_list[-1])

#This section of code used to sort words into lists,
#depending on their word length

max = 0
for i in word_list:
    if len(i) > max:
        max = len(i)

grand_list = []
for i in range(max):
    grand_list.append([])

for i in word_list:
    grand_list[len(i)-1].append(i)

print(grand_list[17])

#/****************************************************************/