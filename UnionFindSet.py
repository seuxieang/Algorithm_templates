# 并查集模版 dict
class UnionFindSet:
    """并查集"""
    def __init__(self, data_list):
        """初始化两个字典，一个保存节点的父节点，另外一个保存父节点的大小
        初始化的时候，将节点的父节点设为自身，size设为1"""
        self.father_dict = {}
        self.size_dict = {}
        self.count = len(data_list)
        for node in data_list:
            self.father_dict[node] = node
            self.size_dict[node] = 1

    def find(self, node):
        """使用递归的方式来查找父节点

        在查找父节点的时候，顺便把当前节点移动到父节点上面
        这个操作算是一个优化
        """
        if node is None or node not in self.father_dict:
            return
        father = self.father_dict[node]
        if(node != father):
            if father != self.father_dict[father]:    # 在降低树高优化时，确保父节点大小字典正确
                self.size_dict[father] -= 1
            father = self.find(father)
        self.father_dict[node] = father
        return father

    def is_same_set(self, node_a, node_b):
        """查看两个节点是不是在一个集合里面"""
        return self.find(node_a) == self.find(node_b)

    def union(self, node_a, node_b):
        """将两个集合合并在一起"""
        if node_a is None or node_b is None:
            return

        a_head = self.find(node_a)
        b_head = self.find(node_b)

        if(a_head != b_head):
            self.count -= 1
            a_set_size = self.size_dict[a_head]
            b_set_size = self.size_dict[b_head]
            if(a_set_size >= b_set_size):
                self.father_dict[b_head] = a_head
                self.size_dict[a_head] = a_set_size + b_set_size
            else:
                self.father_dict[a_head] = b_head
                self.size_dict[b_head] = a_set_size + b_set_size

    def isolate(self,node):
        '''孤立一个节点'''
        if node is None or node not in self.father_dict:
            return
        if self.find(node) == node:
            return
        self.father_dict[node] = node
        self.size_dict[node] = 1
        self.count += 1

# 并查集模版 list
class UnionFindSet:
    """并查集"""
    def __init__(self, n):
        """初始化两个字典，一个保存节点的父节点，另外一个保存父节点的大小
        初始化的时候，将节点的父节点设为自身，size设为1"""
        self.father_list = list(range(n))
        self.size_list = [1] * n
        self.count = n


    def find(self, node):
        """使用递归的方式来查找父节点

        在查找父节点的时候，顺便把当前节点移动到父节点上面
        这个操作算是一个优化
        """
        # if node >= len(self.father_list):
        #     return
        father = self.father_list[node]
        if(node != father):
            if father != self.father_list[father]:    # 在降低树高优化时，确保父节点大小字典正确
                self.size_list[father] -= 1
            father = self.find(father)
        self.father_list[node] = father
        return father

    def is_same_set(self, node_a, node_b):
        """查看两个节点是不是在一个集合里面"""
        # if node_a >= len(self.father_list) or node_b >= len(self.father_list):
        #     return
        return self.find(node_a) == self.find(node_b)

    def union(self, node_a, node_b):
        """将两个集合合并在一起"""
        # if node_a >= len(self.father_list) or node_b >= len(self.father_list):
        #     return

        a_head = self.find(node_a)
        b_head = self.find(node_b)

        if(a_head != b_head):
            self.count -= 1
            a_set_size = self.size_list[a_head]
            b_set_size = self.size_list[b_head]
            if(a_set_size >= b_set_size):
                self.father_list[b_head] = a_head
                self.size_list[a_head] = a_set_size + b_set_size
            else:
                self.father_list[a_head] = b_head
                self.size_list[b_head] = a_set_size + b_set_size

    def isolate(self,node):
        '''孤立一个节点'''
        # if node >= len(self.father_list):
        #     return
        self.father_list[node] = node
        self.size_list[node] = 1
        self.count += 1

# 带权并查集
class UnionFindSetWithValue:
    def __init__(self):
        """
        记录每个节点的父节点
        记录每个节点到根节点的权重
        """
        self.father = {}
        self.value = {}

    def find(self, x):
        """
        查找根节点
        路径压缩
        更新权重
        """
        root = x
        # 节点更新权重的时候要放大的倍数
        base = 1
        while self.father[root] != None:
            root = self.father[root]
            base *= self.value[root]

        while x != root:
            original_father = self.father[x]
            ##### 离根节点越远，放大的倍数越高
            self.value[x] *= base
            base /= self.value[original_father]
            #####
            self.father[x] = root
            x = original_father

        return root

    def merge(self, x, y, val):
        """
        合并两个节点
        """
        root_x, root_y = self.find(x), self.find(y)

        if root_x != root_y:
            self.father[root_x] = root_y
            ##### 四边形法则更新根节点的权重
            self.value[root_x] = self.value[y] * val / self.value[x]

    def is_connected(self, x, y):
        """
        两节点是否相连
        """
        return x in self.value and y in self.value and self.find(x) == self.find(y)

    def add(self, x):
        """
        添加新节点，初始化权重为1.0
        """
        if x not in self.father:
            self.father[x] = None
            self.value[x] = 1.0

