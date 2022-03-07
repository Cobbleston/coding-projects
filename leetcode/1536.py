# DA FINIRE

def minSwaps(grid):
    def possibleSwaps(grid):
        n = len(grid)
        pointsRow = []
        for k in range(0, n):
            p = 0
            i = 0
            while i < n and grid[k][n-1-i] == 0:
                p += 1
                i += 1
            pointsRow.append((p, k))

        #Verifico che sia possibile
        sortedPointsRow = sorted(pointsRow, reverse=True)
        possible = True
        h = n-1
        i = 0
        #print(sortedPointsRow)
        while i < n-1 and possible:
            print(sortedPointsRow[i][0], h)
            if sortedPointsRow[i][0] < h:
                possible = False
            h -= 1
            i += 1
        return possible


    res = 0
    if possibleSwaps(grid):
        .
    else:
        return -1

def printGrid(g):
    for r in g:
        print(r)
    print()


g = [[0,0,1],[1,1,0],[1,0,0]]
#g = [[0,1,1,0],[0,1,1,0],[0,1,1,0],[0,1,1,0]]
#g = [[1,0,0],[1,1,0],[1,1,1]]

printGrid(g)
print(minSwaps(g))