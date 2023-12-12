/// Definition for singly-linked list.
#[derive(PartialEq, Eq, Clone, Debug)]
pub struct ListNode {
    pub val: i32,
    pub next: Option<Box<ListNode>>,
}

impl ListNode {
    /// Create a new `ListNode` with no `next` node
    #[inline]
    pub fn new(val: i32) -> Self {
        ListNode { val, next: None }
    }
}

/// Create a singly-linked list containing `n` nodes
pub fn create_n_list_nodes(n: i32) -> Option<Box<ListNode>> {
    let mut i = 1;
    let mut dummy = Some(Box::new(ListNode::new(0)));
    let mut r = &mut dummy;
    while i <= n {
        r.as_mut().unwrap().next = Some(Box::new(ListNode::new(i)));
        r = &mut r.as_mut().unwrap().next;
        i += 1;
    }
    dummy.unwrap().next
}

/// Add line `println!("create_n_list_nodes(x) {:#?}", l);` and run `cargo test -- --nocapture`
/// to view ListNode structure in the console.
#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn create_0_list_nodes() {
        let l = create_n_list_nodes(0);
        assert_eq!(l, None);
    }

    #[test]
    fn create_1_list_nodes() {
        let l = create_n_list_nodes(1);
        let expected = Some(Box::new(ListNode { val: 1, next: None }));
        assert_eq!(l, expected);
    }

    #[test]
    fn create_4_list_nodes() {
        let l = create_n_list_nodes(4);
        let expected = Some(Box::new(ListNode {
            val: 1,
            next: Some(Box::new(ListNode {
                val: 2,
                next: Some(Box::new(ListNode {
                    val: 3,
                    next: Some(Box::new(ListNode { val: 4, next: None })),
                })),
            })),
        }));
        assert_eq!(l, expected);
    }

    #[test]
    fn create_5_list_nodes() {
        let l = create_n_list_nodes(5);
        let expected = Some(Box::new(ListNode {
            val: 1,
            next: Some(Box::new(ListNode {
                val: 2,
                next: Some(Box::new(ListNode {
                    val: 3,
                    next: Some(Box::new(ListNode {
                        val: 4,
                        next: Some(Box::new(ListNode { val: 5, next: None })),
                    })),
                })),
            })),
        }));
        assert_eq!(l, expected);
    }
}
