from collections import Counter
from itertools import combinations
from players import *

class Game():

    def __init__(self, matches=10):
        self.matches = matches
        self.registry = Counter()

    def play(self, player1: Player, player2: Player):
        score_player1 = 0
        score_player2 = 0
        prev_action_player1 = 0
        prev_action_player2 = 0
        for i in range(self.matches):
            action_player1 = player1.action(prev_action_player2)
            action_player2 = player2.action(prev_action_player1)
            prev_action_player1 = action_player1
            prev_action_player2 = action_player2
            if (action_player1 == action_player2 == 1):
                score_player1 += 2
                score_player2 += 2
            elif (action_player1 == -1 and action_player2 == 1):
                score_player1 += 3
                score_player2 -= 1
            elif (action_player1 ==  1 and action_player2 == -1):
                score_player1 -= 1
                score_player2 += 3
        self.registry.update(Counter({player1.name:score_player1, player2.name:score_player2}))

    def top3(self):
        top3 = self.registry.most_common(3)
        for name, score in top3:
            print(name, score)


def single_play(players):
    print('=========================')
    game = Game()
    for player1, player2 in combinations(players, 2):
        game.play(player1, player2)
    print(dict(game.registry))
    game.top3()


def test1():
    all_players = [Cheater(), Cooperator(), Copycat(), Grudger(), Detective(),
                   Copycheat(), Twosavercoop(), Twosavercheat(), Random(),
                   Simpleton(), Copykitten()]
    for i in range(2, len(all_players)):
        for players in combinations(all_players, i):
            single_play(players)
    

def test2():
    players = [Cheater('Cheater1'), Cheater('Cheater2'), Cheater('Cheater3'), Cheater('Cheater4'),
               Cooperator('Cooperator1'), Cooperator('Cooperator2'), Cooperator('Cooperator3'),
               Cooperator('Cooperator4'),
               Copycat('Copycat1'), Copycat('Copycat2'), Copycat('Copycat3'), Copycat('Copycat4'),
               Grudger('Grudger1'), Grudger('Grudger2'), Grudger('Grudger3'), Grudger('Grudger4'),
               Detective('Detective1'), Detective('Detective2'), Detective('Detective3'),
               Simpleton('Simpleton1'), Simpleton('Simpleton2'), Simpleton('Simpleton3'),
               Copykitten('Copykitten1'), Copykitten('Copykitten2'), Copykitten('Copykitten3')]
    single_play(players)


def test3():
    all_players = [Cheater(), Cooperator(), Copycat(), Grudger(), Detective(),
                   Copycheat(), Twosavercoop(), Twosavercheat(), Random(),
                   Simpleton(), Copykitten()]
    single_play(all_players)


def main():
    # test1()
    # test2()
    test3()


if __name__ == '__main__':
    main()