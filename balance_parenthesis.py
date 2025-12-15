
"""
Course: GCIS 123 (2251)
Exam: Final Exam
Question: Question #3 (25 points)
Filename: balance_parenthesis.py

Complete the bracket balancing function below. It checks if (  and  ) brackets are balanced, using a stack.

Function returns 0 if brackets are balanced,
-1 if there are more closing brackets than needed,
and x otherwise, where x is the index of the most recent
unbalanced left bracket.

Examples:
"--(---(------)--"  returns  2 
"()----)" returns -1
"-----() -- ( () )" returns 0

"""
from node_stack import Stack

def balance_parenthesis(a_string):
    count_left=0
    count_right = 0
    savenumcount = -1
    savenum = 0
    for char in a_string:
        
        savenumcount += 1
        if char == "(":
            count_left += 1
            savenum = savenumcount
        if char == ")":
            count_right += 1
    if count_left > count_right:
        return savenum
    elif count_right > count_left:
        return -1
    elif count_left == count_right:
        return 0
    else:
        return "Error???"
        
 # please replace with your solution


def main():
    print(balance_parenthesis("()----)"))
    print(balance_parenthesis("--(---(-----)--"))
    print(balance_parenthesis("-------() -- ( () )"))

if __name__ == "__main__":    main()
