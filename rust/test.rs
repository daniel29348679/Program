

fn main() {
    let mut s = String::from("hello");

    let r1 = &mut s;

    r1.push_str(" world");
    println!("{}", r1);
    println!("{}", s);

}