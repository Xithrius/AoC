use std::collections::HashMap;

fn main() {
    let f = std::fs::read_to_string("./input.txt").unwrap();

    let input = f
        .split('\n')
        .map(|s| {
            s.to_string()
                .chars()
                .map(|c| c.to_string().parse::<usize>().unwrap())
                .collect::<Vec<usize>>()
        })
        .filter(|v| !v.is_empty())
        .collect::<Vec<Vec<usize>>>();

    // for item in input.iter() {
    //     println!("{:?}", item);
    // }

    solution1(&input);
    solution2(&input);
}

#[derive(PartialEq, std::cmp::Eq, std::hash::Hash, Debug)]
struct Coordinate {
    pub x: i32,
    pub y: i32,
}

fn solution1(lines: &[Vec<usize>]) {
    let mut map: HashMap<Coordinate, usize> = HashMap::new();

    let mut lows = Vec::new();

    for (i, line) in lines.iter().enumerate() {
        for j in 0..line.len() {
            map.insert(
                Coordinate {
                    x: j as i32,
                    y: i as i32,
                },
                lines[i][j],
            );
        }
    }

    for (k, v) in &map {
        let mut adj = Vec::new();

        let kx = k.x as i32;
        let ky = k.y as i32;

        let coordinates = vec![
            Coordinate { x: kx + 1, y: ky },
            Coordinate { x: kx - 1, y: ky },
            Coordinate { x: kx, y: ky + 1 },
            Coordinate { x: kx, y: ky - 1 },
        ];

        for coord in coordinates {
            if let Some(b) = map.get(&coord) {
                adj.push(b);
            }
        }

        if adj.iter().filter(|&&a| a <= v).count() == 0 {
            lows.push(v + 1);
        }
    }

    println!("{:#?}", lows.iter().sum::<usize>());
}

fn solution2(lines: &[Vec<usize>]) {
    let mut map: HashMap<Coordinate, usize> = HashMap::new();
}
