# A melee Attack class capable of imbuing mana into themselves or weapons to
# make them stronger. Geared towards fast, one-on-one, quick bursts of 
# magic in the middle of combat.
class Augmenter:

    def __init__(self,health_points,
                attack_points,defense_points,speed_points,
                mana_level,iq_points,mastery_multiplier,unknown_potential):

        self.health_points = health_points
        self.attack_points = attack_points
        self.defense_points = defense_points
        self.speed_points = speed_points
        self.mana_level = mana_level
        self.iq_points = iq_points
        self.mastery_multiplier = mastery_multiplier
        self.unknown_potential = unknown_potential

    def char_stats(self):
        self.health_points = 750
        self.attack_points = 710
        self.defense_points = 820
        self.speed_points = 800
        self.mana_level = 600
        self.iq_points = 650
        self.mastery = 500
        self.unknown_potential = 0


#A long range Combat/Support class capable of ensuing massive levels of
# damage by conjuring up powerful spells from a farther distance. Have a high attack
# potency that is balanced out by low health and speed
class Conjurer:

    def __init__(self,health_points,
                attack_points,defense_points,speed_points,
                mana_level,iq_points,mastery_multiplier,unknown_potential):

        self.health_points = health_points
        self.attack_points = attack_points
        self.defense_points = defense_points
        self.speed_points = speed_points
        self.mana_level = mana_level
        self.iq_points = iq_points
        self.mastery_multiplier = mastery_multiplier
        self.unknown_potential = unknown_potential

    def char_stats(self):
        self.health_points = 600
        self.attack_points = 830
        self.defense_points = 740
        self.speed_points = 500
        self.mana_level = 800
        self.iq_points = 770
        self.mastery = 500
        self.unknown_potential = 0


# TBD
class Medeian:

    def __init__(self,health_points,
                attack_points,defense_points,speed_points,
                mana_level,iq_points,mastery_multiplier,unknown_potential):

        self.health_points = health_points
        self.attack_points = attack_points
        self.defense_points = defense_points
        self.speed_points = speed_points
        self.mana_level = mana_level
        self.iq_points = iq_points
        self.mastery_multiplier = mastery_multiplier
        self.unknown_potential = unknown_potential

    def char_stats(self):
        self.health_points = 900
        self.attack_points = 900
        self.defense_points = 900
        self.speed_points = 900
        self.mana_level = 900
        self.iq_points = 900
        self.mastery = 900
        self.unknown_potential = 0
