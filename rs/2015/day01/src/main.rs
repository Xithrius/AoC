fn main() {
    let file_input = include_str!("../input.txt");

    let input = file_input
        .trim()
        .chars()
        .map(|s| s.to_string())
        .collect::<Vec<String>>();

    solution1(&input);
    solution2(&input);
}

fn solution1(a: &[String]) {
    println!(
        "{}",
        a.iter().map(|l| if l == "(" { 1 } else { -1 }).sum::<i32>()
    );
}

fn solution2(a: &[String]) {
    println!(
        "{:?}",
        a.iter()
            .map(|c| if c == "(" { 1 } else { -1 })
            .enumerate()
            .fold((0, 0), |(l, f), (i, c)| (
                c + l,
                if f == 0 && (c + l) < 0 { i } else { f }
            ))
    );

    // let mut total = 0;

    // for (i, line) in lines.iter().enumerate() {
    //     if total < 0 {
    //         println!("{:?}", i);
    //         return;
    //     }

    //     if line == "(" {
    //         total += 1;
    //     } else {
    //         total -= 1;
    //     }
    // }
}
