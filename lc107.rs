// Definition for a binary tree node.
// #[derive(Debug, PartialEq, Eq)]
// pub struct TreeNode {
//   pub val: i32,
//   pub left: Option<Rc<RefCell<TreeNode>>>,
//   pub right: Option<Rc<RefCell<TreeNode>>>,
// }
//
// impl TreeNode {
//   #[inline]
//   pub fn new(val: i32) -> Self {
//     TreeNode {
//       val,
//       left: None,
//       right: None
//     }
//   }
// }
use std::cell::RefCell;
use std::collections::VecDeque;
use std::rc::Rc;

impl Solution {
   pub fn level_order_bottom(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<Vec<i32>> {
      if root.is_none() {
         return vec![];
      }
      let mut res: Vec<Vec<i32>> = vec![];
      let mut q = VecDeque::with_capacity(10);
      q.push_front(root.unwrap());
      while !q.is_empty() {
         let mut r2: Vec<i32> = vec![];
         for _ in 0..q.len() {
            let n = q.pop_front().unwrap();
            let n = n.borrow();
            if let Some(left) = n.left.clone() {
               q.push_back(left);
            }
            if let Some(right) = n.right.clone() {
               q.push_back(right);
            }
            r2.push(n.val);
         }
         res.push(r2);
      }
      res.reverse();
      res
   }
}
