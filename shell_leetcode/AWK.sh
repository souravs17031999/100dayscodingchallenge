'''
Awk is a scripting language used for manipulating data and generating reports.The awk command programming
language requires no compiling, and allows the user to use variables, numeric functions, string
functions, and logical operators.
Awk is a utility that enables a programmer to write tiny but effective programs in the form of statements
that define text patterns that are to be searched for in each line of a document and the action that
is to be taken when a match is found within a line. Awk is mostly used for pattern scanning and processing.
It searches one or more files to see if they contain lines that matches with the specified patterns and
then performs the associated actions.
'''


awk options 'selection _criteria {action }' input-file > output-file

'''
# Different data fields can be accessed separately:
$ awk '{print $1}' myfile

FIELDWIDTHS     Specifies the field width.

RS     Specifies the record separator.

FS     Specifies the field separator.

OFS  Specifies the Output separator.

ORS  Specifies the Output separator.

ARGC     Retrieves the number of passed parameters.

ARGV     Retrieves the command line parameters.

ENVIRON     Array of the shell environment variables and corresponding values.

FILENAME    The file name that is processed by awk.

NF     Fields count of the line being processed.

NR    Retrieves total count of processed records.

FNR     The record which is processed.

IGNORECASE     To ignore the character case.
'''

# -------------------------------------------------------------------------------------------

$ awk '

BEGIN{

test="Welcome to LikeGeeks website"

print test

}'

# -----------------------------------------------------------------------------------------
$ awk '{if ($1 > 30) print $1}' testfile
#
$ awk '{

if ($1 > 30)

{

x = $1 * 3

print x

} else

{

x = $1 / 2

print x

}}' testfile

#

$ awk '{

sum = 0

i = 1

while (i < 5)

{

sum += $i

i++

}

average = sum / 3

print "Average:",average

}' testfile

#

$ awk '{

tot = 0

i = 1

while (i < 5)

{

tot += $i

if (i == 3)

break

i++

}

average = tot / 3

print "Average is:",average

}' testfile

#
$ awk '{

total = 0

for (var = 1; var < 5; var++)

{

total += $var

}

avg = total / 3

print "Average:",avg

}' testfile

#

# There are other in-built functions which can be used along with user defined functions like mathematical functions.
