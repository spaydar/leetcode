//! docs TODO put LeetCode problem description here

use utils::list_node::*;

/// docs TODO
pub fn reorder_list_constant_memory(_head: &mut Option<Box<ListNode>>) {}

/// docs TODO put solution explanation here
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

    fn create_n_list_nodes_reordered(mut n: i32) -> Option<Box<ListNode>> {
        let mut dummy = Some(Box::new(ListNode::new(0)));
        let mut r = &mut dummy;
        let mut i = 1;
        while i <= n {
            r.as_mut().unwrap().next = Some(Box::new(ListNode::new(i)));
            r = &mut r.as_mut().unwrap().next;
            i += 1;
            if i <= n {
                r.as_mut().unwrap().next = Some(Box::new(ListNode::new(n)));
                r = &mut r.as_mut().unwrap().next;
                n -= 1;
            }
        }
        dummy.unwrap().next
    }

    #[test]
    fn reorder_list_linear_memory_0_nodes() {
        let head = &mut create_n_list_nodes(0);
        reorder_list_linear_memory(head);
        let expected = create_n_list_nodes_reordered(0);
        assert_eq!(*head, expected);
    }

    #[test]
    fn reorder_list_linear_memory_1_node() {
        let head = &mut create_n_list_nodes(1);
        reorder_list_linear_memory(head);
        let expected = create_n_list_nodes_reordered(1);
        assert_eq!(*head, expected);
    }

    #[test]
    fn reorder_list_linear_memory_4_nodes() {
        let head = &mut create_n_list_nodes(4);
        reorder_list_linear_memory(head);
        let expected = create_n_list_nodes_reordered(4);
        assert_eq!(*head, expected);
    }

    #[test]
    fn reorder_list_linear_memory_5_nodes() {
        let head = &mut create_n_list_nodes(5);
        reorder_list_linear_memory(head);
        let expected = create_n_list_nodes_reordered(5);
        assert_eq!(*head, expected);
    }
}
