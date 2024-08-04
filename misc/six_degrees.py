# Six Degrees of Kevin Bacon

# https://www.codingame.com/ide/puzzle/six-degrees-of-kevin-bacon


import sys
import math
from collections import defaultdict

# 6 Degrees of Kevin Bacon!
m = defaultdict(list)
a = defaultdict(list)

actor_name = input()
n = int(input())

for i in range(n):
    movie_cast = input()
    movie = movie_cast.split(':')
    movie_name = movie[0]
    actors = movie[1].split(',')

    for actor in actors:
        actor = actor.strip()
        m[movie_name].append(actor)
        a[actor].append(movie_name)


def degrees(actor, n, cast):

    queue  = [(actor, 0)]

    while queue:
        current_actor, count = queue.pop(0)

        if current_actor == 'Kevin Bacon':
            return count
        else:
            neighbors = get_neighbors( current_actor)
        
            if neighbors: 
                for neighbor in neighbors:
                    queue.append((neighbor, count + 1))


def get_neighbors(actor):

    movies = a[actor]
    actors = []

    for movie in movies:
        actors += m[movie]

    return actors

print(degrees(actor_name, n, movie_cast))
