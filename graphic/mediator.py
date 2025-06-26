from scipy.spatial import cKDTree

class Mediator():
    def __init__(self):
        pass
    
    def build_tree(self, colonists, food_list):
        if food_list:
            food_pos_list = [(f.pos_x, f.pos_y) for f in food_list]
            tree = cKDTree(food_pos_list)
            for i in colonists:
                dists, idx = tree.query((i.pos_x, i.pos_y))
                i.target = food_list[idx]

mediator = Mediator()
