load 'regex'
require 'format/printf'
contents =. 1!:1 <'data/1.txt'
words =. > '\S+' rxall contents
numbers =. ((-: # numbers) , 2) $ numbers =. ". words
sort =. /:~
left =. sort {."1 numbers
right =. sort {:"1 numbers
'Part 1: %d' printf +/ | left - right
'Part 2: %d' printf +/ left * +/"1 left =/ right
exit ''