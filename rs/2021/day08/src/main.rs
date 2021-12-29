use std::collections::HashMap;

fn main() {
    let input = std::fs::read_to_string("./input.txt")
        .unwrap()
        .split('\n')
        .map(|s| {
            s.to_string()
                .split(" | ")
                .map(|c| c.trim().to_string())
                .collect::<Vec<String>>()
        })
        .filter(|s| s.len() == 2)
        .collect::<Vec<Vec<String>>>();

    // for item in &input {
    //     println!("{:?}", item);
    // }

    solution1(&input);
    solution2(&input);
}

fn solution1(lines: &[Vec<String>]) {
    let mut total = 0;
    for line in lines {
        let items = line[1]
            .split(' ')
            .map(|s| s.to_string())
            .collect::<Vec<String>>();
        for item in items {
            if vec![2, 4, 3, 7].contains(&item.len()) {
                total += 1;
            }
        }
    }

    println!("{:?}", total);
}

fn solution2(lines: &[Vec<String>]) {
    let mut total = 0;

    let alph = vec!["a", "b", "c", "d", "e", "f", "g"]
        .iter()
        .map(|s| s.to_string())
        .collect::<Vec<String>>();

    for line in lines {
        let c = line[0]
            .split(' ')
            .map(|s| s.to_string())
            .collect::<Vec<String>>();
        let d = line[1]
            .split(' ')
            .map(|s| s.to_string())
            .collect::<Vec<String>>();

        // println!("{:?} - {:?}", c, d);

        let mut map: HashMap<Vec<String>, usize> = HashMap::new();
        for item in c {
            let mut i = item.chars().map(|c| c.to_string()).collect::<Vec<String>>();
            i.sort();
            match i.len() {
                2 => map.insert(i, 1),
                3 => map.insert(i, 7),
                4 => map.insert(i, 4),
                5 => {
                    // 2, 3, 5,
                    let missing = alph
                        .iter()
                        .filter(|&c| !i.contains(c))
                        .map(|c| c.to_string())
                        .collect::<Vec<String>>();

                    let pos0 = alph.iter().position(|x| x == &missing[0]).unwrap();
                    let pos1 = alph.iter().position(|x| x == &missing[1]).unwrap();

                    let distance = if pos0 > pos1 {
                        pos0 - pos1
                    } else {
                        pos1 - pos0
                    };

                    let cloned_item = i.clone();

                    match distance {
                        3 => map.insert(cloned_item, 2),
                        1 => map.insert(cloned_item, 3),
                        _ => map.insert(cloned_item, 5),
                    }

                    // println!("{:?}: {:?} -> {:?}", item, s, map.get(&item).unwrap());
                }
                6 => {
                    // 0, 6, 9
                    let missing = alph
                        .iter()
                        .filter(|&c| !i.contains(c))
                        .map(|c| c.to_string())
                        .collect::<Vec<String>>();

                    let pos = alph.iter().position(|x| x == &missing[0]).unwrap();

                    let cloned_item = i.clone();

                    match pos {
                        0 => map.insert(cloned_item, 9),
                        1 | 2 | 3 => map.insert(cloned_item, 6),
                        _ => map.insert(cloned_item, 0),
                    }
                }
                _ => map.insert(i, 8),
            };
        }

        let x = d
            .iter()
            .map(|y| {
                let mut i = y.chars().map(|s| s.to_string()).collect::<Vec<String>>();
                i.sort();
                map.get(&i).unwrap().to_string()
            })
            .collect::<Vec<String>>()
            .join("")
            .parse::<usize>()
            .unwrap();
        total += x;

        println!("{:?}\n{:?}\n{:?}\n", d, map, x);
    }

    println!("{:?}", total);
}
