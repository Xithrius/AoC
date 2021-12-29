use std::collections::HashMap;

use regex::{Captures, Regex};

fn main() {
    let re = Regex::new(r"^(\d+),(\d+) -> (\d+),(\d+)$").unwrap();

    let f = std::fs::read_to_string("./input.txt").unwrap();

    let input = f
        .split('\n')
        .flat_map(|s| re.captures(s))
        .collect::<Vec<Captures>>();

    solution1(&input);
    solution2(&input);
}

fn solution1(lines: &[Captures]) {
    let f_u32 =
        |c: &Captures, i: usize| -> u32 { c.get(i).unwrap().as_str().parse::<u32>().unwrap() };

    let mut v = vec![];

    for line in lines {
        let x0 = f_u32(&line, 1);
        let y0 = f_u32(&line, 2);
        let x1 = f_u32(&line, 3);
        let y1 = f_u32(&line, 4);

        if x0 == x1 || y0 == y1 {
            let x_iter = if x0 < x1 { x0..=x1 } else { x1..=x0 };

            for x in x_iter {
                let y_iter = if y0 < y1 { y0..=y1 } else { y1..=y0 };

                for y in y_iter {
                    v.push(vec![x, y]);
                }
            }
        }
    }

    let mut counts: HashMap<Vec<u32>, usize> = HashMap::new();

    for item in v {
        *counts.entry(item).or_insert(0) += 1;
    }

    println!("{:?}", counts.values().filter(|&&i| i >= 2).count());
}

fn solution2(lines: &[Captures]) {
    let f_u32 =
        |c: &Captures, i: usize| -> u32 { c.get(i).unwrap().as_str().parse::<u32>().unwrap() };

    let mut v = vec![];

    for line in lines {
        let x0 = f_u32(&line, 1);
        let y0 = f_u32(&line, 2);
        let x1 = f_u32(&line, 3);
        let y1 = f_u32(&line, 4);

        if x0 == x1 || y0 == y1 {
            let x_iter = if x0 < x1 { x0..=x1 } else { x1..=x0 };

            for x in x_iter {
                let y_iter = if y0 < y1 { y0..=y1 } else { y1..=y0 };

                for y in y_iter {
                    v.push(vec![x, y]);
                }
            }
        } else if (x1 > x0 && y1 > y0) || (x0 > x1 && y0 > y1) {
            let x_iter = if x0 < x1 { x0..=x1 } else { x1..=x0 };
            let y_iter = if y0 < y1 { y0..=y1 } else { y1..=y0 };

            v.extend(
                x_iter
                    .zip(y_iter)
                    .map(|(a, b)| vec![a, b])
                    .collect::<Vec<Vec<u32>>>(),
            );
        } else {
            let x_max = if x0 > x1 { x0 } else { x1 };
            let x_min = if x0 < x1 { x0 } else { x1 };

            let y_max = if y0 > y1 { y0 } else { y1 };
            let y_min = if y0 < y1 { y0 } else { y1 };

            v.extend(
                (x_min..=x_max)
                    .zip((y_min..=y_max).rev())
                    .map(|(a, b)| vec![a, b])
                    .collect::<Vec<Vec<u32>>>(),
            );
        }
    }

    let mut counts: HashMap<Vec<u32>, usize> = HashMap::new();

    for item in v {
        *counts.entry(item).or_insert(0) += 1;
    }

    println!("{:?}", counts.values().filter(|&&i| i >= 2).count());
}
