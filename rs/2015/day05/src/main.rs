fn main() {
    let f = std::fs::read_to_string("./input.txt").unwrap();

    let input = f
        .split('\n')
        .map(|s| s.to_string())
        .filter(|s| !s.is_empty())
        .collect::<Vec<String>>();

    // println!("{:#?}", input);

    solution1(&input);
    // solution2(&input);
}

fn solution1(lines: &[String]) {
    let mut total = 0;

    let vowels = vec!["a", "e", "i", "o", "u"];
    let illegal = vec!["ab", "cd", "pq", "xy"];

    for line in lines {
        if (vowels.iter().filter(|&&v| line.contains(v)).count() < 3)
            || (illegal.iter().filter(|&&v| line.contains(v)).count() > 0)
        {
            continue;
        }

        let chars = line.chars().map(|c| c.to_string()).collect::<Vec<String>>();

        let mut repeat = 0;
        for i in 0..chars.len() - 1 {
            if chars[i] == chars[i + 1] {
                repeat = 1;
                break;
            }
        }

        if repeat == 0 {
            break;
        }

        total += 1;
    }

    println!("{:?}", total);
}

fn solution2(lines: &[String]) {}
