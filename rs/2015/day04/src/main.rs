use hex_literal::hex;
use md5::{Digest, Md5};

fn main() {
    let f = std::fs::read_to_string("./input.txt").unwrap();

    let input = f.trim().to_string();

    println!("{:?}", input);

    solution1(&input);
    // solution2(&input);
}

fn solution1(line: &String) {
    let mut index = 1;

    loop {
        let mut hasher = Md5::new();

        let test = format!("{}{}", line, index);

        println!("{:?}", test);

        hasher.update(test.as_bytes());

        let result = hasher.finalize();

        println!("{:?}", result);

        index += 1;

        // if hasher.finalize()[..5] ==  {
        //     index += 1;
        // } else {
        //     break;
        // }
    }

    println!("{:?}", index);
}

fn solution2(line: &String) {}
