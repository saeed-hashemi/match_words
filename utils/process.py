
def matching(grid, pattern, x, y,
             nrow, ncol, level):
    """
    Function to check if a word exists in a grid starting from the first
    match in the grid level: index till which pattern is matched x, y: current
    position in 2D array

    Prameters
    -----------------------
    grid: list -> 2d Grid of characters
    pattern: str -> word
    x: int -> x of current pointer
    y: int -> y of current pointer
    nrow: int -> shape of grid
    ncol: int -> shape of grid
    level: int -> position of current pointer in the word

    Returns
    -----------------------
    Boolean -> if matched True else false
    """
    l = len(pattern)

    # matched
    if (level == l):
        return True

    # Boundary check
    if (x < 0 or y < 0 or
            x >= nrow or y >= ncol):
        return False
    # Recursion
    if (grid[x][y] == pattern[level]):

        temp = grid[x][y]
        grid[x].replace(grid[x][y], "-")

        res = (matching(grid, pattern, x - 1, y, nrow, ncol, level + 1) or
               matching(grid, pattern, x + 1, y, nrow, ncol, level + 1) or
               matching(grid, pattern, x, y - 1, nrow, ncol, level + 1) or
               matching(grid, pattern, x, y + 1, nrow, ncol, level + 1))

        grid[x].replace(grid[x][y], temp)
        return res

    return False


def checkMatch(grid, pattern):
    """
    Check the pattern if exists in the grid or not.

    Parameters
    --------------------
    grid: list -> 2D list which contains characters
    patter: str -> word

    Returns
    --------------------
    boolean -> If the word exists retuens True else False
    """

    l = len(pattern)
    nrow, ncol = len(grid), len(grid[0])
    if (l > nrow * ncol):
        return False
    for i in range(nrow):
        for j in range(ncol):
            if (grid[i][j] == pattern[0]):
                if (matching(grid, pattern, i, j,
                             nrow, ncol, 0)):
                    return True
    return False
