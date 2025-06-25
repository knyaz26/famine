from scipy.spatial import cKDTree

class Mediator():
    def __init__(self):
        self.colonists = []
        self.food_list = []

    def get_objects(self, colonists, food):
        self.colonists = colonists
        self.food_list = food

    def build_tree(self):
        food_pos_list = [(f.pos_x, f.pos_y) for f in self.food_list]
        tree = cKDTree(food_pos_list)
        for i in self.colonists:
            dists, idx = tree.query((i.pos_x, i.pos_y))
            i.target = self.food_list[idx]

mediator = Mediator()
