# problem4.py

class Queens:
    def init(self, size):
        self.size = size
        self.answer = 0
        self.result()
    def check(self, pos, row, col)
        for i in range(row):
            if pos[i]== col or \
                pos[i] - i == col - row or \
                    pos[i] + i == col + row:
            
            return False
        return True
    def place(self,pos,row):
        if row == self.size:
            self.show(pos)
            self.answer += 1
        else:
            for col in range(self.size):
                if self.checkplace(pos,row,col)
                    pos[row]=col
                    self.place(pos,row+1)
                    if row == self.size:
                        return
                        
    def result(self):
        pos = [-1] * self.size
        self.place(pos,0)
        print("Amount of solutions: ", self.answer)
    def show(self,pos):
        for row in range(self.size):
            l = ""
            for col in range(self.size):
                if pos[row] == col:
                    l += "1"
                else:
                    l += "0"
            print(l)
        print("\n")
    
    
def main():
    Queens(8)

main()
