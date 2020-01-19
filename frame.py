class Frame:

    def __init__(self, sequence, begin):
        self.sequence = self.__clean(sequence)
        self.is_valid = all(map(lambda c: c != "N", self.sequence))
        self.begin = begin

    @staticmethod
    def __clean(seq):
        return seq.upper()
