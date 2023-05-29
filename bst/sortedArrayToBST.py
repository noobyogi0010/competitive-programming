"""
Created on: 29/05/2023
Created by: Yogesh
Description: How to create a BST from an acsending ordersorted array.
"""

class BST:
    def __init__(self, val=0, left=None, right=None):
        self.val=val
        self.left=left
        self.right=right

def sortedArrayToBST(nums):
    def traverse(left, right):
        if left>right: return None

        mid=(left+right)//2
        root=BST(nums[mid])
        root.left=traverse(left,mid-1)
        root.right=traverse(mid+1,right)

        return root
    return traverse(0,len(nums)-1)

def preorder(bst):
    if not bst:
        return None
    
    preorder(bst.left)
    print(bst.val)
    preorder(bst.right)

def main():
    arr=input()
    nums=list(map(int, arr.split(" ")))
    bst=sortedArrayToBST(nums)
    preorder(bst)

if __name__=="__main__":
    main()