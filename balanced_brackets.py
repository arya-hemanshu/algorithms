
# To check if the brackets in a program are balanced or not
# The program expects a string as an input and 
# return True if the brackets are closed in a proper order 
# else returns False

opening = ['{','[','(']
closing = ['}',']',')']

def are_brackets_balanced(brackets):
    expected = []
    for index, b in enumerate(brackets):
        if b in opening:
            i = opening.index(b)
            if index == 0:
                expected.append(b)
                expected.append(closing[i])
            else:
                expected = expected[:index] + [b, closing[i]] + expected[index:]
        else:
            if ''.join(expected[:index+1]) != brackets[:index+1]:
                return False
    return True


s = '{[({[()()][]})]}'
print(are_brackets_balanced(s))