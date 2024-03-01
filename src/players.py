import random

class Player():

    def __init__(self, name: str = None):
        self.name: str = name
        self.my_action: int = 0
    
    def cheating(self):
        self.my_action = -1

    def cooperating(self):
        self.my_action = 1


class Cheater(Player):

    def __init__(self, name='Cheater'):
        super().__init__(name)

    def action(self, prev_action_opponent):
        super().cheating()
        return self.my_action


class Cooperator(Player):

    def __init__(self, name='Cooperator'):
        super().__init__(name)

    def action(self, prev_action_opponent):
        super().cooperating()
        return self.my_action



class Copycat(Player):

    def __init__(self, name='Copycat'):
        super().__init__(name)

    def action(self, prev_action_opponent):
        if prev_action_opponent == 0:
            super().cooperating()
            return self.my_action 
        else:
            return prev_action_opponent


class Grudger(Player):

    def __init__(self, name='Grudger'):
        super().__init__(name)
    
    def action(self, prev_action_opponent):
        if prev_action_opponent == 0:
            super().cooperating()
        if prev_action_opponent == -1:
            super().cheating()
        return self.my_action
        
class Detective(Player):

    def __init__(self, name='Detective'):
        super().__init__(name)
        self.count_prev_action = 0
        self.first_action = [1, -1, 1, 1]
        self.deceived = False

    def action(self, prev_action_opponent: int):
        if prev_action_opponent == 0:
            self.count_prev_action = 0
            self.deceived = False
        if self.count_prev_action < 4:
            answer = self.first_action[self.count_prev_action]
            if prev_action_opponent == -1:
                self.deceived = True
        else:
            if self.deceived:
                answer = prev_action_opponent
            else:
                super().cheating()
                answer = self.my_action
        self.count_prev_action += 1
        return answer
    
class Copycheat(Player):

    def __init__(self, name='Copycheat'):
        super().__init__(name)

    def action(self, prev_action_opponent):
        if prev_action_opponent == 0:
            super().cheating()
            return self.my_action 
        else:
            return prev_action_opponent

class Twosavercoop(Player):

    def __init__(self, name='Twosavercoop'):
        super().__init__(name)
        self.count_prev_action = 0
        self.save_opponent_action = [0, 0]

    def action(self, prev_action_opponent: int):
        if prev_action_opponent == 0:
            self.count_prev_action = 0
            self.save_opponent_action = [0, 0]
            super().cooperating()
        if self.count_prev_action > 0 and self.count_prev_action < 3:
            self.save_opponent_action[self.count_prev_action - 1] = prev_action_opponent
            super().cooperating()
        if self.save_opponent_action[0] == self.save_opponent_action[1] == 1:
            super().cooperating()
        elif self.save_opponent_action[0] == self.save_opponent_action[1] == -1:
            super().cheating()
        elif self.save_opponent_action[0] == 1 and self.save_opponent_action[1] == -1:
            if self.count_prev_action < 4:
                super().cheating()
            else:
                super().cooperating()
        self.count_prev_action += 1
        return self.my_action

class Twosavercheat(Player):

    def __init__(self, name='Twosavercheat'):
        super().__init__(name)
        self.count_prev_action = 0
        self.save_opponent_action = [0, 0]

    def action(self, prev_action_opponent: int):
        if prev_action_opponent == 0:
            self.count_prev_action = 0
            self.save_opponent_action = [0, 0]
            super().cheating()
        if self.count_prev_action > 0 and self.count_prev_action < 3:
            self.save_opponent_action[self.count_prev_action - 1] = prev_action_opponent
            super().cheating()
        if self.save_opponent_action[0] == self.save_opponent_action[1] == 1:
            super().cooperating()
        elif self.save_opponent_action[0] == self.save_opponent_action[1] == -1:
            super().cheating()
        elif self.save_opponent_action[0] == 1 and self.save_opponent_action[1] == -1:
            if self.count_prev_action < 4:
                super().cheating()
            else:
                super().cooperating()
        self.count_prev_action += 1
        return self.my_action

class Random(Player):

    def __init__(self, name='Random'):
        super().__init__(name)

    def action(self, prev_action_opponent: int):
        rnd = random.randint(0, 1)
        if rnd == 0:
            super().cheating()
        else:
            super().cooperating()
        return self.my_action
    
class Simpleton(Player):

    def __init__(self, name='Simpleton'):
        super().__init__(name)
    
    def action(self, prev_action_opponent: int):
        if prev_action_opponent == 0:
            super().cooperating()
        elif prev_action_opponent == -1:
            self.my_action *= -1
        return self.my_action

class Copykitten(Player):

    def __init__(self, name='Copykitten'):
        super().__init__(name)
        self.count_prev_action = 0
        self.deceived = []

    def action(self, prev_action_opponent):
        if prev_action_opponent == 0:
            super().cooperating()
            self.count_prev_action = 0
            self.deceived = []
        else:
            if prev_action_opponent == -1:
                self.deceived.append(True)
                if len(self.deceived) > 1:
                    if self.deceived[-2]:
                        super().cheating()
            else:
                self.deceived.append(False)
                super().cooperating()
        return self.my_action