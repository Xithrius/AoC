with open("./input.txt") as f:
    text = [list(x) for x in f.readlines()]


def main0():
    v_len = len(text)
    d = {
        'F': lambda y: y[:len(y) // 2],
        'B': lambda y: y[len(y) // 2:],
        'L': lambda x: x[:len(x) // 2],
        'R': lambda x: x[len(x) // 2:],
    }
    seats = []
    for instructions in text:
        rows, columns = list(range(128)), list(range(8))
        for instruction in instructions:
            if len(rows) == 1 and len(columns) == 1:
                break
            if instruction in ['F', 'B']:
                rows = d[instruction](rows)
            else:
                columns = d[instruction](columns)
        seats.append({'row': rows[0], 'column': columns[0], 'id': (rows[0] * 8) + columns[0]})
    m = max([x['id'] for x in seats])
    print(m)
    all_seats = []
    for row in range(128):
        for column in range(8):
            all_seats.append({'row': row, 'column': column, 'id': (row * 8) + column})
    all_seat_ids = [seat['id'] for seat in all_seats]
    missing = []
    current_seats = [seat['id'] for seat in seats]
    for seat_id in all_seat_ids:
        if seat_id not in current_seats:
            missing.append(seat_id)

    print(sorted(missing))


    

def main1():
    ...


print(main0())
# print(main1())
