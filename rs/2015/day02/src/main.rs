const PATTERN: &str = r"^(\d+)x(\d+)x(\d+)$";

fn main() {
    let re = regex::Regex::new(PATTERN).unwrap();

    let f = std::fs::read_to_string("./input.txt").unwrap();

    let input = f
        .split('\n')
        .flat_map(|s| re.captures(s))
        .collect::<Vec<regex::Captures>>();

    solution1(&input);
    // solution2(&input);
}

fn f_usize(c: &regex::Captures, i: usize) -> usize {
    c.get(i).unwrap().as_str().parse::<usize>().unwrap()
}

fn solution1(lines: &[regex::Captures]) {
    let mut total = 0;

    for line in lines {
        let l = f_usize(&line, 1);
        let w = f_usize(&line, 2);
        let h = f_usize(&line, 3);

        let lw = l * w;
        let wh = w * h;
        let hl = h * l;

        total += (2 * lw) + (2 * wh) + (2 * hl) + (vec![lw, wh, hl].iter().min().unwrap());
    }

    println!("{:?}", total);
}

// fn solution2(lines: &[regex::Captures]) {}
