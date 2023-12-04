/// Definition for singly-linked list.
#[derive(PartialEq, Eq, Clone, Debug)]
pub struct ListNode {
  pub val: i32,
  pub next: Option<Box<ListNode>>
}

impl ListNode {
  #[inline]
  fn new(val: i32) -> Self {
    ListNode {
      next: None,
      val
    }
  }
}

pub fn reorder_list(head: &mut Option<Box<ListNode>>) {
}

pub fn reorder_list_linear_memory(head: &mut Option<Box<ListNode>>) {
    let mut v = Vec::<Option<Box<ListNode>>>::new();
    while let Some(mut node) = head.take() {
        *head = node.next.take();
        v.push(Some(node));
    }
    let (mut l, mut r) = (0, v.len() - 1);
    let mut runner = Some(Box::new(ListNode::new(0)));
    let mut dummy = ListNode::new(0);
    dummy.next = runner;
    while l < r {
        runner = v[l].take();
        runner.unwrap().next = v[r].take();
        l += 1;
        if l < r {

        }
    }
    let _ = head.insert(dummy.next.unwrap());
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn it_works() {
        let result = add(2, 2);
        assert_eq!(result, 4);
    }
}
