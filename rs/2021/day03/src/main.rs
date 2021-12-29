fn main() {
    let input = std::fs::read_to_string("./input.txt")
        .unwrap()
        .split('\n')
        .map(|s| s.to_string())
        .filter(|s| !s.is_empty())
        .map(|s| {
            s.chars()
                .map(|c| c.to_string().parse::<u32>().unwrap())
                .collect::<Vec<u32>>()
        })
        .collect::<Vec<Vec<u32>>>();

    // println!("{:#?}\n\n", input);

    solution1(&input);
    solution2(&input);
}

fn bit_to_decimal(v: &[u32]) -> u32 {
    v.iter()
        .enumerate()
        .map(|(i, a)| u32::pow(2, (v.len() - i - 1) as u32) * a)
        .collect::<Vec<u32>>()
        .iter()
        .sum::<u32>()
}

fn solution1(lines: &[Vec<u32>]) {
    let h = lines[0].len();

    let higher = (0..h)
        .map(|i| {
            if lines.iter().map(|r| r[i]).sum::<u32>() >= (lines.len() / 2) as u32 {
                1
            } else {
                0
            }
        })
        .collect::<Vec<u32>>();

    let lower = higher
        .iter()
        .map(|i| if *i == 1 { 0 } else { 1 })
        .collect::<Vec<u32>>();

    println!("{:?}", bit_to_decimal(&higher) * bit_to_decimal(&lower));
}

fn solution2(lines: &Vec<Vec<u32>>) {
    let h = lines[0].len();

    let mut higher = lines.clone();
    let mut lesser = lines.clone();

    for i in 0..h {
        if higher.len() > 1 {
            higher = higher
                .iter()
                .filter(|r| {
                    r[i] == if higher.iter().map(|r| r[i]).sum::<u32>()
                        >= ((higher.len() as f32) / 2.0).ceil() as u32
                    {
                        1
                    } else {
                        0
                    }
                })
                .map(|r| r.to_owned())
                .collect::<Vec<Vec<u32>>>();
        }

        if lesser.len() > 1 {
            lesser = lesser
                .iter()
                .filter(|r| {
                    r[i] == if lesser.iter().map(|r| r[i]).sum::<u32>()
                        >= ((lesser.len() as f32) / 2.0).ceil() as u32
                    {
                        0
                    } else {
                        1
                    }
                })
                .map(|r| r.to_owned())
                .collect::<Vec<Vec<u32>>>();
        }

        if higher.len() == 1 && lesser.len() == 1 {
            break;
        }
    }

    println!(
        "{:?}",
        bit_to_decimal(&higher[0]) * bit_to_decimal(&lesser[0])
    );
}
