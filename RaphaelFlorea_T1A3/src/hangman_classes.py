#/***********************************************************************************************/

from copy import deepcopy

#Make the hangman class, 
#which is template for hangman stages to be printed out
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

    """This builds on previous function
        It deep-copies the previous hangman stage,
        then modifies line of next stage and adds it to list of stages"""
    def stage_adder(self, stages, line_index, new_line):
        new_stage = deepcopy(self)
        new_stage.modify_line(line_index, new_line)
        stages.append(new_stage)
        return new_stage

#/***********************************************************************************************/


#Here, make the full hangman picture to be printed out
def stages_initialiser():
    lines = []
    lines.append('_______ ')
    lines.append('|    |  ')
    lines.append('|    O  ')
    lines.append('|   -|- ')
    lines.append('|   / \ ')
    lines.append('|_______')

    #Make first instance of hangman_stage class
    stage10 = hangman_stage(lines)

    #Make a list of all the hangman stages
    """Note, the list will be reversed at the end,
        as appending stages in backwards order"""
    stages = []
    stages.append(stage10)
    return stages

#/***********************************************************************************************/

#Now start adding all the other stages, using 'stage_adder'
def stage_builder(stages):
    stage10 = stages[0]
    stage9 = stage10.stage_adder(stages, 4, '|   /   ')
    stage8 = stage9.stage_adder(stages, 4, '|       ')
    stage7 = stage8.stage_adder(stages, 3, '|   -|  ')
    stage6 = stage7.stage_adder(stages, 3, '|    |  ')
    stage5 = stage6.stage_adder(stages, 3, '|       ')
    stage4 = stage5.stage_adder(stages, 2, '|       ')
    stage3 = stage4.stage_adder(stages, 1, '|       ')
    stage2 = stage3.stage_adder(stages, 0, '        ')

    #stage1 needs to remove vertical left column of hangman picture,
    #Thus, call modify_line function directly to remove from each line
    stage1 = deepcopy(stage2)
    for i in range(1,5):
        stage1.modify_line(i, '        ')
    stage1.modify_line(5, ' _______')
    stages.append(stage1)

    #Finally create initial blank stage
    stage0 = stage1.stage_adder(stages, 5, '        ')
    stages.append(stage0)
    return stages

#/***********************************************************************************************/
