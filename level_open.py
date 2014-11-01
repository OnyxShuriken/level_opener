#!/usr/bin/python3
__author__ = 'Cole'

#Copyright Cole Gosney 2014
#Level opener

level_data = {}

level_x = 0

level_y = 0

def def_levels(level_list, line_length, number_of_lines):
    global level_data, level_x, level_y
    level_data = level_list
    level_x = line_length
    level_y = number_of_lines

def load_level(level_no):
    temp = []
    level = []

    f = open(level_data[level_no])
    
    for a in range(0, level_y):
        for b in range(0, level_x + 1):
            c = f.read(1)
            if c == "\n" or c == "":
                pass
            else:
                temp.append(c)
        level.append(temp)
        temp = []
        
    f.close()
    
    return level
