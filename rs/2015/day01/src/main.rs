fn main() {
    let f = std::fs::read_to_string("./input.txt").unwrap();

    let input = f
        .trim()
        .chars()
        .map(|c| c.to_string())
        .collect::<Vec<String>>();

    // println!("{:#?}", input);

    solution1(&input);
    solution2(&input);
}

fn solution1(lines: &[String]) {
    let total: i32 = lines
        .iter()
        .map(|l| if l == "(" { 1 } else { -1 })
        .collect::<Vec<i32>>()
        .iter()
        .sum();

    println!("{:?}", total);
}

fn solution2(lines: &[String]) {
    let mut total = 0;

    for (i, line) in lines.iter().enumerate() {
        if total < 0 {
            println!("{:?}", i);
            return;
        }

        if line == "(" {
            total += 1;
        } else {
            total -= 1;
        }
    }
}
