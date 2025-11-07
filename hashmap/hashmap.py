class HashMap:
    def __init__(self, size=10):
        self.size = size
        self.map = [[] for _ in range(size)]
