impl Solution {
   pub fn island_perimeter(grid: Vec<Vec<i32>>) -> i32 {
      fn get(grid: &Vec<Vec<i32>>, x: usize, y: usize) -> i32 {
         if x < 0 || x >= grid[0].len() || y < 0 || y >= grid.len() {
            0
         } else {
            *grid.get(y).unwrap().get(x).unwrap()
         }
      }
      let mut counting = 0;
      'main: loop {
         for y in 0..grid.len() {
            for x in 0..grid[y].len() {
               if get(&grid, x, y) == 1 {
                  if get(&grid, x - 1, y) == 0 {
                     counting += 1;
                  }
                  if get(&grid, x, y - 1) == 0 {
                     counting += 1;
                  }
                  if get(&grid, x + 1, y) == 0 {
                     counting += 1;
                  }
                  if get(&grid, x, y + 1) == 0 {
                     counting += 1;
                  }
               }
            }
         }
      }

      counting
   }
}
