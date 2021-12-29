use std::{cmp::Eq, collections::HashMap, hash::Hash};

fn main() {
    let f = std::fs::read_to_string("./input.txt").unwrap();
    let input = f
        .trim()
        .chars()
        .map(|c| c.to_string())
        .collect::<Vec<String>>();

    // println!("{:#?}", input);

    solution1(&input);
    solution2(&input);
}

#[derive(PartialEq, Hash, Eq, Clone)]
struct Coordinate {
    pub x: i32,
    pub y: i32,
}

fn solution1(lines: &[String]) {
    let mut coords: HashMap<Coordinate, usize> = HashMap::new();

    let mut current = Coordinate { x: 0, y: 0 };

    for line in lines {
        *coords.entry(current.to_owned()).or_insert(0) += 1;

        match line.as_str() {
            ">" => current.x += 1,
            "<" => current.x -= 1,
            "^" => current.y += 1,
            "v" => current.y -= 1,
            _ => {}
        }
    }

    let total = coords.values().filter(|&&i| i >= 1).count();

    println!("{:?}", total);
}

fn solution2(lines: &[String]) {
    let mut coords: HashMap<Coordinate, usize> = HashMap::new();

    let mut s = Coordinate { x: 0, y: 0 };
    let mut r = Coordinate { x: 0, y: 0 };

    for (i, line) in lines.iter().enumerate() {
        if i % 2 == 0 {
            match line.as_str() {
                ">" => s.x += 1,
                "<" => s.x -= 1,
                "^" => s.y += 1,
                "v" => s.y -= 1,
                _ => {}
            }
            *coords.entry(s.to_owned()).or_insert(0) += 1;
        } else {
            match line.as_str() {
                ">" => r.x += 1,
                "<" => r.x -= 1,
                "^" => r.y += 1,
                "v" => r.y -= 1,
                _ => {}
            }
            *coords.entry(r.to_owned()).or_insert(0) += 1;
        }
    }

    let total = coords.values().filter(|&&i| i >= 1).count();

    println!("{:?}", total);
}
