import random

# A tree as an array or records:
# data left ptr right ptr

tree = [[-1, -1, -1] for _ in range(10)]
root = -1
nextEmpty = 0


def insert(num):
    global root, nextEmpty

    # print("inserting", num)
    # If tree is empty (no root), create a node holding key k as root; done
    if root == -1:  # -1 means none
        root = 0
        tree[root][0] = num
        nextEmpty += 1
        return

    # Set CurrNode = RootNode and commence search
    currNode = root

    while True:

        # If k< CurrNode.key ... /* key must go in left subtree */
        if num < tree[currNode][0]:

            # If CurrNode.left == NULL, create a node holding k as left child of CurrNode; done.
            if tree[currNode][1] == -1:
                tree[currNode][1] = nextEmpty
                tree[nextEmpty][0] = num
                nextEmpty += 1
                return
            # else set CurrNode = CurrNode.left, and go to 3.
            else:
                currNode = tree[currNode][1]

        # elif k > CurrNode.key ... /* key must go in right subtree */
        elif num > tree[currNode][0]:

            # If CurrNode.right == NULL, create a node holding k as left child of CurrNode; done.
            if tree[currNode][2] == -1:
                tree[currNode][2] = nextEmpty
                tree[nextEmpty][0] = num
                nextEmpty += 1
                return
            # else set CurrNode = CurrNode.right, and go to 3.
            else:
                currNode = tree[currNode][2]

        else:
            # k must equal CurrNode.key, done. /* No duplicate keys in a BST. */
            return


for _ in range(10):
    insert(random.randint(0, 1000))

print()


def searchtree(num, currNode):
    if tree[currNode][0] == -1:
        return False
    else:
        if num == tree[currNode][0]:
            return True
        else:
            if num < tree[currNode][0]:
                if tree[currNode][1] != -1:
                    return searchtree(num, tree[currNode][1])
                else:
                    return False
            if tree[currNode][2] != -1:
                return searchtree(num, tree[currNode][2])
            else:
                return False


# in order traversal
def inorder(p):
    if tree[p][1] != -1:
        inorder(tree[p][1])
    print(tree[p][0])
    if tree[p][2] != -1:
        inorder(tree[p][2])


# post order traversal
def postorder(p):
    if tree[p][1] != -1:
        postorder(tree[p][1])
    if tree[p][2] != -1:
        postorder(tree[p][2])
    print(tree[p][0])


# pre order traversal
def preorder(p):
    print(tree[p][0])
    if tree[p][1] != -1:
        preorder(tree[p][1])
    if tree[p][2] != -1:
        preorder(tree[p][2])


depth = 1
treelevel = []

# a tuple is added to list treelevel where it contains the value of the node and the level of the tree it is at
# this list is then sorted by level and prints the nodes that are smaller or equal than to the number of levels the user wants to print
def level(p, numd):
    global depth
    treelevel.append((tree[p][0], depth))
    if tree[p][1] != -1:
        depth += 1
        level(tree[p][1], numd)
        depth -= 1
    if tree[p][2] != -1:
        depth += 1
        level(tree[p][2], numd)
        depth -= 1


for i in tree:
    print(i)


while True:
    print(
        "enter: \n b for binary search \n in for inorder \n post for postorder \n pre for preorder \n q to quit \n l to print by level"
    )
    choice = input()
    if choice == "q":
        quit()
    if choice == "b":
        num = int(input("enter number to search"))
        print(searchtree(num, root))
    if choice == "in":
        inorder(root)
    if choice == "post":
        postorder(root)
    if choice == "pre":
        preorder(root)
    if choice == "l":
        levelchoice = int(input("enter number of levels to print from graph"))
        level(root, levelchoice)
        treelevel.sort(key=lambda x: x[1])
        print([i for i in treelevel if i[1] <= levelchoice])
