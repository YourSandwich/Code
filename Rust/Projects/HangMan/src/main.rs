extern crate rand;
use rand::Rng;

use std::fs::File;
use std::process::Command;
use std::io;
use std::io::prelude::*;

const MAX_ATTEMPS: u8 = 12;

// Describes that the Letter is a Character and has an attribute "revealded" that can be either
// true or false
struct Letter {
    character: char,
    revealed: bool
}

enum GameProgress {
    InProgress,
    Won,
    Lost
}

fn main() {
    let mut turns_left = MAX_ATTEMPS;
    let select_word = select_word();

    // Print selected word
    let mut letters = create_letters(&select_word);
    
    loop {
        Command::new("clear").status().unwrap();

        println!("Welcome to RustMan!");
        println!("\nYou have {} tries left.", turns_left);
        run_game(&letters);

        println!("Enter any letter to guess:");
        let user_inp = read_user_input_character();

        // Exit game if input "*" or input fails
        if user_inp == '*' {
            break;
        }
       
        // check if user guest a letter
        let mut one_revealed = false;
        for letter in letters.iter_mut() {
            if letter.character == user_inp {
                letter.revealed = true;
                one_revealed = true;
            }
        }
        if !one_revealed {
            turns_left -= 1;
        }

        match check_progress(turns_left, &letters) {
            GameProgress::InProgress => continue,
            GameProgress::Won => {
                println!("\nCongrats, you won!");
                break;
            }
            GameProgress::Lost => {
                println!("\nYou Lost!");
                break;
            }
        }
    }
    println!("The selected word was: {}", select_word);
}

fn select_word() -> String {
    // Open File
    let mut file = File::open("words.txt").expect("Could not open file!");

    // Load Word into Variabel
    let mut file_contents = String::new();
    file.read_to_string(&mut file_contents).expect("An error has occured while reading the file!");

    let dict: Vec<&str> = file_contents.trim().split(',').collect();

    // Index random word from dict
    let random_index = rand::thread_rng().gen_range(0..dict.len());

    return String::from(dict[random_index]);
}

// Creates a Vector and pushes seperate Letters of the word into it. 
fn create_letters(word: &String) -> Vec<Letter> {
    let mut letters: Vec<Letter> = Vec::new();

    for l in word.chars() {
        letters.push(Letter {
        character: l,
        revealed: false
        });
    }

    return letters;
}

// Creates the playfield _ _ _ _ <- Hidden letters from the dict word
fn run_game(letters: &Vec<Letter>) {
    let mut run_word = String::from("\nProgress:"); // Progress: A _ _ M _ I _ C

    for letter in letters {
        run_word.push(' ');
    
        if letter.revealed {
            run_word.push(letter.character);
        } else {
        run_word.push('_');
        }
    }
    println!("{}", run_word)
}

fn read_user_input_character() -> char {
    let mut user_inp = String::new();

    // get user input
    match io::stdin().read_line(&mut user_inp){
        Ok(_) => {
            match user_inp.chars().next() {
                Some(s) => { return s;}
                None => {return '*';}
            }
        }
        Err(_) => { return '*'; }
    }
}

fn check_progress(turns_left: u8, letters: &Vec<Letter>) -> GameProgress {
    let mut all_revealed = true;
    for letter in letters {
        if !letter.revealed {
            all_revealed = false;
        }
    }
    
    if all_revealed {
        return GameProgress::Won;
    }

    if turns_left > 0 {
        return GameProgress::InProgress
    } 
    return GameProgress::Lost;
}
