from enum import Enum, auto


class NoValue(Enum):
    def __repr__(self):
        return '<%s.%s>' % (self.__class__.__name__, self.name)


class TokenType(NoValue):
    EOF = auto()
    IF = auto()
    ELSE = auto()
    WHILE = auto()
    BREAK = auto()
    CONTINUE = auto()
    LBRT = auto()
    RBRT = auto()
    EQ = auto()
    PLUS = auto()
    MINUS = auto()
    STAR = auto()
    SLASH = auto()
    LESS = auto()
    MORE = auto()
    EQEQ = auto()
    NOTEQ = auto()
    INPUTSPACES = auto()
    INPUTNUMBER = auto()
    PRINTSPACES = auto()
    PRINTNUMBER = auto()
    VAR = auto()
    NUMBER = auto()
