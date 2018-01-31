class Min_Max():

    def is_winning(self, board, player):
        for i in range(0,9,3):
            if board[i] == board[i+1] == board[i+2] == player:
                return True

        for i in range(3):
            if board[i] == board[i+3] == board[i+6] == player:
                return True

        if board[0] == board[4] == board[8] == player:
            return True

        if board[2] == board[4] == board[6] == player:
            return True

        return False

    def check_termination(self, board, player1, player2):
        value = 10 if player1 == self.jarvis else -10

        if self.is_winning(board, player1):
            return True, value
        
        elif self.is_winning(board, player2):
            return True, -value

        elif board.count('-') == 0:
            return True, 0

        else:
            return False, -1

    def min_max(self, board, player1, player2):

        termination, value = self.check_termination(board, player1, player2)
        if termination:
            return -1, value

        scores = {}
        for i in range (len(board)):
            if board[i] == '-':
                new_board = list(board)
                new_board[i] = player1
                scores[i] = self.min_max(new_board, player2, player1)[1]

        best_score = max([value for key, value in scores.items()]) if player1 == self.jarvis else min([value for key, value in scores.items()])

        for key, value in scores.items()    :
            if value == best_score:
                return key, value

    def run(self, board, jarvis, human):
        self.jarvis = jarvis
        self.human = human
        return self.min_max(board, self.jarvis, self.human)[0]

def print_board(board):
    for i in range(9):
        print(i,') ', board[i], end="  ")
        if ((i+1)%3 == 0):
            print() 

def main(): 
    game = Min_Max()
    board = '- - - - - - - - -'.split()
    while(1):
        print_board(board)
        index = int(input("Your move, enter the index:"))
        board[index] = 'O'
        board[game.run(board, 'X', 'O')] = 'X'



if __name__ == '__main__':
    main()
