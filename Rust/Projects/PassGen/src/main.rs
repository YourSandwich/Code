use rand::{Rng, thread_rng};
use std::env;

fn generate_password(length: usize, lowercase: bool, uppercase: bool, special: bool, numeric: bool) -> String {
    let mut password = String::new();
    let mut rng = thread_rng();
    let mut chars = Vec::new();
    let lowercase_chars = "abcdefghijklmnopqrstuvwxyz";
    let uppercase_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    let special_chars = "!@#$%^&*()-_=+[{]}\\|;:'\",<.>/?";
    let numeric_chars = "0123456789";
    if lowercase {
        chars.extend(lowercase_chars.chars());
    }
    if uppercase {
        chars.extend(uppercase_chars.chars());
    }
    if special {
        chars.extend(special_chars.chars());
    }
    if numeric {
        chars.extend(numeric_chars.chars());
    }
    for _ in 0..length {
        let idx = rng.gen_range(0..chars.len());
        password.push(chars[idx]);
    }
    password
}

fn print_help() {
    println!("Usage: passgen [OPTIONS] [LENGTH]\n");
    println!("Generate a random password.\n");
    println!("Options:");
    println!("  -l,           Include lowercase letters");
    println!("  -u,           Include uppercase letters");
    println!("  -s,           Include special characters");
    println!("  -n,           Include numbers");
    println!("  -h,           Display this help and exit");
}

fn main() {
    let args: Vec<String> = env::args().collect();
    let mut length = 12;
    let mut lowercase = false;
    let mut uppercase = false;
    let mut special = false;
    let mut numeric = false;
    if args.len() == 1 {
        length = 12;
        lowercase = true;
        uppercase = true;
        special = true;
        numeric = true;
    } else if args.len() == 2 {
        length = args[1].parse().unwrap_or(12);
        lowercase = true;
        uppercase = true;
        special = true;
        numeric = true;
    } 
    else {
        for arg in &args[1..] {
            if arg.starts_with('-') {
                for c in arg.chars().skip(1) {
                    match c {
                        'l' => lowercase = true,
                        'u' => uppercase = true,
                        's' => special = true,
                        'n' => numeric = true,
                        'h' => {
                            print_help();
                            return;
                        },
                        _ => {
                            println!("Error: Invalid option: {}", c);
                            return;
                        }
                    }
                }
            } else {
                length = arg.parse().unwrap_or(12);
            }
        }
    }
    let password = generate_password(length, lowercase, uppercase, special, numeric);
    println!("{}", password);
}
