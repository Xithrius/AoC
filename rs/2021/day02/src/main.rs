fn main() {
    let input = std::fs::read_to_string("./input.txt")
        .unwrap()
        .split('\n')
        .map(|s| s.split(' ').map(|s| s.to_string()).collect::<Vec<String>>())
        .collect::<Vec<Vec<String>>>();

    solution1(&input);
    solution2(&input);
}

fn solution1(lines: &[Vec<String>]) {
    let mut v = 0;
    let mut h = 0;

    for line in lines {
        if line.len() == 1 {
            continue;
        }

        let num = line[1].parse::<usize>().unwrap();

        match line[0].as_str() {
            "forward" => h += num,
            "up" => v -= num,
            "down" => v += num,
            _ => {}
        }
    }

    println!("{:?}", v * h);
}

fn solution2(lines: &[Vec<String>]) {
    let mut v = 0;
    let mut h = 0;
    let mut a = 0;

    for line in lines {
        if line.len() == 1 {
            continue;
        }

        let num = line[1].parse::<usize>().unwrap();

        match line[0].as_str() {
            "forward" => {
                h += num;
                v += a * num;
            }
            "up" => {
                a -= num;
            }
            "down" => {
                a += num;
            }
            _ => {}
        }
    }

    println!("{:?}", h * v)
}
