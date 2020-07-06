use std::cmp::Ordering;

impl Solution {
   pub fn reconstruct_queue(people: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
      let mut v = people.to_vec();
      v.sort_unstable_by(|x, y| {
         if x[0] > y[0] {
            Ordering::Less
         } else if x[0] == y[0] {
            if x[1] > y[1] {
               Ordering::Greater
            } else {
               Ordering::Less
            }
         } else {
            Ordering::Greater
         }
      });
      let mut res: Vec<Vec<i32>> = vec![];
      for i in v.iter() {
         res.insert(i[1] as usize, vec![i[0], i[1]]);
      }
      res
   }
}
