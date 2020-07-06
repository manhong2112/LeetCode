impl Solution {
   pub fn search(nums: Vec<i32>, target: i32) -> i32 {
      let mut size = nums.len();
      let mut left = 0usize;
      if size == 0 {
         -1
      } else if size == 2 {
         if nums[0] == target {
            0
         } else if nums[1] == target {
            1
         } else {
            -1
         }
      } else {
         while size > 1 {
            let half = size / 2;
            let mid = left + half;
            let right = left + size - 1;
            println!("{} {} {}", left, mid, size);
            if nums[mid] == target {
               return mid as i32;
            } else if nums[left] <= nums[mid] {
               if nums[left] <= target && target <= nums[mid] {
                  return Solution::binarySearch(&nums, target, left, half);
               } else {
                  left = mid;
                  size -= half;
               }
            } else if mid + 1 < nums.len() && nums[mid + 1] <= nums[right] {
               if nums[mid + 1] <= target && target <= nums[right] {
                  return Solution::binarySearch(&nums, target, mid + 1, size - half - 1);
               } else {
                  size -= half;
               }
            } else {
               if size == 2 {
                  if nums[0] == target {
                     return 0;
                  } else if nums[1] == target {
                     return 1;
                  } else {
                     return -1;
                  }
               } else {
                  return -1;
               }
            }
         }
         println!("{} {}", left, size);
         if nums[left] == target {
            left as i32
         } else {
            -1
         }
      }
   }

   pub fn binarySearch(nums: &Vec<i32>, target: i32, left: usize, size: usize) -> i32 {
      println!("binarySearch {} {}", left, size);
      let mut size = size;
      if size == 0 {
         return -1;
      }
      let mut left = left;
      while size > 1 {
         let half = size / 2;
         let mid = left + half;
         if nums[mid] <= target {
            left = mid
         }
         size -= half;
      }

      if nums[left] == target {
         left as i32
      } else {
         -1
      }
   }
}
