fn main() {
    let input = std::fs::read_to_string("./input.txt")
        .unwrap()
        .split("\n\n")
        .map(|s| s.to_string())
        .filter(|s| !s.is_empty())
        .collect::<Vec<String>>();

    let moves = input[0]
        .split(',')
        .map(|s| s.parse::<i32>().unwrap())
        .collect::<Vec<i32>>();

    let boards = input[1..]
        .iter()
        .map(|s| {
            s.split('\n')
                .collect::<Vec<&str>>()
                .iter()
                .map(|r| {
                    r.split(' ')
                        .filter_map(|s| s.parse::<i32>().ok())
                        .collect::<Vec<i32>>()
                })
                .collect::<Vec<Vec<i32>>>()
        })
        .collect::<Vec<Vec<Vec<i32>>>>();

    // solution1(moves, boards);
    solution2(moves, boards);
}

fn won_func(board: Vec<Vec<i32>>) -> bool {
    for i in 0..board.len() {
        if board[i].iter().sum::<i32>() == (board[i].len() as i32 * -1) {
            return true;
        } else if board.iter().map(|r| r[i]).sum::<i32>() == (board[i].len() as i32 * -1) {
            return true;
        }
    }

    false
}

fn solution1(global_moves: Vec<i32>, global_boards: Vec<Vec<Vec<i32>>>) {
    let moves = global_moves.clone();
    let mut boards = global_boards.clone();

    let mut winning_int: i32 = 0;
    let mut won = false;

    'outer: loop {
        for item in &moves {
            for board in 0..boards.len() {
                for row in 0..boards[board].len() {
                    for b_value in 0..boards[board][row].len() {
                        if item == &boards[board][row][b_value] {
                            let tmp = boards[board][row][b_value];

                            boards[board][row][b_value] = -1;

                            if won_func(boards[board].clone()) {
                                winning_int = tmp;
                                won = true;
                            }
                            // println!("{:?}", boards[board][row][b_value]);
                        }
                    }
                }

                if won {
                    let mut unmarked = 0;
                    for a in &boards[board] {
                        for b in a {
                            if -1 != *b {
                                unmarked += *b;
                            }
                        }
                    }

                    println!("{:?}", unmarked * winning_int);
                    break 'outer;
                }
            }
        }
    }
}

fn solution2(moves: Vec<i32>, global_boards: Vec<Vec<Vec<i32>>>) {
    let mut boards = global_boards.clone();

    let mut winning_int: i32 = 0;
    let mut won = false;
    let mut wons = vec![];

    'outer: loop {
        for item in &moves {
            for board in 0..boards.len() {
                if wons.contains(&boards[board]) {
                    continue;
                }

                for row in 0..boards[board].len() {
                    for b_value in 0..boards[board][row].len() {
                        if item == &boards[board][row][b_value] {
                            let tmp = boards[board][row][b_value];

                            boards[board][row][b_value] = -1;

                            if won_func(boards[board].clone()) {
                                if boards.len() - wons.len() == 1 {
                                    winning_int = tmp;
                                    won = true;
                                } else {
                                    wons.push(boards[board].clone());
                                }
                            }
                            // println!("{:?}", boards[board][row][b_value]);
                        }
                    }
                }

                if won {
                    let mut unmarked = 0;
                    for a in &boards[board] {
                        for b in a {
                            if -1 != *b {
                                unmarked += *b;
                            }
                        }
                    }

                    println!("{:?}", unmarked * winning_int);
                    break 'outer;
                }
            }
        }
    }
}
