from tokens import TokenType
from Exceptions import NonexistentToken


class Lexer:
    def __init__(self, file: str, space_symbol: str = ' ', point_symbol: str = '.'):
        self.file: str = file
        self.position: int = 0
        self.space_symbol: str = space_symbol
        self.point_symbol: str = point_symbol
        self.alphabet: list = [self.space_symbol, self.point_symbol]
        self.tokens = []

    def tokenize(self):
        while self.current() != TokenType.EOF:
            current = self.current()
            if current == self.space_symbol:
                self.addToken(self.tokenizeSpaces())
            if current == self.point_symbol:
                self.addToken(self.tokenizePoint())
            continue
        print(self.tokens, '\n')

    def countSpaces(self):
        current = self.current()
        count_spaces = 0
        while current == self.space_symbol:
            count_spaces += 1
            current = self.next()
        self.tokenizeDelimiter()
        return count_spaces

    def countPoints(self):
        current = self.current()
        count_points = 0
        while current == self.point_symbol:
            count_points += 1
            current = self.next()
        return count_points

    def tokenizePoint(self):
        count = self.countPoints()
        if count == 2:
            return self.tokenizeBracket()
        if count == 3:
            return self.tokenizeVar()
        if count == 4:
            return self.tokenizeEqOperator()
        if count == 5:
            return self.tokenizePositiveNumber()
        if count == 6:
            return self.tokenizeNegativeNumber()
        if count == 7:
            return self.tokenizeInput()
        if count == 8:
            return self.tokenizePrint()

    def tokenizeSpaces(self):
        count = self.countSpaces()
        if count == 1:
            return TokenType.IF
        elif count == 2:
            return TokenType.ELSE
        elif count == 3:
            return TokenType.WHILE
        elif count == 4:
            return TokenType.BREAK
        elif count == 5:
            return TokenType.CONTINUE
        elif count == 6:
            return TokenType.PLUS
        elif count == 7:
            return TokenType.MINUS
        elif count == 8:
            return TokenType.STAR
        elif count == 9:
            return TokenType.SLASH
        else:
            raise NonexistentToken

    def tokenizeBracket(self):
        spaces = self.countSpaces()
        if spaces == 1:
            return TokenType.LBRT
        if spaces == 2:
            return TokenType.RBRT

    def tokenizeVar(self):
        spaces = self.countSpaces()
        return [TokenType.VAR, spaces]

    def tokenizeEq(self):
        spaces = self.countSpaces()
        if spaces == 1:
            return TokenType.EQ

    def tokenizePositiveNumber(self):
        spaces = self.countSpaces()
        return [TokenType.NUMBER, spaces]

    def tokenizeNegativeNumber(self):
        spaces = self.countSpaces()
        return [TokenType.NUMBER, -spaces]

    def tokenizeEqOperator(self):
        spaces = self.countSpaces()
        if spaces == 1:
            return TokenType.EQ
        elif spaces == 2:
            return TokenType.LESS
        elif spaces == 3:
            return TokenType.MORE
        elif spaces == 4:
            return TokenType.EQEQ
        elif spaces == 5:
            return TokenType.NOTEQ

    def tokenizeInput(self):
        spaces = self.countSpaces()
        if spaces == 1:
            return TokenType.INPUTSPACES
        if spaces == 2:
            return TokenType.INPUTNUMBER

    def tokenizePrint(self, mode=1):
        spaces = self.countSpaces()
        if mode == 1:
            return [TokenType.PRINTSPACES, spaces]
        if mode == 2:
            return [TokenType.PRINTNUMBER, spaces]

    def tokenizeDelimiter(self):
        while self.current() != self.point_symbol:
            self.next()
        self.next()

    def addToken(self, token):
        self.tokens.append(token)

    def next(self, position: int = 1):
        self.position += position
        try:
            current = self.file[self.position]
        except IndexError:
            return TokenType.EOF
        if current not in self.alphabet:
            return self.next(position + 1)
        else:
            return current

    def current(self):
        return self.next(0)
