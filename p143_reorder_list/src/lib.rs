//! docs TODO put LeetCode problem description here

use utils::list_node::*;

/// docs TODO
pub fn reorder_list(_head: &mut Option<Box<ListNode>>) {}

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

    #[test]
    fn reorder_list_linear_memory_0_nodes() {
        let head = &mut create_n_list_nodes(0);
        reorder_list_linear_memory(head);
        assert_eq!(*head, None);
    }

    #[test]
    fn reorder_list_linear_memory_1_node() {
        let head = &mut create_n_list_nodes(1);
        reorder_list_linear_memory(head);
        let expected = Some(Box::new(ListNode { val: 1, next: None }));
        assert_eq!(*head, expected);
    }

    #[test]
    fn reorder_list_linear_memory_4_nodes() {
        let head = &mut create_n_list_nodes(4);
        reorder_list_linear_memory(head);
        let expected = Some(Box::new(ListNode {
            val: 1,
            next: Some(Box::new(ListNode {
                val: 4,
                next: Some(Box::new(ListNode {
                    val: 2,
                    next: Some(Box::new(ListNode { val: 3, next: None })),
                })),
            })),
        }));
        assert_eq!(*head, expected);
    }

    #[test]
    fn reorder_list_linear_memory_5_nodes() {
        let head = &mut create_n_list_nodes(5);
        reorder_list_linear_memory(head);
        let expected = Some(Box::new(ListNode {
            val: 1,
            next: Some(Box::new(ListNode {
                val: 5,
                next: Some(Box::new(ListNode {
                    val: 2,
                    next: Some(Box::new(ListNode {
                        val: 4,
                        next: Some(Box::new(ListNode { val: 3, next: None })),
                    })),
                })),
            })),
        }));
        assert_eq!(*head, expected);
    }
}
