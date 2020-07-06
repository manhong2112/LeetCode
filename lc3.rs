use std::cmp::max;
use std::collections::HashMap;

impl Solution {
   pub fn length_of_longest_substring(s: String) -> i32 {
      let s: Vec<char> = s.chars().collect();
      let mut cs: HashMap<char, usize> = HashMap::new();
      let mut i = 0usize;
      let mut j = 0usize;
      let mut max_len = 0;
      while j < s.len() {
         match cs.get(&s[j]) {
            Some(&v) if v >= i => {
               i = v + 1;
            }
            _ => {}
         }
         cs.insert(s[j], j);
         j += 1;
         max_len = max(max_len, (j - i) as i32);
      }
      max_len
   }
}
