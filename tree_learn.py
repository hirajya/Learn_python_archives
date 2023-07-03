# class TreeNode:
#     def __init__(self, name, designation):
#         self.name = name
#         self.designation = designation
#         self.children = []
#         self.parent = None
#
#     def get_level(self):
#         level = 0
#         p = self.parent
#         while p:
#             level += 1
#             p = p.parent
#
#         return level
#
#     def print_type(self, type_value):
#         spaces = ' ' * self.get_level() * 3
#         prefix = spaces + "|__" if self.parent else ""
#         if type_value == 'name':
#             print(prefix + self.name)
#         if type_value == 'designation':
#             print(prefix + self.designation)
#         if type_value == 'both':
#             print(f'{prefix}{self.name} ({self.designation})')
#
#     def print_tree(self, type_value):
#         self.print_type(type_value)
#         for child in self.children:
#             child.print_tree(type_value)
#
#     def add_child(self, child):
#         child.parent = self
#         self.children.append(child)
#
#
# def build_product_tree():
#     root = TreeNode('Nilupul', 'CEO')
#
#     CTO = TreeNode("Chinmay", 'CTO')
#     IH = TreeNode("Vishwa", 'Infrastructure Head')
#     IH.add_child(TreeNode("Dhaval", 'Cloud Manager'))
#     IH.add_child(TreeNode("Abhijit", 'App Manager'))
#     CTO.add_child(IH)
#
#     CTO.add_child(TreeNode('Aamir', 'Application Head'))
#
#     HR_Head = TreeNode("Gels", 'HR Head')
#     HR_Head.add_child(TreeNode("Peter",'Recruitment Manager'))
#     HR_Head.add_child(TreeNode("Waqas", 'Policy Manager'))
#
#     root.add_child(CTO)
#     root.add_child(HR_Head)
#
#     return root
#
#
# if __name__ == '__main__':
#     root = build_product_tree()
#     root.print_tree('name')

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level

    def print_tree(self, level):
        if self.get_level() > level:
            return
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + '|__' if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree(level)

    def add_child(self, child):
        child.parent = self
        self.children.append(child)


def build_product_tree():
    root = TreeNode('Global')

    india = TreeNode('India')

    gujarat = TreeNode('Gujarat')
    gujarat.add_child(TreeNode('Ahmedabad'))
    gujarat.add_child(TreeNode('Baroda'))

    karnataka = TreeNode('Karnataka')
    karnataka.add_child(TreeNode('Bangluru'))
    karnataka.add_child(TreeNode('Mysore'))

    usa = TreeNode('USA')

    new_jersey = TreeNode('New Jersey')
    new_jersey.add_child(TreeNode('Princeton'))
    new_jersey.add_child(TreeNode('Trenton'))

    california = TreeNode('California')
    california.add_child(TreeNode('San Francisco'))
    california.add_child(TreeNode('Mountain View'))
    california.add_child(TreeNode('Palo Alto'))

    root.add_child(india)
    root.add_child(usa)

    india.add_child(gujarat)
    india.add_child(karnataka)

    usa.add_child(new_jersey)
    usa.add_child(california)

    return root


if __name__ == '__main__':
    root_node = build_product_tree()
    root_node.print_tree(1)
