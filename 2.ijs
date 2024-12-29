require 'format/printf'
NB. `strsplit` taken from https://code.jsoftware.com/wiki/Phrases/Strings.
strsplit=: #@[ }.each [ (E. <;.1 ]) ,
contents =. 1!:1 <'2.txt'
lines =. (13 10 { a.) strsplit contents  NB. Windows newline = \r\n
safe =. verb define
all_equal =. verb : '*/ y = {. y'
line =. ". > y
shifts =. }. line - |.!.0 line
monotone =. all_equal signs =. * shifts
(all_equal (1&<: *. 3&>:) | shifts) * monotone
)
'Part 1: %d' printf +/ safe"0 lines
exit ''