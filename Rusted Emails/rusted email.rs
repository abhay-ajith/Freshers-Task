extern crate regrex;
use regerx::Regex;
use std::io;
fn main(){
  println!("Enter the email");
  let mut txt = String::new();
  io::stdin()
        .read_line(&mut txt)
        .expect("WAs unable to read the line");
  assert!(Regrex::new(r"\w[a-zA-Z0-9._+-]+@[a-zA-Z0-9._]+\.[a-zA-Z]").unwrap().is_match(&txt));
}