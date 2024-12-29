require 'format/printf'

NB. `strsplit` taken from https://code.jsoftware.com/wiki/Phrases/Strings.
strsplit=: #@[ }.each [ (E. <;.1 ]) ,
contents =. 1!:1 <'data/2.txt'
lines =. (13 10 { a.) strsplit contents  NB. Windows newline = \r\n

parse_line =. verb : '". > y'
NB. Drop all zeroes from an array. We use this to drop only trailing zeros,
NB. but this works because none of the input lines contains a zero.
drop_zeros =: verb : 'y #~ 0 ~: y'

is_safe =: verb define
all_equal =: verb : '*/ y = {.y'
all_true =. verb : 'all_equal 1, y'
shifts =. }. y - |.!.0 y =. drop_zeros y
monotone =. all_equal signs =. * shifts
(all_true (1&<: *. 3&>:) | shifts) * monotone
)

'Part 1: %d' printf +/ is_safe"1 parse_line lines

NB. We don't need to check if the original array is safe, because if it was,
NB. then the arrays formed by dropping the first or last elements will be safe,
NB. and they'll show up in the "OR".
NB. `e. i. n` to generate the identity matrix for postiive integer `n` is taken
NB. from https://wiki.jsoftware.com/wiki/Essays/Identity_Matrix.
is_safe2 =. verb : '+./ is_safe"1 y #~ 1 - e.i.# y =. drop_zeros y'

'Part 2: %d' printf +/ is_safe2"1 parse_line lines
exit ''