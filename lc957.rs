impl Solution {
   pub fn prison_after_n_days(cells: Vec<i32>, mut n: i32) -> Vec<i32> {
      if n == 0 {
         return cells;
      }
      n -= 1;
      let mut cache: Vec<Option<i32>> = vec![None; 64];
      let mut k = vec![0; 8];
      for i in 1..7 {
         if cells[i - 1] == cells[i + 1] {
            k[i] = 1;
         }
      }
      println!("{}", toKey(&k));
      cache[toKey(&k)] = Some(n);
      fn toKey(cells: &Vec<i32>) -> usize {
         ((cells[1] << 5)
            + (cells[2] << 4)
            + (cells[3] << 3)
            + (cells[4] << 2)
            + (cells[5] << 1)
            + (cells[6] << 0)) as usize
      }
      while n != 0 {
         n -= 1;
         let mut v = vec![0; 8];
         for i in 1..7 {
            if k[i - 1] == k[i + 1] {
               v[i] = 1;
            }
         }
         k = v;
         if cache[toKey(&k)].is_some() {
            n %= cache[toKey(&k)].unwrap() - n;
         }
         cache[toKey(&k)] = Some(n);
      }
      return k;
   }
}
