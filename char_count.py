"""
Total duration: 22:41
"""

import sys

from collections import Counter


def test_example():
    """
    test with the example given in the instructions
    (run with nose tests: nose zen.py)
    """
    in_string = "this is 1 string of text"
    expected = """1 1
e 1
f 1
g 1
h 1
i 3
n 1
o 1
r 1
s 3
t 4
x 1"""
    assert count_chars(in_string) == expected

def test_edge_cases():
    assert count_chars("") == ""
    assert count_chars(" \n\t\r") == ""
    assert count_chars("abbb") == "a 1\nb 3"

def count_chars(in_string):
    """
    analyze a string and print the counts of all non-whitespace characters.
    Output the counts by printing the character followed by its count on a line.
    Sort the output alphanumerically by the character.

    Future additions:
      - validate type of input
    """
    WHITESPACE = "\r\n\t "
    out_lines = []
    for char, count in sorted(Counter(in_string).items()):
        if char in WHITESPACE:
            continue
        out_lines.append("%s %s" % (char, count))
    return '\n'.join(out_lines)

def print_count_chars(in_string):
    """
    print the result
    """
    print count_chars(in_string)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        print_count_chars(sys.argv[1])