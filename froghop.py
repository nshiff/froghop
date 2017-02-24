class Froghop:

    def __init__(self):
        pass

    def getSolution(self, stringToTest):

        has_lily_pad = '_' in stringToTest
        has_waterlogged = 'x' in stringToTest
        if (not has_lily_pad) and (not has_waterlogged):
            return -1

        elif has_lily_pad and (not has_waterlogged):
            return stringToTest

        elif (not has_lily_pad) and has_waterlogged:
            return stringToTest + '__'






        return False

