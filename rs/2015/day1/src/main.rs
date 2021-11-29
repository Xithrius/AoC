fn main() {
    let input = std::fs::read_to_string("./input.txt").unwrap();

    let trimmed = input.trim();

    let level = 0;

    for i in 0..=trimmed.len() {
        if trimmed[i] == "(" {
            level += 1;
        } else {
            level -= 1;
        }
    }
}
