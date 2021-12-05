fn main() {
    // let mut previous = 0;
    let input = std::fs::read_to_string("./input.txt")
        .unwrap()
        .split('\n')
        .filter_map(|i| i.parse::<usize>().ok())
        .collect::<Vec<usize>>();

    println!(
        "{:?}",
        (0..input.len() - 1)
            .filter(|&i| input[i] < input[i + 1])
            .count()
    );

    println!(
        "{:?}",
        (0..input.len() - 3)
            .filter(|&i| input[i] < input[i + 3])
            .count()
    );
}
