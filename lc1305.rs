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
   pub fn get_all_elements(
      root1: Option<Rc<RefCell<TreeNode>>>,
      root2: Option<Rc<RefCell<TreeNode>>>,
   ) -> Vec<i32> {
      fn to_sorted_vec(root: Option<Rc<RefCell<TreeNode>>>) -> VecDeque<i32> {
         fn f(v: &mut VecDeque<i32>, node: Option<Rc<RefCell<TreeNode>>>) {
            if node.is_some() {
               let t = node.unwrap();
               let k = t.borrow();
               f(v, k.left.clone());
               v.push_back(k.val);
               f(v, k.right.clone());
            }
         }
         let mut v: VecDeque<i32> = VecDeque::new();
         f(&mut v, root);
         v
      }
      let mut v1 = to_sorted_vec(root1);
      let mut v2 = to_sorted_vec(root2);
      let mut ret = VecDeque::new();
      while !v1.is_empty() && !v2.is_empty() {
         if v1[0] < v2[0] {
            ret.push_back(v1.pop_front().unwrap());
         } else {
            ret.push_back(v2.pop_front().unwrap());
         }
      }
      if v1.is_empty() {
         ret.extend(v2);
      } else {
         ret.extend(v1);
      }
      Vec::from(ret)
   }
}
