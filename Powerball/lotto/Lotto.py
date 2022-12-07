import random
from Powerball.lotto import colors

class chance:
    def __init__(self):
        self.winnernumber = []
        self.tiketholdernumber = []
        self.pick = random.randint(1, 10)
        self.pball = random.randint(1, 10)

    def choose(self):
        for i in range(5):
            rnum1 = random.randint(1, 20)
            self.tiketholdernumber.append(rnum1)
            rnum2 = random.randint(1, 20)
            self.winnernumber.append(rnum2)


class union(chance):
    def display(self):
        print("Today’s Powerball winning numbers:", colors.YELLOW, self.winnernumber, colors.MAGENTA, self.pball, colors.RESET)
        print("your lucky numbers:", colors.YELLOW, self.tiketholdernumber, colors.MAGENTA, self.pick)

    def winner(self):
        union_set = len(set(self.winnernumber).intersection(set(self.tiketholdernumber)))
        if union_set == 5 and self.pick == self.pball:
            print(colors.YELLOW, "Correct White Balls and the Powerball: Jackpot $324,000,000")
        elif union_set == 5 and self.pick != self.pball:
            print(colors.WHITE, "5 Correct White Balls, but no Powerball: $1,000,000")
        elif union_set == 4 and self.pick == self.pball:
            print(colors.GREEN, "4 Correct White Balls and the Powerball: Jackpot $10,000")
        elif union_set == 4 and self.pick != self.pball:
            print(colors.WHITE, "4 Correct White Balls, but no Powerball: $100")
        elif union_set == 3 and self.pick == self.pball:
            print(colors.BLACK, "3 Correct White Balls and the Powerball: Jackpot $100")
        elif union_set == 3 and self.pick != self.pball:
            print(colors.CYAN, "3 Correct White Balls, but no Powerball: $7")
        elif union_set == 2 and self.pick == self.pball:
            print("2 Correct White Balls and the Powerball: $7")
        elif union_set == 1 and self.pick == self.pball:
            print(colors.WHITE, "1 Correct White Ball and the Powerball: $4")
        elif union_set == 0 and self.pick == self.pball:
            print(colors.WHITE, "No White Balls, Just the Powerball: $4")
        else:
            print(colors.RED, "You are not lucky ! \n ",colors.BLUE," You will be lucky one day!\n  ",
                  colors.RED,"Try again!\n",colors.GREEN,"  Thanks")




