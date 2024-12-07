def count_word(grid, word):
    rows = len(grid)
    cols = len(grid[0])
    word_len = len(word)
    count = 0

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]

    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols

    # def search(x, y, dx, dy):
    #     for i in range(word_len):
    #         nx, ny = x + i * dx, y + i * dy
    #         if not is_valid(nx, ny) or grid[nx][ny] != word[i]:
    #             return 0
    #     return 1

    for x in range(1, rows - 1):
        for y in range(1, cols - 1):
            if (
                is_valid(x - 1, y - 1)
                and grid[x - 1][y - 1] == "M"
                and is_valid(x, y)
                and grid[x][y] == "A"
                and is_valid(x + 1, y + 1)
                and grid[x + 1][y + 1] == "S"
                and is_valid(x - 1, y + 1)
                and grid[x + 1][y + 1] == "M"
                and is_valid(x, y)
                and grid[x][y] == "A"
                and is_valid(x + 1, y - 1)
                and grid[x + 1][y - 1] == "S"
            ):
                count += 1

    return count


input_string = """
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
""".strip()


grid = [list(row) for row in input_string.split("\n")]

word = "X-MAS"

occurrences = count_word(grid, word)
print(occurrences)
