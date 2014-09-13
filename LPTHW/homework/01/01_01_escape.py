# Print out some useful information."
# How about the list of escape sequences from lesson 10."
print "\nEscape:\t\tWhat it does:"
the_list = """
\\\ \t\tBackslash(\)
\\'\t\tSingle-quote(')
\\"\t\tDouble-quote(")
\\a\t\tASCII bell(BEL)
\\b\t\tASCII backspace(BS)
\\f\t\tASCII formfeed(FF)
\\n\t\tASCII linefeed(LF)
\\N{name}\tCharacter named name in the Unicode database(Unicode only)
\\r\t\tASCII carriage return(CR)
\\t\t\tASCII horizontal tab(TAB)
\\uxxxx\t\tCharacter with 16-bit hex value xxxx(Unicode only)
\\Uxxxxxxxx\tCharacter with 32-bit hex value xxxxxxxx(Unicode only)
\\v\t\tASCII vertical tab(VT)
\\ooo\t\tCharacter with octal value oo
\\xhh\t\tCharacter with hex value hh
"""
print the_list
