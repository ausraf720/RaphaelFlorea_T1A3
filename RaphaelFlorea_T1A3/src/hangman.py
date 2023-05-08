
#Make the hangman class, which is template for hangman stages to be printed out
class hangman_stage:
    def __init__(self, lines):
        self.lines = lines

    def printer(self):
        for i in self.lines:
            print(i)



#Here, make the full hangman picture to be printed out, and gameover
lines = []
lines.append('_______ ')
lines.append('|    |  ')
lines.append('|    O  ')
lines.append('|   -|- ')
lines.append('|   / \ ')
lines.append('|_______')

stage10 = hangman_stage(lines)

stage10.printer()