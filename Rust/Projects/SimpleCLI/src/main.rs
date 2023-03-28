use std::env;

fn main() {
    let args: Vec<String> = env::args().collect();

    if args.len() != 5 {
        print_help();
        return;
    }

    let mut input_dir = "";
    let mut output_dir = "";

    for i in 1..args.len() {
        match &args[i][..] {
            "-i" => {
                input_dir = &args[i + 1];
            }
            "-o" => {
                output_dir = &args[i + 1];
            }
            "--help" => {
                print_help();
                return;
            }
            _ => {}
        }
    }

    println!("Input directory: {}", input_dir);
    println!("Output directory: {}", output_dir);
}

fn print_help() {
    println!("Usage: my-program -i <input directory> -o <output directory>");
}
