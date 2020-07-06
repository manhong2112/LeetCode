use std::collections::VecDeque;

impl Solution {
   pub fn running_sum(nums: Vec<i32>) -> Vec<i32> {
      Vec::from(nums.iter().fold(VecDeque::new(), |mut acc, &v| {
         if acc.is_empty() {
            acc.push_back(v);
            acc
         } else {
            acc.push_back(acc[acc.len() - 1] + v);
            acc
         }
      }))
   }
}
