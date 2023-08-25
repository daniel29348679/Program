#![allow(warnings)]
use std::cmp::{max, min};
use std::io::{stdin, stdout, BufWriter, Write};

#[derive(Default)]
struct Scanner {
    buffer: Vec<String>,
}

impl Scanner {
    fn next<T: std::str::FromStr>(&mut self) -> T {
        loop {
            if let Some(token) = self.buffer.pop() {
                return token.parse().ok().expect("Failed parse");
            }
            let mut input = String::new();
            stdin().read_line(&mut input).expect("Failed read");
            self.buffer = input.split_whitespace().rev().map(String::from).collect();
        }
    }
}

fn main() {
    let mut scan = Scanner::default();
    let out = &mut BufWriter::new(stdout());

    let n = scan.next::<usize>();
    let q = scan.next::<usize>();

    let mut values: Vec<u64> = (0..n).map(|_| scan.next::<u64>()).collect();

    for i in 1..n {
        values[i] += values[i - 1];
    }

    for _ in 0..q {
        let a = scan.next::<usize>();
        let b = scan.next::<usize>();
        if a == 1 {
            writeln!(out, "{}", values[b - 1]);
        } else {
            writeln!(out, "{}", values[b - 1] - values[a - 2]);
        }
    }
}
