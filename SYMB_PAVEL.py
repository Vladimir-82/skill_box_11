def is_true(string):
    res = []
    for i in string:
        if i == '(':
            res.append('rnd')
        if i == '[':
            res.append('sqr')
        if i == '{':
            res.append('fig')
        if i == ')':
            if not res or res.pop() != 'rnd':
                return False
        if i == ']':
            if not res or res.pop() != 'sqr':
                return False
        if i == '}':
            if not res or res.pop() != 'fig':
                return False
    return True

string = '({}[{}]()'
print(is_true(string))