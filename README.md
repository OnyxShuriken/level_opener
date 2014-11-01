Level Opener
============
###A file that is capable of reading a tile-based map file and exporting the tiles in a drawable and friendly list.

###Requires:
* Python 3.x

###Usage:
First, import the file into your program.
```
import level_open
```
Now you will need the names of your level files. Add them to an ascending dictionary, like so:
```
my_levels = {1:'levelone.txt', 2:'leveltwo.txt', 3:'levelthree.txt'}
```
Now call level_open.def_levels which takes the following arguments:
* level_list will be your level file dictionary (my_levels in this case); 
* line_length will be how much data is in one line; 
* number_of_lines will be how many lines there are.
An example with 6 peices of data per line and 6 lines of data would be:
```
level_open.def_levels(my_levels, 6, 6)
```
Now we can read the level. To do this, we will need to call level_open.load_level with the number corresponding the level from our dictionary.
An example for loading the first level in our dictionary ('levelone.txt' in this case) would be:
```
level = level_open.load_level(1)
```
Now we print the list and will get something like (assuming all six lines of data contain 1-6):
```
[[1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6]]
```
This will allow you to draw the data onto tiles. You would have to loop through each line to get its data, and then do something with that data per tile. An example where each tile is drawn with its number would produce:
```
[1] [2] [3] [4] [5] [6]
[1] [2] [3] [4] [5] [6]
[1] [2] [3] [4] [5] [6]
[1] [2] [3] [4] [5] [6]
[1] [2] [3] [4] [5] [6]
[1] [2] [3] [4] [5] [6]
```
