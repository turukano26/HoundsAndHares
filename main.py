adjacencyDict = {
    0:{1,11,21},
    1:{0,11,12,2},
    2:{1,12,3},
    3:{2,12,13,4},
    4:{3,13,23},
    11:{0,1,12,21},
    12:{1,2,3,11,13,21,22,23},
    13:{3,4,12,23},
    21:{0,11,12,22},
    22:{12,21,23},
    23:{4,12,13,22}
}
houndBackwardRemovalDict = {
    0:{1,2,3,4,11,12,13,21,22,23},
    1:{2,3,4,12,13,22,23},
    2:{3,4,13,23},
    3:{4},
    4:{}
}

class GameState:
    def __init__(self, hare, hound1, hound2, hound3, turn):
        self.creatures = {
            "hare": hare,
            "hound1": hound1,
            "hound2": hound2,
            "hound3": hound3
        }
        self.turn = turn


intialState = GameState(0,3,4,23,"hare")


def haresPossibleMoves(gameState):
    moves = adjacencyDict[gameState.creatures["hare"]]
    
    for h in gameState.creatures:
        moves.discard(gameState.creatures[h])

    return moves


def houndsPossibleMoves(gameState):
    #creates list of all possible hound moves
    movesList = []
    #cycles through all the hounds
    for h in gameState.creatures:
        if h != "hare":
            #gets all spaces adjacent to the current hound
            moves = adjacencyDict[gameState.creatures[h]]
            #removes all spaces that another creature is occupying
            for c in gameState.creatures:
                moves.discard(gameState.creatures[c])
            #removes all spaces backwards from the hound
            moves.difference_update(houndBackwardRemovalDict[gameState.creatures[h] % 10])
            #adds this set to the movesList
            movesList.append([h,moves])

    return movesList

houndsPossibleMoves(intialState)