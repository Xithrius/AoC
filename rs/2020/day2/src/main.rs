fn main() {
    let input = std::fs::read_to_string("./input.txt")
        .unwrap()
        .split('\n')
        .map(|s| s.to_string())
        .filter(|s| !s.is_empty())
        .collect::<Vec<String>>();

    // println!("{:?}", input);

    solution1(&input);
    solution2(&input);
}

fn solution1(lines: &[String]) {
    let mut correct = 0;

    let pattern = regex::Regex::new(r"^(\d+)-(\d+) ([a-z]): ([a-z]*)$").unwrap();

    let stuff = pattern.captures("asdfasdf");

    for line in lines {
        if let Some(capture) = pattern.captures(line) {
            let char = capture.get(3).unwrap().as_str();
            let chars = capture.get(4).unwrap().as_str();

            let lower = capture.get(1).unwrap().as_str().parse::<usize>().unwrap();
            let higher = capture.get(2).unwrap().as_str().parse::<usize>().unwrap();

            let count = chars.chars().filter(|s| s.to_string() == char).count();

            if count >= lower && count <= higher {
                correct += 1;
            }
        } else {
            println!("{:?}", line);
        }
    }

    println!("{:?}", correct);
}

fn solution2(lines: &[String]) {
    let mut correct = 0;

    let pattern = regex::Regex::new(r"^(\d+)-(\d+) ([a-z]): ([a-z]*)$").unwrap();

    for line in lines {
        let capture = pattern.captures(line).unwrap();

        let i0 = capture.get(1).unwrap().as_str().parse::<usize>().unwrap() - 1;
        let i1 = capture.get(2).unwrap().as_str().parse::<usize>().unwrap() - 1;

        let char = capture.get(3).unwrap().as_str();

        let chars = line.chars().map(|s| s.to_string()).collect::<Vec<String>>();

        if (chars[i0] == char && chars[i1] != char) || (chars[i0] != char && chars[i1] == char) {
            correct += 1;
        }
    }

    println!("{:?}", correct);
}
