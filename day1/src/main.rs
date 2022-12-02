use std::env;
use std::fs;
use std::io::{self, prelude::*, BufReader};

fn main() -> io::Result<()> {
    let args: Vec<String> = env::args().collect();
    let file_path = &args[1];

    let file = fs::File::open(file_path).expect("Unable to open file");
    let reader = BufReader::new(file);
    let mut max_calories = 0;
    let mut calc_calories = 0;
    let mut total_calories_per_elf_vec: Vec<i32> = Vec::new();
    for line in reader.lines() {
        if let Ok(l) = line {
            if l.is_empty() {
                total_calories_per_elf_vec.push(calc_calories);
                //reset
                if calc_calories > max_calories {
                    max_calories = calc_calories;
                }
                calc_calories = 0;
                continue;
            }
            else {
                calc_calories += l.parse::<i32>().unwrap();
            }
        }
    }
    println!("Max calories: {}", max_calories);

    total_calories_per_elf_vec.sort_unstable();
    total_calories_per_elf_vec.reverse();
    let top_three = &total_calories_per_elf_vec[0..3];
    let sum: i32 = top_three.iter().sum::<i32>();
    println!("top 3 elves individual totals: {:?}", &top_three[0..3]);
    println!("Top 3 elf calorie total: {}", sum);
    Ok(())
}