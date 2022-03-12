#coding:utf-8   
def incomodam(n):
    if n <= 0 or type(n) != int:
        return ''
    elif n == 1:
        return 'incomodam '
    else:
        return 'incomodam ' + incomodam(n - 1)

def elefantes(n, primeiro = True):
    if n < 1:
        return ''
    if n == 1:
        return 'Um elefante incomoda muita gente\n'

    if primeiro:
        return elefantes(n - 1, False) \
               + str(n) + ' elefantes ' + incomodam(n) + 'muito mais'
    else:
        return elefantes(n - 1, False) \
               + str(n) + ' elefantes ' + incomodam (n) + 'muito mais\n' \
               + str(n) + ' elefantes ' + incomodam (n) + 'muita gente\n'

#print(elefantes(4))