use regex::{Captures, Regex};

fn main() {
    let re = Regex::new(r"^(\d+)-(\d+) ([a-z]): ([a-z]*)$").unwrap();

    let f = std::fs::read_to_string("./input.txt").unwrap();

    let input = f
        .split('\n')
        .flat_map(|s| re.captures(s))
        .collect::<Vec<Captures>>();

    solution1(&input);
    solution2(&input);
}

fn f_usize(c: &Captures, i: usize) -> usize {
    c.get(i).unwrap().as_str().parse::<usize>().unwrap()
}

fn solution1(lines: &[Captures]) {
    let mut total = 0;

    for line in lines {
        let min = f_usize(&line, 1);
        let max = f_usize(&line, 2);

        let char = line.get(3).unwrap().as_str();

        let occur = line
            .get(4)
            .unwrap()
            .as_str()
            .chars()
            .filter(|c| c.to_string() == char)
            .count();

        if occur >= min && occur <= max {
            total += 1;
        }
    }

    println!("{:?}", total);
}

fn solution2(lines: &[Captures]) {
    let mut total = 0;

    for line in lines {
        let i0 = f_usize(&line, 1) - 1;
        let i1 = f_usize(&line, 2) - 1;

        let char = line.get(3).unwrap().as_str();

        let chars = line
            .get(4)
            .unwrap()
            .as_str()
            .chars()
            .map(|c| c.to_string())
            .collect::<Vec<String>>();

        if (chars[i0] == char && chars[i1] != char) || (chars[i0] != char && chars[i1] == char) {
            total += 1;
        }
    }

    println!("{:?}", total);
}
