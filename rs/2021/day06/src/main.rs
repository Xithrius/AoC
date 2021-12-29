use std::collections::HashMap;

fn main() {
    let input = std::fs::read_to_string("./input.txt")
        .unwrap()
        .trim()
        .split(',')
        .map(|s| s.to_string().parse::<u32>().unwrap())
        .collect::<Vec<u32>>();

    solution1(&input);
    solution2(&input);
}

fn solution1(lines: &Vec<u32>) {
    let mut fishes = lines.clone();

    let days = 80;

    for _ in 0..days {
        let mut spawn_offset = 0;

        for fish in 0..(fishes.len() - spawn_offset) {
            if fishes[fish] == 0 {
                fishes.push(8);
                fishes[fish] = 7;
                spawn_offset += 1;
            }

            fishes[fish] -= 1;
        }
    }

    println!("{:?}", fishes.len());
}

fn solution2(lines: &[u32]) {
    let mut fishes = lines.clone();

    let days = 256;

    let mut fish_count: [u64; 9] = [0; 9];

    for &lifetime in fishes {
        fish_count[lifetime as usize] += 1;
    }

    for day in 0..days {
        let tmp = fish_count[0];

        for i in 0..=7 {
            fish_count[i] = fish_count[i + 1];
        }

        fish_count[6] += tmp;
        fish_count[8] = tmp;
    }

    println!("{:?}", fish_count.iter().sum::<u64>());
}
