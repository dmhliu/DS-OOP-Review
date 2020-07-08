'''Player class to record stats for individual players
'''


class Player:
    '''Dosctring Parameters
    -----------------------------
    yards : int 
        
    name  : str
        
    touchdowns : int
        number of tds scored by this player TODO, clarify how player stats are bound to a game
    safety : int
        count of safeties scored  (offense)
    interceptions : int 
        count of interceptions made (defense)
    field_goals : int
        count of fgs made (offense)

=
    '''
    def __init__(self, name=None, yards=120, touchdowns=5, safety=1,
                 interceptions=0, field_goals=3):
        self.stats = {}

        self.stats['name'] = name             
        self.stats['yards'] = yards                # number of yards run
        self.stats['td'] = touchdowns      # int number of tds scored by player
        self.stats['safety'] = safety
        self.stats['interceptions'] = interceptions
        self.stats['field_goals'] = field_goals

    def get_points(self):
        '''Gets points scored by the player from stats
        '''
        td_points = 6 * self.stats['td']
        safety_points = 2 * self.stats['safety']
        total_points = td_points + safety_points
        return total_points


class Quarterback(Player):
    '''Override certain parameters of the default Player class and add some
    functionality unique to quarterbacks
    '''
    def __init__(self, name=None, yards=130, touchdowns=5, completed_passes=20,
                 interceptions=4, safety=None, field_goals=None):
        super().__init__(name=name, yards=yards, touchdowns=touchdowns,
                         safety=safety, interceptions=interceptions)
        self.completed_passes = completed_passes

    def passing_score(self):
        '''This is a random formula... FYI
        '''
        score = self.completed_passes - (2 * self.interceptions)
        return score

# TODO - refine the default player stats and/or make a defensive player default
# with number of tackles, sacks, interceptions etc.
class Receiver(Player):
    def __init__(self, name=None, yards=130, touchdowns=5, completed_passes=20,
                 interceptions=4, safety=None, field_goals=None):
        super().__init__(name=name, yards=yards, touchdowns=touchdowns,
                         safety=safety, interceptions=interceptions)
        self.completed_passes = completed_passes