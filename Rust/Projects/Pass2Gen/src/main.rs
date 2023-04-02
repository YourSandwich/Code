use clap::{App, Arg};
use rand::{thread_rng, Rng};

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
    if chars.is_empty() {
        // If no character types are specified, default to using all character types
        chars.extend(lowercase_chars.chars());
        chars.extend(uppercase_chars.chars());
        chars.extend(special_chars.chars());
        chars.extend(numeric_chars.chars());
    }
    for _ in 0..length {
        let idx = rng.gen_range(0..chars.len());
        password.push(chars[idx]);
    }
    password
}

fn main() {
    let matches = App::new("pass2gen")
        .about("Generate a random password")
        .arg(Arg::with_name("length").help("Sets the length of the password").default_value("12").index(1))
        .arg(Arg::with_name("lowercase").short("l").help("Include lowercase letters"))
        .arg(Arg::with_name("uppercase").short("u").help("Include uppercase letters"))
        .arg(Arg::with_name("special").short("s").help("Include special characters"))
        .arg(Arg::with_name("numeric").short("n").help("Include numbers"))
        .setting(clap::AppSettings::DisableVersion)
        .get_matches();

    let length = matches.value_of("length").unwrap().parse::<usize>().unwrap();
    let lowercase = matches.is_present("lowercase");
    let uppercase = matches.is_present("uppercase");
    let special = matches.is_present("special");
    let numeric = matches.is_present("numeric");

    let password = generate_password(length, lowercase, uppercase, special, numeric);
    println!("{}", password);
}
