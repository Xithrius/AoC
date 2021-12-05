fn main() {
    let args = std::fs::read_to_string("./input.txt")
        .unwrap()
        .split('\n')
        .filter_map(|s| s.parse::<usize>().ok())
        .collect::<Vec<usize>>();

    sol1(&args);
    sol2(&args);
}

fn sol1(args: &[usize]) {
    for i in 0..args.len() {
        for j in 0..args.len() {
            if i == j {
                continue;
            } else if args[i] + args[j] == 2020 {
                println!("{}", args[i] * args[j]);
                return;
            }
        }
    }
}

fn sol2(args: &[usize]) {
    for i in 0..args.len() {
        for j in 0..args.len() {
            for k in 0..args.len() {
                if i == j || i == k || j == k {
                    continue;
                } else if args[i] + args[j] + args[k] == 2020 {
                    println!("{}", args[i] * args[j] * args[k]);
                    return;
                }
            }
        }
    }
}
