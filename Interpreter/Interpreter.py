INTEGER, PLUS, EOF = 'INTEGER', 'PLUS', 'EOF'

class Token(object):
    def __init__(self,type,value):
        # token type: INTEGER, PLUS, or EOF
        self.type = type
        # token value: 0,1,2. 3,4,5,6,7,8,9 '+', or None
        self.value = value

    def __str__(self):
        return 'Token({type},{value})'.format(
            type=self.type,
            value=repr(self.value)
        )
    
    def __repr__(self):
        return self.__str__()
    

class Interpreter(object):
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.current_token = None

    def get_next_token(self):

        text = self.text

        if self.pos > len(text) - 1:
            return Token(EOF,None)
        
        current_char = text[self.pos]

        if current_char.isdigit():
            token = Token(INTEGER, int(current_char))
            self.pos += 1
            return token
        
        if current_char == '+':
            token = Token(PLUS,current_char)
            self.pos += 1
            return token
        self.error()
    