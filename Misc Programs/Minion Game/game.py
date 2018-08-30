class Minion:
    kevin_score = 0
    stuart_score = 0
    vowels = ['A', 'E', 'I', 'O', 'U']
    sub_strings = {}

    def process(self, string):
        print(len(string))
        string = memoryview(string.encode())
        for pos in range(0, len(string)):
            for alpha in range(pos, len(string)):
                if string[pos:alpha+1][0] in self.vowels:
                    self.kevin_score += 1
                    if string[pos:alpha + 1] not in self.sub_strings:
                        self.sub_strings[string[pos:alpha + 1]] = 1
                    else:
                        self.sub_strings[string[pos:alpha + 1]] += 1
                else:
                    self.stuart_score += 1
                    if string[pos:alpha + 1] not in self.sub_strings:
                        self.sub_strings[string[pos:alpha + 1]] = 1
                    else:
                        self.sub_strings[string[pos:alpha + 1]] += 1

    def custom_input(self):
        name = str(input("Enter the string for the game: "))
        self.process(name.upper())

    def output(self):
        # print("Values is : ")
        # print(self.sub_strings)
        # print("Stuart Score is: " + str(self.stuart_score))
        # print("Kevin Score is: " + str(self.kevin_score))
        if self.stuart_score > self.kevin_score:
            print("Stuart " + str(self.stuart_score))
        elif self.kevin_score > self.stuart_score:
            print("Kevin " + str(self.kevin_score))
        else:
            print("Draw")


if __name__ == '__main__':
    obj = Minion()
    obj.custom_input()
    obj.output()
