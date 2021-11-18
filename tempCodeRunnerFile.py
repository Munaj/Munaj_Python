    def __or__(self,other):
        if(self.percent >= other.percent):
            return self.percent
        else:
            return other.percent
        