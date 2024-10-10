class MyPlayer:
    """_summary_ Player plays move that give the most points meaning if in matrix of pay-off 
        C gives more points than D, player plays C and vica-versa.
    """    
    def __init__(self, pay_off_matrix:[[],[]], iteration_count=None):
        if iteration_count is not None:
            self.iter_count = iteration_count
        else:
            self.iter_count = iteration_count
        self.pay_off_matrix = pay_off_matrix
        self.move_history: [()] = []
            
            
    def select_move(self) -> bool:
        return True
    
    def record_last_moves(self, input1, input2):
        self.move_history.append((input1, input2))    

    def count_matrix(self)

if __name__ == "__main__":
    