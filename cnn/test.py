import numpy as np
from resTree import BTree
from ansBean import Bean
# 前序遍历函数
def preorder(node):
    if node.data != None:
        node.show()
        if node.left:
            preorder(node.left)
        if node.middle:
            preorder(node.middle)
        if node.right:
            preorder(node.right)

def init(parent,ans,i):
    dimension = np.shape(ans)
    if i < dimension[0]-1:

        leftchild = parent.insertleft(i,0,ans[i][0][0],ans[i][0][1])
        init(leftchild,ans,i+1)
        middlechild = parent.insertmiddle(i,1,ans[i][1][0],ans[i][1][1])
        init(middlechild, ans, i + 1)
        rightchild = parent.insertright(i,2,ans[i][2][0],ans[i][2][1])
        init(rightchild, ans, i + 1)

def cal_road(node, list):  # 遍历二叉树所有分支,需要给函数传入一个存放结果的空列表
    if (node.left == None and node.middle == None and node.right == None):
        node.show()
        list.append(node.data)
    if node.left != None:
        node.left.data.setresult(node.data.getresult()+ node.left.data.getresult())
        cal_road(node.left, list)
    if node.middle != None:
        node.middle.data.setresult(node.data.getresult() + node.middle.data.getresult())
        cal_road(node.middle, list)
    if node.right != None:
        node.right.data.setresult(node.data.getresult() + node.right.data.getresult())
        cal_road(node.right, list)

if __name__ == '__main__':
    # test(0)
    ans = [
        [
            [1, 0.73787034],
            [2, 0.13283059],
            [3, 0.085309468]
        ],
        [
            [4, 0.97359949],
            [5, 0.015085977],
            [6, 0.0038305908]
        ],
        [
            [7, 0.81347722],
            [8, 0.089165218],
            [9, 0.049395841]
        ],
        [
            [13, 0.70233637],
            [16, 0.20754124],
            [1, 0.075191125]
        ]
    ]
    dimension = np.shape(ans)
    root = BTree(-1,-1,0,0)
    init(root, ans, 0)

    preorder(root)
    result_L = []
    print("emmm")
    cal_road(root, result_L)
    print("22")
    for i in range(len(result_L)):
        for j in range(dimension[1]):
            if result_L[i].getresult() == ans[dimension[0]-1][j][0]:
                print((i,j,result_L[i].tostring()))

