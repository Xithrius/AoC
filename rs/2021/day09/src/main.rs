fn main() {
    let f = std::fs::read_to_string("./input.txt").unwrap();
    let input = f
        .split('\n')
        .map(|s| {
            s.to_string()
                .chars()
                .map(|c| c.to_string().parse::<usize>().unwrap())
                .collect::<Vec<usize>>()
        })
        .filter(|x| !x.is_empty())
        .collect::<Vec<Vec<usize>>>();

    for item in input.iter() {
        println!("{:?}", item);
    }

    solution1(&input);
    solution2(&input);
}

fn solution1(lines: &[Vec<usize>]) {
    let h = lines[0].len();
    for i in 0..lines.len() {
        for j in 0..h {}
    }
}

fn solution2(lines: &[Vec<usize>]) {}
