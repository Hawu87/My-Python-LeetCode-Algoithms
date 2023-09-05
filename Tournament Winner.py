def tournamentWinner(competitions, results):
    map, i = {}, 0
    max_val, max_str = -1, ""

    while i < len(results):
        curr = competitions[i][0] if results[i] == 1 else competitions[i][1]
        map[curr] = 3 + map.get(curr, 0)
        max_str = curr if map[curr] > max_val else max_str
        max_val = map[max_str]
        i += 1
    return max_str
