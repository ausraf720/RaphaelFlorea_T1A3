
#Make the hangman class, which is template for hangman stages to be printed out
class hangman_stage:
    def __init__(self, lines):
        self.lines = lines

    #Prints everything out
    def printer(self):
        for i in self.lines:
            print(i)

    #Modifies individual line of hangman output
    def modify_line(self, line_index, new_line):
        self.lines[line_index] = new_line



#Here, make the full hangman picture to be printed out, and gameover
lines = []
lines.append('_______ ')
lines.append('|    |  ')
lines.append('|    O  ')
lines.append('|   -|- ')
lines.append('|   / \ ')
lines.append('|_______')

#Test all of above code is working
stage10 = hangman_stage(lines)
stage9 = stage10
stage9.modify_line(4, '|   /   ')

#Testing to see how by copying stage9 from stage10,
#stage10 now produces same result as stage9
stage9.printer()
stage10.printer()