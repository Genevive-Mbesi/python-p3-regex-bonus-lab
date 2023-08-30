import re

my_pattern = r""
my_regex = re.compile(my_pattern)
my_pattern = r"[^\s].*today.*"
my_regex = re.compile(my_pattern, re.MULTILINE)
