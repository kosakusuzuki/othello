#コマの管理

from .cell import Cell

class Board:
    DIRECTIONS = [
        (-1, -1),(-1, 0),(-1, 1),(0, -1),
        (0, 1),(1, -1),(1, 0),(1, 1)
    ]

    def __init__(self): #盤面を作る
        self.cells = [
            [Cell() for i in range (8)]
            for i in range(8)
        ]
        self.cells[3][3].stone = Cell.WHITE#初期配置
        self.cells[3][4].stone = Cell.BLACK
        self.cells[4][3].stone = Cell.BLACK
        self.cells[4][4].stone = Cell.WHITE

    def print_board(self):#盤面を表示する
        for row in self.cells:
            for cell in row:
                if cell.stone == Cell.BLACK:
                    print("B", end=" ")
                elif cell.stone == Cell.WHITE:
                    print("W", end=" ")
                elif cell.can_put:
                    print("*", end=" ")
                else:
                    print(".", end=" ")
            print()



    def put_stone(self, row: int, col: int, stone: int) -> bool:#石を置く
        if not self.can_put(row, col, stone):
            return False
        
        self.cells[row][col].stone = stone
        self.flip_stones(row, col,stone)
        return True
    
    def is_inside(self, row: int,col: int) -> bool:#盤面内か
        if 0 <=row < 8 and 0 <= col < 8:
            return True
        return False
    
    def get_stone(self, row: int, col: int) -> int | None:#指定したマスの石を取得
        if not self.is_inside(row, col):
            return None
        return self.cells[row][col].stone



    def get_next_stone(self, row: int, col: int, dr: int, dc: int) -> int | None:#隣の石に移動してget_stoneへ
        return self.get_stone(
            row + dr,col + dc
        )
    
    def has_opponent_in_direction(self, row: int, col: int, dr: int, dc:int, stone:int) -> bool:#相手の石を挟めるか
        row += dr
        col += dc
        if not self.is_inside(row,col):
            return False
        

        next_stone = self.get_stone(row,col)

        if next_stone != Cell.get_opponent(stone):
            return False
        
        while next_stone == Cell.get_opponent(stone):
            row += dr
            col += dc

            if not self.is_inside(row, col):
                return False
            
            next_stone = self.get_stone(row, col)

        return next_stone == stone
    
    def can_put(self, row: int, col: int, stone:int) -> bool:#そのマスに石を置けるか
        if self.get_stone(row,col) != Cell.EMPTY:
            return False
        
        for dr, dc in Board.DIRECTIONS:
            if self.has_opponent_in_direction(row, col, dr, dc, stone):
                return True
        
        return False
    
    def update_can_put(self, stone: int) -> None:#すべてのマスをチェック
        for row in range(8):
            for col in range(8):
                self.cells[row][col].can_put = self.can_put(row, col, stone)

    def flip_in_direction(self, row: int, col:int, dr: int, dc:int, stone:int) -> None:#ひっくり返す
        if not self.has_opponent_in_direction(row, col, dr, dc, stone):
            return
        row += dr
        col += dc

        while self.get_stone(row, col) != stone:
            self.cells[row][col].stone = stone
            row += dr
            col += dc

    def flip_stones(self, row:int, col:int, stone:int) -> None:
        for dr, dc in Board.DIRECTIONS:
            self.flip_in_direction(row, col, dr, dc, stone)

    def has_valid_move(self, stone: int) -> bool:#置けるマスがあるか確認
        for row in range(8):
            for col in range(8):
                if self.can_put(row, col, stone):
                    return True
        return False
    
    def count_stones(self) -> tuple[int, int]:
        black = 0
        white = 0

        for row in range(8):
            for col in range(8):
                stone = self.get_stone(row,col)

                if stone == Cell.BLACK:
                    black += 1
                elif stone == Cell.WHITE:
                    white += 1
        return black,white
        
    
                
       