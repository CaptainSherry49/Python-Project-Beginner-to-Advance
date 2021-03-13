import re

"""
findall, search, split, sub, finditer
"""

my_str = """It's often used as a “scripting language” for web applications. This means that it can automate specific
series of tasks, making it more efficient. Consequently, 03102-1234 Python (and languages like it) is often used in 
software applications, pages within a 31529-1434 web browser, the shells of operating systems and some games."""

# ------------------ Meta Character ---------------------- #

# pattern = re.compile(r'used')
# pattern = re.compile(r'.tly')         # .	Any character (except newline character)	"he..o"
# pattern = re.compile(r"^It's")        # ^	Starts with	"^hello"
# pattern = re.compile(r'games.$')      # $	Ends with	"world$"
# pattern = re.compile(r'en*')          # *	Zero or more occurrences	"aix*"
# pattern = re.compile(r'en+')          # +	One or more occurrences	"aix+"
# pattern = re.compile(r'in{1}')        # {}	Exactly the specified number of occurrences	"al{2}"
# pattern = re.compile(r'in|it')          # |	Either or	"falls|stays"
# pattern = re.compile(r'(in a)')          # ()	Capture and group

# ---------------- Note ---------------- #
# r' ' == ya ham is liya use kar raha ha q k andar likhna sa special sequence character bhi print hojata ha


# ------------------------ Special Sequences ------------------------- #

"""
pattern = re.compile(r"\AIt's")   #  \A	Returns a match if the specified characters are at the beginning of the string	
"\AThe"


pattern = re.compile(r"\b a")  #\b	Returns a match where the specified characters are at the beginning or at the end of
a word	r"\bain"

"""

pattern = re.compile(r"\d{5}-\d{4}")

matches = pattern.finditer(my_str)

for match in matches:
    print(match)
