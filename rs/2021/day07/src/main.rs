fn main() {
    let f = std::fs::read_to_string("./input.txt").unwrap();

    let input = f
        .split(',')
        .map(|s| s.to_string().trim().parse::<usize>().unwrap())
        .collect::<Vec<usize>>();

    solution1(&input);
    solution2(&input);
}

fn solution1(lines: &[usize]) {
    let mut v = Vec::new();

    for &i in lines.iter() {
        let mut total = 0;
        for &j in lines.iter() {
            if i != j {
                if i > j {
                    total += i - j;
                } else {
                    total += j - i;
                }
            }
        }
        v.push(total);
    }

    println!("{:?}", v.iter().min().unwrap());
}

fn solution2(lines: &Vec<usize>) {
    let mut v = Vec::new();
    let mut nums = lines.clone();

    // Please for the love of god rewrite this solution it's so unoptimized
    let min = *lines.iter().min().unwrap();
    let max = *lines.iter().max().unwrap();

    for num in min..max {
        if !nums.contains(&num) {
            nums.push(num);
        }
    }

    for &i in nums.iter() {
        let mut total = 0;
        for &j in lines.iter() {
            if i != j {
                if i > j {
                    total += (1..=i - j).collect::<Vec<usize>>().iter().sum::<usize>();
                } else {
                    total += (1..=j - i).collect::<Vec<usize>>().iter().sum::<usize>();
                }
            }
        }
        v.push(total);
    }

    println!("{:?}", v.iter().min().unwrap());
}
