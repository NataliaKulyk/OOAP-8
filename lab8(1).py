from collections import deque

# Клас, що представляє вузол дерева
class Node:
    def __init__(self, name):
        self.name = name
        self.children = []

# Клас, що представляє дерево
class Tree:
    def __init__(self, root_name):
        self.root = Node(root_name)

    # Метод для додавання дитини до батьківського вузла
    def add_child(self, parent_name, child_name):
        parent_node = self.find_node(self.root, parent_name)
        if parent_node:
            child_node = Node(child_name)
            parent_node.children.append(child_node)

    # Метод для пошуку вузла по імені
    def find_node(self, current_node, name):
        if current_node.name == name:
            return current_node
        for child in current_node.children:
            result = self.find_node(child, name)
            if result:
                return result
        return None

# Клас ітератора для обходу дерева в ширину
class TreeIterator:
    def __init__(self, tree):
        self.queue = deque()
        self.queue.append(tree.root)

    def __iter__(self):
        return self

    def __next__(self):
        if not self.queue:
            raise StopIteration
        current_node = self.queue.popleft()
        for child in current_node.children:
            self.queue.append(child)
        return current_node.name

# Створення дерева з географічними назвами
geography_tree = Tree("Україна")
geography_tree.add_child("Україна", "Київська область")
geography_tree.add_child("Київська область", "Києво-Святошинський район")
geography_tree.add_child("Києво-Святошинський район", "Софіївська Борщагівка")
geography_tree.add_child("Софіївська Борщагівка", "Центральна вулиця")

# Ітерація через дерево в ширину
iterator = TreeIterator(geography_tree)
for node in iterator:
    print(node)
