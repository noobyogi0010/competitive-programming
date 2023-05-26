# Binary Search Tree
Lets understand this with the help of a problem, **Runway Reservation System**.

## Define The Problem
- You are given an airport with a single runway.
- Reservations for future landings.
- Reserve request for landings. They will specify timings for landing as *t*.
- Add *t* to the set *R* if no other landings are scheduled within *k* mins. For simplicities sake we are going to keep *k* as `3` mins.
- Remove from the set *R* after plane lands.

## Define Goal For The Problem
- `|R| = n`
- This implementation should take at max `log(n)`.

## Try Out Diff DS
- Unsorted Array: Searching a point of insertion will take `n` time and inserting the time `t` will also take `n` time which is more then our requirement. 
- Sorted Array: Searching will take `log(n)` by using binary search but insertion will take `n` time because we would need to shift every element to the right of insertion point which is more than our requirement.
- Sorted Linked List: We can perform insertion in constant time but searching an element will take linear time ie `n` time which is more than our requirement.
- Min/Max Heap: Finding an element in heap will take linear time ie `n` time. (*need to review heaps*)
So, sorted array is very close to our requirement. We just want a way to do fast insertion. Hence comes **BST**!

## Decoding BST
- BST is a bit complex DS as compared to sorted arrays.
- Let `x` be a node in BST. Then this node will have 3 pointers and key value which will be `parent(x)` pointer for parent node, `left(x)` for left child, and `right(x)` for right child.
- The prettiest property of a BST is that for all nodes `x`, if `y` is a left sub-tree of `x` then `key(y) <= key(x)`. Likewise, if `y` is a right sub-tree of `x` then `key(y) >= key(x)`.



