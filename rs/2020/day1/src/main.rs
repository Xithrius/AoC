fn main() {
    let args = std::fs::read_to_string("./input.txt")
        .unwrap()
        .split('\n')
        .filter_map(|s| s.parse::<usize>().ok())
        .collect::<Vec<usize>>();

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
