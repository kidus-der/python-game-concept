# this class will have all the actions a player in the game
# can do during a round


class Player:
    def __init__(self,attack,defend,move,mastery,
                x_variable):

        self.attack = attack
        self.defend = defend
        self.move = move
        self.mastery = mastery
        self.x_variable = x_variable

    def attack_opps(self, hit_opps):

        
