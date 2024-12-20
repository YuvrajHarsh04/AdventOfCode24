def parse_input(input_data):
    grid = [list(line) for line in input_data.strip().splitlines()]
    start_pos = None
    start_dir = None
    directions = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}

    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell in directions:
                start_pos = (i, j)
                start_dir = cell
                grid[i][j] = '.'  # Replace the guard symbol with an open space
                break
        if start_pos:
            break

    return grid, start_pos, start_dir

def turn_right(direction):
    turn_order = ['^', '>', 'v', '<']
    idx = turn_order.index(direction)
    return turn_order[(idx + 1) % 4]

def simulate_guard(grid, start_pos, start_dir):
    directions = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}
    visited_states = set()
    pos = start_pos
    facing = start_dir

    rows, cols = len(grid), len(grid[0])

    while True:
        state = (pos, facing)
        if state in visited_states:
            return True  # Loop detected
        visited_states.add(state)

        dx, dy = directions[facing]
        next_pos = (pos[0] + dx, pos[1] + dy)

        if not (0 <= next_pos[0] < rows and 0 <= next_pos[1] < cols):
            return False  # Guard exits the grid

        if grid[next_pos[0]][next_pos[1]] == '#':
            facing = turn_right(facing)
        else:
            pos = next_pos

def find_obstruction_positions(grid, start_pos, start_dir):
    rows, cols = len(grid), len(grid[0])
    valid_positions = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '.' and (i, j) != start_pos:
                # Place obstruction temporarily
                grid[i][j] = '#'
                if simulate_guard(grid, start_pos, start_dir):
                    valid_positions += 1
                # Remove obstruction
                grid[i][j] = '.'

    return valid_positions

def main(input_data):
    grid, start_pos, start_dir = parse_input(input_data)
    result = find_obstruction_positions(grid, start_pos, start_dir)
    return result

