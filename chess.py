import itertools
import string

def calculation_nearly_points(may_move, point):
    varie = may_move
    for i in may_move:
        pass


class Deck:
    def __init__(self, x: int=8, y: int=8):
        self.x = x
        self.y = y
        self.grid_x = [string.ascii_uppercase[i - 1] for i in range(1, self.x+1)]
        self.grid_y = [i for i in range(1, self.y+1)]
        self.play_deck = self.generation_play_deck()

    def generation_play_deck(self):
        cells_iterabl = [i for i in itertools.product(self.grid_y, self.grid_x)]
        cells = []
        for i in cells_iterabl:
            cells.append({
                "name": f"{i[0]}_{i[1]}",
                "x": string.ascii_uppercase.find(i[1])+1,
                "y": i[0],
                "color": "",
                "figure": None,
            })
        return cells

    def add_fidure(self, figure, cell: str):
        for i in self.play_deck:
            if i["name"] == cell:
                if i["figure"] == None:
                    i["figure"] = figure


class Figure:

    def __init__(self, name, play_deck):
        self.name = name
        self.play_deck = play_deck
        #self.position = self.position_calculation()

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def position_calculation(self):
        for i in self.play_deck:
            if i["figure"] == self:
                return i

    def to_move(self, cell):
        for i in self.play_deck:
            if i["figure"] == self:
                i["figure"] = None
            if i["name"] == cell:
                i["figure"] = self


class Horse(Figure):

    def __init__(self, name, palay_deck):
        self.name = name
        self.play_deck= palay_deck
        super(Horse, self).__init__(name=self.name, play_deck=self.play_deck)


    def varies_move(self):
        x = self.position_calculation()["x"]
        y = self.position_calculation()["y"]
        path = [[x+1, y+2], [x+2, y+1], [x+2, y-1], [x+1, y-2], [x-1, x-2], [x-2, y-1], [x-2, y+1], [x-1, y+2]]
        index = set()
        for i in path:
            for j in i:
                if j <= 0:
                    index.add(path.index(i))

        while len(index) != 0:
            path.pop(max(index))
            index.remove(max(index))
        return path

    def varies_two_move(self):
        x = self.position_calculation()["x"]
        y = self.position_calculation()["y"]
        path = [[x-3, y+3], [x-1, y+3], [x+1, y+3], [x+3, y+3], [x+3, y+1], [x+3, y-1], [x+3, y-3], [x+1, y-3], [x-1, y-3], [x-3, y-3],
                [x-3, y-1], [x-3, y+1], [x, y+2], [x+2, y], [x, y-2], [x-2, y], [x-1, y+1], [x+1, y+1], [x+1, y-1], [x-1, y-1]]
        index = set()
        for i in path:
            for j in i:
                if j <= 0:
                    index.add(path.index(i))

        while len(index) != 0:
            path.pop(max(index))
            index.remove(max(index))
        return path

    def varies_three_move(self):
        x = self.position_calculation()["x"]
        y = self.position_calculation()["y"]
        path = [[x-2, y+3], [x, y+3], [x+2, y+3], [x+3, y+2], [x+3, y], [x+3, y-2], [x+2, y-3], [x, y-3], [x-2, y-3], [x-3, y-2], [x-3, y],
                [x-3, y+2], [x-2, y+2], [x+2, y+2], [x+2, y-2], [x-2, y-2], [x-1, y], [x, y+1], [x+1, y], [x, y-1]]
        index = set()
        for i in path:
            for j in i:
                if j <= 0:
                    index.add(path.index(i))

        while len(index) != 0:
            path.pop(max(index))
            index.remove(max(index))
        return path





if __name__ == '__main__':

    deck_1 = Deck()
    horse_black = Horse("horse_black", deck_1.play_deck)
    deck_1.add_fidure(horse_black, "1_B")
    point = Horse("point", deck_1.play_deck)
    deck_1.add_fidure(point, "7_F")

    one_move_point = point.varies_move()
    two_move_point = point.varies_two_move()
    three_move_point = point.varies_three_move()

    one_move_horse = horse_black.varies_move()
    two_move_horse = horse_black.varies_two_move()
    three_move_horse = horse_black.varies_three_move()

    print(horse_black.varies_move())
    print(horse_black.varies_two_move())
    print(horse_black.varies_three_move())
    print(deck_1.play_deck)



