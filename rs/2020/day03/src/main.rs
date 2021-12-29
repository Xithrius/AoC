fn main() {
    let input = std::fs::read_to_string("./input.txt")
        .unwrap()
        .split('\n')
        .map(|s| {
            s.to_string()
                .chars()
                .map(|c| c.to_string())
                .collect::<Vec<String>>()
        })
        .filter(|s| !s.is_empty())
        .collect::<Vec<Vec<String>>>();

    for item in input.iter() {
        println!("{:?}", item);
    }

    solution1(&input);
    solution2(&input);
}

fn solution1(lines: &[Vec<String>]) {
    let mut hits: u32 = 0;

    for (x, line) in lines.iter().enumerate() {
        if line[(3 * x) % line.len()] == "#" {
            hits += 1;
        }
    }

    println!("{:?}", hits);
}

fn solution2(lines: &[Vec<String>]) {
    let f = |x_m: usize, y_m: usize| -> u32 {
        let mut hits = 0;

        for (x, line) in lines.iter().enumerate().step_by(y_m) {
            // println!("{:?}, {:?}", x * x_m);

            if line[(x_m * x) % line.len()] == "#" {
                hits += 1;
            }
        }

        hits
    };

    println!("{:?}", f(1, 1) * f(3, 1) * f(5, 1) * f(7, 1) * f(1, 2));
}
