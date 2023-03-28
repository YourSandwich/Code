use std::env;
use std::fs;
use std::path::PathBuf;

fn main() {
    let args: Vec<String> = env::args().collect();

    if args.len() != 3 {
        if args.contains(&String::from("--help")) {
            println!("Please specify <output_dir> and <summary_dir>");
        } else {
            println!("Invalid number of arguments. Please specify <output_dir> and <summary_dir>");
        }
        return;
    }

    let query = &args[1];
    let file_path = &args[2];

    println!("Summarizing CSVs in {}", query);
    println!("Output directory: {}", file_path);
    summarize(query, file_path);
}

fn summarize(query: &str, file_path: &str) {
    let path = query;
    let _output = file_path;

    // Open the directory at the specified path
    let dir_entries = fs::read_dir(path).unwrap();

    // Iterate over the directory entries
    for entry in dir_entries {
        let entry = entry.unwrap();
        let file_path = entry.path();

        // Print the entry path
        println!("{}", PathBuf::from(file_path).display());
    }
}
