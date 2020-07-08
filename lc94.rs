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
use std::rc::Rc;
use std::cell::RefCell;
use std::collections::VecDeque;

impl Solution {
    pub fn inorder_traversal(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<i32> {
        match root {
            Some(v) => {
                let mut p = Some(v.clone());
                let mut s = VecDeque::new();
                let mut ret = VecDeque::new();
                while p.is_some() || !s.is_empty() {
                    while let Some(a) = p {
                        p = a.borrow().left.clone();
                        s.push_front(a.clone());
                    }
                    if let Some(a) = s.pop_front() {
                        let l = a.borrow();
                        ret.push_back(l.val);
                        p = l.right.clone();
                    }
                }
                Vec::from(ret)
            },
            None => vec![]
        }
    }
}
