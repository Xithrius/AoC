fn main() {
    let input = std::fs::read_to_string("./input.txt")
        .unwrap()
        .split('\n')
        .filter_map(|s| s.parse::<usize>().ok())
        .collect::<Vec<usize>>();

    sol1(&input);
    sol2(&input);
}

fn sol1(lines: &[usize]) {
    for i in 0..lines.len() {
        for j in 0..lines.len() {
            if i == j {
                continue;
            } else if lines[i] + lines[j] == 2020 {
                println!("{}", lines[i] * lines[j]);
                return;
            }
        }
    }
}

fn sol2(lines: &[usize]) {
    for i in 0..lines.len() {
        for j in 0..lines.len() {
            for k in 0..lines.len() {
                if i == j || i == k || j == k {
                    continue;
                } else if lines[i] + lines[j] + lines[k] == 2020 {
                    println!("{}", lines[i] * lines[j] * lines[k]);
                    return;
                }
            }
        }
    }
}
