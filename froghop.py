class Froghop:

    def __init__(self):
        pass



    def _getFinalXSubscript(self, lilypadstring):
        start = 0
        for i in range(len(lilypadstring)):
            if lilypadstring[i] == 'x':
                start = i
        return start

    def _doesNaiveSolutionWork(self, lilypadstring):
        final_x_subscript = self._getFinalXSubscript(lilypadstring)
        cursor_position = final_x_subscript








        return cursor_position





    def getSolution(self, inputString):
        stringToTest = ''
        for character in inputString:
            stringToTest += character.lower()

        has_lily_pad = '_' in stringToTest
        has_waterlogged = 'x' in stringToTest
        if (not has_lily_pad) and (not has_waterlogged):
            return -1

        elif has_lily_pad and (not has_waterlogged):
            return stringToTest

        elif (not has_lily_pad) and has_waterlogged:
            return stringToTest + '__'

        solution = stringToTest
        i = 0
        while i < 100 and (not self._doesNaiveSolutionWork(solution)):
            solution += '_'
            i += 1
        return solution





