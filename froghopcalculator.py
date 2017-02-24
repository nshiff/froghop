class FroghopCalculator:


    def getFinalXSubscript(self, lilypadstring):
        start = 0
        for i in range(len(lilypadstring)):
            if lilypadstring[i] == 'x':
                start = i
        return start

    def getFinalPosition(self, lilypadstring):
        finalPosition = 0
        i=0
        while i < len(lilypadstring):
            if lilypadstring[i] == 'x':
                return i - 1
            i += 1
        