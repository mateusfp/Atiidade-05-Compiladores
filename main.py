# Test it out
from lx import lexer

data = '''
4.1
MATEUS
;
=
'''

# Give the lexer some input
lexer.input(data)


# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break  # No more input
    print(tok)