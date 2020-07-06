impl Solution {
   pub fn decompress_rl_elist(nums: Vec<i32>) -> Vec<i32> {
      let mut v: Vec<i32> = Vec::new();
      let mut i = 0;
      loop {
          if i > nums.len() - 1 {
              break;
          }
          let freq = nums[i];
          let n = nums[i + 1];
          for _ in 0 .. freq {
              v.push(n);
          }
          i += 2;
      }
      v
   }
}
