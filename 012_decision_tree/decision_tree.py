from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_graphviz
dataset=[
    [1,0,0,1,0],
    [1,0,0,2,0],
    [1,1,0,2,1],
    [1,1,1,1,1],
    [1,0,0,1,0],
    [2,0,0,2,0],
    [2,0,0,2,0],
    [2,1,1,2,1],
    [2,0,1,3,1],
    [2,0,1,2,1],
    [3,0,1,3,1],
    [3,0,1,2,1],
    [3,1,0,3,1],
    [3,1,0,3,1],
    [3,0,0,1,0]
]
feature =['年龄','没有工作','没有自己的房子','信贷情况']
classname =['不借','借']

X = [x[0:4] for x in dataset]
print(X)
Y = [y[-1] for y in dataset]
print(Y)
tree_clf = DecisionTreeClassifier(max_depth=4)
tree_clf.fit(X, Y)

export_graphviz(
            tree_clf,
            out_file=("loan.dot"),
            feature_names=feature,
            class_names=classname,
            rounded=True,
            filled=True,

        )

import re
# 打开 dot_data.dot，修改 fontname="支持的中文字体"
f = open("./loan.dot", "r+", encoding="utf-8")
open('./Tree_utf8.dot', 'w', encoding="utf-8").write(re.sub(r'fontname=helvetica', 'fontname="Microsoft YaHei"', f.read()))
f.close()


'''
dot -Tpng loan.dot -o loan.png
生成图片
'''

