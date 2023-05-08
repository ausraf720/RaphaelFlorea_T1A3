from copy import deepcopy

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

#/****************************************************************/


#Here, make the full hangman picture to be printed out, and gameover
lines = []
lines.append('_______ ')
lines.append('|    |  ')
lines.append('|    O  ')
lines.append('|   -|- ')
lines.append('|   / \ ')
lines.append('|_______')
stage_final = hangman_stage(lines)
stages = []

#Make a list of all the hangman stages
#Note, the list will be reversed at the end,
#as appending stages in backwards order
stages.append(stage_final)
old_stage = stage_final

#/****************************************************************/

#Now start adding all the other stages
#Need to build a function to avoid repeating code later

new_stage = deepcopy(old_stage)
new_stage.modify_line(4, '|   /   ')
stages.append(new_stage)
old_stage = new_stage

new_stage = deepcopy(old_stage)
new_stage.modify_line(4, '|       ')
stages.append(new_stage)
old_stage = new_stage

#Do initial tests
for i in stages:
    i.printer()