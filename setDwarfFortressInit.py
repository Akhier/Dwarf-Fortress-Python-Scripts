#Modifies the init and d_init files for Dwarf Fortress (file must be in same folder as init files)
#Version Changelog:
#1.0 Completed Jan-22-2015 by Akhier Dragonheart
#1.1 Missed semicolons on second if stack
import re

d_init = open('d_init.txt')
file1 = []
for line in d_init:
    if re.match(r'(\[AUTOSAVE:)', line):
        file1.append('[AUTOSAVE:SEASONAL]\n')
    elif re.match(r'(\[AUTOB)', line):
        file1.append('[AUTOBACKUP:YES]\n')
    elif re.match(r'(\[AUTOSAVE_)', line):
        file1.append('[AUTOSAVE_PAUSE:YES]\n')
    elif re.match(r'(\[INI)', line):
        file1.append('[INITIAL_SAVE:YES]\n')
    elif re.match(r'(\[PAU)', line):
        file1.append('[PAUSE_ON_LOAD:YES]\n')
    elif re.match(r'(\[POP)', line):
        file1.append('[POPULATION_CAP:50]\n')
    elif re.match(r'(\[STR)', line):
        file1.append('[STRICT_POPULATION_CAP:60]\n')
    elif re.match(r'(\[B)', line):
        file1.append('[BABY_CHILD_CAP:10:10]\n')
    elif re.match(r'(\[V)', line):
        file1.append('[VARIED_GROUND_TILES:YES]\n')
    elif re.match(r'(\[EN)', line):
        file1.append('[ENGRAVINGS_START_OBSCURED:YES]\n')
    elif re.match(r'(\[SHOW_F)', line):
        file1.append('[SHOW_FLOW_AMOUNTS:YES]\n')
    else:
        file1.append(line)
d_init.close()
new_d_init = open('d_init.txt', 'w')
for item in file1:
    new_d_init.write(item)
new_d_init.close()
init = open('init.txt')
file2 = []
for line in init:
    if re.match(r'(\[SO)', line):
        file2.append('[SOUND:NO]\n')
    elif re.match(r'(\[I)', line):
        file2.append('[INTRO:NO]\n')
    elif re.match(r'(\[FPS:)', line):
        file2.append('[FPS:YES]\n')
    elif re.match(r'(\[FPS_)', line):
        file2.append('[FPS_CAP:120]\n')
    elif re.match(r'(\[MA)', line):
        file2.append('[MACRO_MS:0]\n')
    else:
        file2.append(line)
init.close()
new_init = open('init.txt', 'w')
for item in file2:
    new_init.write(item)
new_init.close()