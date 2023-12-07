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

pub fn reorder_list(_head: &mut Option<Box<ListNode>>) {
}

pub fn reorder_list_linear_memory(head: &mut Option<Box<ListNode>>) {
    use std::collections::VecDeque;
    let mut v = VecDeque::<Option<Box<ListNode>>>::new();
    while let Some(mut node) = head.take() {
        *head = node.next.take();
        v.push_back(Some(node));
    }
    let mut dummy = Some(Box::new(ListNode::new(0)));
    let mut runner = &mut dummy;
    while let Some(mut l_node) = v.pop_front() {
        runner.as_mut().unwrap().next = l_node.take();
        runner = &mut runner.as_mut().unwrap().next;
        if let Some(mut r_node) = v.pop_back() {
            runner.as_mut().unwrap().next = r_node.take();
            runner = &mut runner.as_mut().unwrap().next;
        }
    }
    *head = dummy.unwrap().next;
}

#[cfg(test)]
mod tests {
    use super::*;

    fn make_list_node_4() -> Option<Box<ListNode>> {
        let l4 = Some(Box::new(ListNode::new(4)));
        let mut l3 = Some(Box::new(ListNode::new(3)));
        let mut l2 = Some(Box::new(ListNode::new(2)));
        let mut l1 = Some(Box::new(ListNode::new(1)));
        l3.as_mut().unwrap().next = l4;
        l2.as_mut().unwrap().next = l3;
        l1.as_mut().unwrap().next = l2;
        l1
    }

    fn make_list_node_5() -> Option<Box<ListNode>> {
        let l5 = Some(Box::new(ListNode::new(5)));
        let mut l4 = Some(Box::new(ListNode::new(4)));
        let mut l3 = Some(Box::new(ListNode::new(3)));
        let mut l2 = Some(Box::new(ListNode::new(2)));
        let mut l1 = Some(Box::new(ListNode::new(1)));
        l4.as_mut().unwrap().next = l5;
        l3.as_mut().unwrap().next = l4;
        l2.as_mut().unwrap().next = l3;
        l1.as_mut().unwrap().next = l2;
        l1
    }
    //fn make_list_node(mut n: i32) -> Option<Box<ListNode>> {
    //    let mut l: &mut Option<Box<ListNode>> = &mut None;
    //    while n > 0 {
    //        let mut new = Some(Box::new(ListNode::new(n)));
    //        new.unwrap().next = *l;
    //        l = &mut new;
    //        n -= 1;
    //    }
    //    *l
    //}

    #[test]
    fn reorder_list_linear_memory_1() {
        let head = &mut Some(Box::new(ListNode { val: 1, next: None }));
        reorder_list_linear_memory(head);
        println!("reorder_list_linear_memory_1 {:#?}", head);
        //assert_eq!(result, 4);
    }

    #[test]
    fn reorder_list_linear_memory_4() {
        let head = &mut make_list_node_4();
        reorder_list_linear_memory(head);
        println!("reorder_list_linear_memory_4 {:#?}", head);
        //assert_eq!(result, 4);
    }

    #[test]
    fn reorder_list_linear_memory_5() {
        let head = &mut make_list_node_5();
        reorder_list_linear_memory(head);
        println!("reorder_list_linear_memory_5 {:#?}", head);
        //assert_eq!(result, 4);
    }

    // Run `cargo test -- --nocapture` to see println! output in stdout
    #[test]
    fn create_list_node() {
        println!("make_list_node_4 {:#?}", make_list_node_4());
        println!("make_list_node_5 {:#?}", make_list_node_5());
        //assert_eq!(result, 4);
    }
}
