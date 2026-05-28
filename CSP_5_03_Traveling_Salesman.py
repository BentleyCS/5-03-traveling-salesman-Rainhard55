import math
import random

import pygame
import itertools

def getPathDistance(places : list):
    #Given a list of x,y coordinates return the distance it would take to go to each coordinate
    # in order and then back to the start.
    dist = 0
    for i in range (len(places)-1):
        xi = places[i][0]
        yi = places[i][1]

        xf = places[i+1][0]
        yf = places[i+1][1]

        dist += math.sqrt(math.pow(xf - xi, 2) + math.pow(yf - yi, 2))


        return dist



def hueristic_TSP(places : list):

    bestroute = []
    calculations = 0

    current = places[0]

    bestroute.append(current)

    remaining = places.copy()
    remaining.remove(current)

    while len(remaining) > 0:

        closest = remaining[0]
        shortest = 999999

        for place in remaining:

            calculations += 1

            distance = math.sqrt((place[0] - current[0])**2 + (place[1] - current[1])**2)

            if distance < shortest:
                shortest = distance
                closest = place

        bestroute.append(closest)

        current = closest

        remaining.remove(closest)

    print(f"there were {calculations} calculations for heuristic TSP")


def generatePermutations(places : list):
    # a function that given a list will return all possible permutations of the list.
    return list(itertools.permutations(places))


def getDistance(spot1, spot2):
    #Given two coordinates in a plane return the distance between those two points.
    dist = math.sqrt((spot1[0] - spot2[0]) ** 2 + (spot1[1] - spot2[1]) ** 2)
    return dist

def generate_RandomCoordinates(n):
    #Creates a list of random coordinates
    newPlaces = []
    for i in range(n):
        newPlaces.append([random.randint(10,790),random.randint(10,590)])
    return newPlaces

places = [[80,75],[100,520],[530,300],[280,200],[350,150],[700,120],[400,500]]


def DrawExample(places):
    # Draws the TSP showcase to the screen.

    TSP = full_TSP(places.copy())
    Heuristic = heuristic_TSP(places.copy())  # fixed typo

    pygame.init()
    pygame.font.init()

    screen = pygame.display.set_mode((800, 800))
    pygame.display.set_caption("TSP Visualization")

    font = pygame.font.SysFont(None, 36)
    text_rect = (20, 750)

    clock = pygame.time.Clock()

    running = True

    while running:
        clock.tick(60)  # limits FPS to 60

        screen.fill((255, 255, 255))

        # Draw full TSP (red)
        if len(TSP) >= 2:
            for i in range(len(TSP) - 1):
                pygame.draw.line(screen, (255, 0, 0), TSP[i], TSP[i + 1], 5)
            pygame.draw.line(screen, (255, 0, 0), TSP[0], TSP[-1], 5)

        # Draw heuristic TSP (blue)
        if len(Heuristic) >= 2:
            for i in range(len(Heuristic) - 1):
                pygame.draw.line(screen, (0, 0, 255), Heuristic[i], Heuristic[i + 1], 3)
            pygame.draw.line(screen, (0, 0, 255), Heuristic[0], Heuristic[-1], 3)

        # Draw points
        for spot in places:
            pygame.draw.circle(screen, (0, 0, 0), (int(spot[0]), int(spot[1])), 6)

        # Legend text
        text_surface = font.render(
            "Red = Full TSP | Blue = Heuristic",
            True,
            (0, 0, 0)
        )
        screen.blit(text_surface, text_rect)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.flip()

    pygame.quit()

