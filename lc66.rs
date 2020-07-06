impl Solution {
   pub fn plus_one(digits: Vec<i32>) -> Vec<i32> {
      let mut k = digits;
      let l = k.len();
      k[l - 1] += 1;
      for n in 1..l {
         if k[l - n] == 10 {
            k[l - n] = 0;
            k[l - n - 1] += 1;
         }
      }
      if k[0] == 10 {
         k[0] = 0;
         k.insert(0, 1);
      }
      k
   }
}
