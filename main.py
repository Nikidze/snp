from lexer import Lexer

file = open('test.txt').read()

Lexer(file).tokenize()