# Example input data
data = """...........#....................#......#.....................#.#...........#......................................................
.....................................#....#.................#...............................#.....................................
..#..#.......#.............................................#.#.........................#......................#..............#....
.........................#.....#...............#.................#................................................................
.......#..........#........#.#............................................#....#.....................#..........##..#.............
.........#.....................................................#..............................................................#...
.....#..............................................................#................##.....#...........#.......#.........#.......
.......#.........#......#...............#............................#.........#.....#.....#...#..................................
.......#...............#...................#...............#............#.......................................................#.
........#.......................................................................##..#..............#...#..........................
..............#........#.......................#......#...............#..#......................#......#...#............#.........
................#................#...........................................#.....#................#..........#..................
..##....................#...........#......................#..................#.......#...........................................
..................................................................#..........#...................#................................
........................#.......#..........................#................................#.....................#...#.#.........
...............#........#...............#.##..#.#...............#...........#......................................#..............
.#.........#.#...............................................................................#..........................#...#.....
..............................#.....#.............##..............#.##....................#......#.................#....#.........
..............#.............................#........#.....#..........................................#...........#...............
...................#.................#..............#....##..#......................#..............................#....#.#.......
.............##.....................#..........#....................................#.....................#...#.#.................
.........................#..........#.......#.................................#...................................................
............#.................#.................................................#.........##....................#.........#.....#.
.#.........#.........................#..............#............#..#...........................##.........#......................
...........................#.....#...................#....#...........#.#.#...........#...................#.......................
.................#..#......#..............................................................................#...................#...
...............................#..............#...#..#......##.#.........................#........#...........#...................
........#...............##.............................................................#..........................#...............
.............#.............#.............#...................#...........#....................#...................................
##.......................................................................................#....#...........#....#...........#......
.....................#.#.......................................#.....................................#.................#..........
......................#...................................................................#.....................#............#...#
.........................#.#........................#.#................#....#....#.....#..........................................
.....................#...#.......................................#.......#.............#...................#......................
.............#...............#...............................................................................................#....
........................................................................................................#........#.........#......
.................................##....................#....#..............#.....#.....#..#....#.........................#.#.....#
.........................................................................#........#........#.........................#...#........
#...................#..........#......................#..............................#.#........................#.................
.#.....................................................................#..#.......#........................#......................
.......................#..............#..............#..#..............................#..........................................
...................................................................................................#...................#..........
...............#............#....................................#.....................#....................#.....................
............#..#.#..........#.#.......#..........................#.................#.#..........#.......#.........................
.......#....#.............................#..............................#..#........................#........#...................
........#.................#.....#.#..............................#........................#...................#..........#........
............................#........................#.........................................................#..................
....................................#.............##....................................................................#..#......
..................................................#................................................#..............#........#...##.
...........##.................#.........................#....................................................#...........#........
...........#.#..................#.......................#...#.......#................#.......##...................................
................................................#...........#........#.......................#.....................#....#.#.......
...............#........................................#............................#.....................................#......
........#...#.....#.......................................................#.#................................#.#..................
.....#............#.#...............#.#.....#....................#.#...................#...................##.........#..........#
............#.................#....................................................#...........................................#..
................#..#.....#....................................#................#...#..............................................
.....................................................................#...............#............................................
..................#...........#.....#...................#....#..............................................#.....................
.#............#...................................#.........#.........................................#...........#...............
#.......#..#...#.....#............................................................................................................
..#.........................................................##..............................#................................#....
..............................#..............#........................................................#....................#......
#.........#.........#.............#..............#............................#..........#........................#..#............
....#...........#..........................##......#.............................#.....#........................#.................
.....#.................................................................#..#.......................................................
..........................#.......#.......#..................#....................................................................
................#....................#..................#.........................................................................
..............................................#..........................#...........#.....#...........................#....#.#...
.##...............#...#...........................................................................................................
..................#..#.......................#...#..#.#.................................#.........................#...........#...
..........................................................................#....................................#..................
#...........#.............................##.....................#........#....#...#........#.....................#.....#.........
.......#.............................#...^....#..................................#.........#......................................
........#..............................#................................#.....#....##.............................................
.................#...........................#........................#..........#..........#.................#.#..........#.....#
..................................................................................................................#...............
..........#.........#........................#........................................................#........................#..
................................................................................................................#.................
....................#......................#....#.......#.....#...................................................................
................................#........................................................#.........................###............
......#..............#.#....................#............#.......................#.......................................#........
.........................#....................................#..............#.......#............................................
..............#.................#........................................................#..#.....................................
.....#.#........................#...........................................#..#.....#.................#................#......##.
................#.............#...................................................................................................
#....................#..........#..............##...#........#..#.........................#............#......#..................#
...........#..#.......#.....................#..........................................................#........#.................
...............................................#................#...........#................................#....................
.............#.......#.................#........#.............................................#...........#.......................
....................#.......#.....#.......................#.................#.............#.........................#.............
.#..............#.................................................................................................................
..#.#......................................#.................#.........#...................................#.#....................
......#..............................#........#.#..................#................#.................................#...........
..............#........................................#..........................................................................
.#...........#.........#...........#...................#................#..................................#............#..#......
.........#....#...................#..#.................................................................#....#.....................
..........#...........................#.....................................#...............#.......#...#.........................
...........#..................................#............................................................##................#....
.......................#..#.......................................................................................................
...............................................#......................#.#.#.............#..#........#...........................#.
..#.................................................#..............................#.....................................#........
..........#..#..........#...................#......................................##......#.......#........#.....#...............
.#.#...............................................##...#................#..............#.....#...................................
....................#..#...............................#..#.......#....................#....#.....................#.....#.#.......
#...................#...........#...................................................#...........................#..##.........###.
.............#.........#......#..........................#.................#......##................#...............#...#.........
........#.....................................................................................#...................................
..#...........#...................................#...................#............................#.........#.................#..
.................................................................................#................................................
.#........#.................#......................................#.....#...........#................#...........................
#...........................#..............................#....#............................................................#....
#..........#.............................................#..........#.......................................................#.....
.........#...#...#...#............................................................#....#..........#.......................#.......
.........................#.........................#........#............#..............#.....##.........................#...#....
...............................#...........#..............................................#......................#......#.........
......................#........................#..#.....................#...............................#........................#
......#...##..............................................................................................................#.......
............#.............#.#...............................................#.........#..........................#...........#....
.......................................#............#...............................................#.............................
....#........#.............................#...............#.#................................................#...................
.........#.#........................#.....#...##...#.........###............#.#.........#......#.........#................#.....#.
...........#....................#......................##...............#.......................................................#.
#......................................................#.................##....................................#........#.....#...
..#..........................##.................#...........................................#.....................................
.......................................#............#......#...#.........#......##......................................#.........
.#.......#.........................................##..............................................#.#...................#........
.................#.........#..........................##............................#..#.....#....................................
.....#....................................#......................................#.......................#...........#..#..#......
.......#......#.........#.....#........#......#.................#...........#............#..................#....#...........#...."""

result = main(data)
print(f"Number of valid obstruction positions: {result}")