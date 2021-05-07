#! /usr/bin/env python3
# coding: utf-8

from TournamentApp.models.tournament import Tournament
from TournamentApp.models.player import Player

p1 = Player('Nico', 'Dem', '30/09/1988', 'M', 1)
p2 = Player('Nico', 'Dem', '11/03/1959', 'F', 2)
p3 = Player('Gwi', 'Dem', '16/06/1987', 'M', 5)
p4 = Player('AL', 'Dem', '21/03/1994', 'F', 15)
p5 = Player('Eric', 'Dem', '11/01/1954', 'M', 21)
p6 = Player('Annie', 'Dem', '13/10/1932', 'F', 7)
p7 = Player('Almire', 'lesco', '26/04/2018', 'M', 33)
p8 = Player('Constant', 'lesco', '21/04/1988', 'M', 4)
liste_joueurs = [p1, p2, p3, p4, p5, p6, p7, p8]

tournoi = Tournament('tournoi', 'ici', 4, 'bullet', 'rien de précis')

for el in liste_joueurs:
    el.points = 0
    tournoi.add_players(el)

tournoi.set_first_round()

for el in tournoi.rounds[0].matchs:
    print(el.get_match)

p1.points += 10
p6.points += 0

print(tournoi.all_possible_pairs - tournoi.match_already_done)

tournoi.rounds[0].matchs[0].points_p1 = p1.points
print(tournoi.rounds[0].matchs[0].get_match)