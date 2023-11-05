import math # import math module

# Input Player Status
EMPTY = "-" #untuk mengisi posisi dalam papan ketidak awal bermain
PLAYER_X = "X" # X berupa simbol permainan untuk mewakili player
PLAYER_O = "O" # O berupa simbol permainan untuk mewakili player

# Papan Game
board = [EMPTY, EMPTY, EMPTY,
         EMPTY, EMPTY, EMPTY,
         EMPTY, EMPTY, EMPTY] #tata letak papan game

# Fungsi untuk Print Papan Game
def print_board(board): #untuk menjalankan fungsi print papan game
    print("-------------")#untuk membuat kolom pada papan game
    for i in range(3): #untuk membuat baris pada papan game
        print("|", board[i*3], "|", board[i*3 + 1], "|", board[i*3 + 2], "|")#untuk membuat pembatas antar kolom dalam papan game
        print("-------------")#untuk membuat kolom pada papan game

# Fungsi untuk Mengecek Pemenang
def check_winner(board):#untuk menjalankan fungsi mengecek pemenang
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Baris
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Kolom
        [0, 4, 8], [2, 4, 6]  # Diagonal
    ]

    for combination in winning_combinations:
        if board[combination[0]] == board[combination[1]] == board[combination[2]] != EMPTY: #Perintah untuk menjalankan aturan atau check-win.
            return board[combination[0]] #Jika ada pemenang maka akan mengembalikan nilai pemenang.

    if EMPTY not in board: #Jika tidak terdapat pemenang atau terjadi seri
        return "tie" #maka akan memunculkan pernyataan "tie"

    return None #maka akan kembali ke keadaan papan game awal, atau papan game yang belum dimainkan

# Fungsi untuk Evaluasi Pemenang dalam Game
def evaluate(board): #untuk menjalankan fungsi mengevaluasi
    winner = check_winner(board) #mengecek pemenang

    if winner == PLAYER_X: #Jika yang menang player X
        return 1 #maka akan mengembalikan nilai 1
    elif winner == PLAYER_O: #Jika yang menang player O
        return -1 #maka akan mengembalikan nilai -1
    else:
        return 0 #Jika tidak ada pemenang atau seri akan mengembalikan nilai 0

# Minimax Fungsi dan Aplha-Beta Pruning
def minimax(board, depth, alpha, beta, maximizing_player): #untuk menjalankan fungsi dalam minimax
    if check_winner(board) is not None or depth == 0: #Jika mengecek tidak terdapat pemenang
        return evaluate(board) #kembali atau ulangi evaluasi papan

    if maximizing_player: #jika komputer yang mejadi player
        max_eval = -math.inf #nilai maksimum adalah -infiniti
        for i in range(9): #untuk menjalankan fungsi minimax
            if board[i] == EMPTY: #jika pada papan game terdapat simbol "-" yang melambangkan EMPTY
                board[i] = PLAYER_X #atau terdapat simbol X pada papan game
                eval_score = minimax(board, depth - 1, alpha, beta, False) #maka akan mencari atau mengevaluasi minimax untuk mecari kemungkinan terbaik
                board[i] = EMPTY #pada papan game yang terdapat simbol "-" 
                max_eval = max(max_eval, eval_score) #nilai max-eval akan mencari nilai max tertinggi
                alpha = max(alpha, eval_score) #nilai alpha akan mencari nilai max tertinggi
                if beta <= alpha: #akan memastikan jika beta <= alpha
                    break #maka akan menghentikan fungsi minimax
        return max_eval #maka akan mengembalikan nilai max_eval
    else:
        min_eval = math.inf #nilai minimum adalah infiniti
        for i in range(9): #untuk menjalankan fungsi minimax
            if board[i] == EMPTY: #jika pada papan game terdapat simbol "-" yang melambangkan EMPTY
                board[i] = PLAYER_O #atau terdapat simbol O pada papan game
                eval_score = minimax(board, depth - 1, alpha, beta, True) #maka akan mencari atau mengevaluasi minimax untuk mecari kemungkinan terbaik
                board[i] = EMPTY #pada papan game yang terdapat simbol "-" 
                min_eval = min(min_eval, eval_score) #nilai min_eval akan mencari nilai min terendah
                beta = min(beta, eval_score)
                if beta <= alpha:  #akan memastikan jika beta <= alpha
                    break #maka akan menghentikan fungsi minimax
        return min_eval #maka akan mengembalikan nilai min_eval

# Fungsi untuk Menentukan Langka Terbaik dengan Menggunakan Minimax dan Alpha-Beta Pruning
def find_best_move(board): #untuk menjalankan fungsi pengambilakn keputusan terbaik
    best_score = -math.inf #nilai terbaik adalah -infiniti
    best_move = None #langkah terbaik adalah None

    for i in range(9): 
        if board[i] == EMPTY: #jika pada papan game terdapat simbol "-" yang melambangkan EMPTY
            board[i] = PLAYER_X #atau terdapat simbol X pada papan game
            move_score = minimax(board, 9, -math.inf, math.inf, False) #maka akan mencari atau mengevaluasi minimax untuk mecari kemungkin
            board[i] = EMPTY #pada papan game yang terdapat simbol "-"

            if move_score > best_score: #jika nilai langkah > nilai terbaik
                best_score = move_score # maka nilai terbaik = nilai langkah
                best_move = i #maka kemungkinan pada langkah terbaik akan digantikan dengan evaluasi tersebuh

    return best_move #maka akan mengembalikan nilai langkah terbaik

# Perulangan dalam Game
while True:
    print_board(board) #menampilkan papan game
    winner = check_winner(board) #mengecek pemenang

    if winner is not None: #Jika tidak terdapat pemenang
        if winner == "tie": #Jika ada seri
            print("It's a tie!") #perintah untuk print "It's a tie!"
        else:
            print("Player", winner, "wins!") #perintah untuk print "Player X wins!" atau "Player O wins" 
        break

    if len([cell for cell in board if cell != EMPTY]) % 2 == 0: #perintah untuk menyatakan siapa yang bermain duluan, jika user maka 0 dan jika komputer maka 1
        # Giliran Player O's 
        while True:
            move = int(input("Enter 0's move (0-8): ")) #untuk menginput nomor pada kolom papan game dari 0 sampai 8
            if board[move] == EMPTY: #kondisi awal papan sebelum di pilih "-"
                board[move] = PLAYER_O #untuk memprint O pada kolom yang telah di pilih user.
                break
            else:
                print("Invalid move! Try again.")#ketika salah memasukkan nomor pada kolom papan game
    else:
        # Giliran Player X's
        move = find_best_move(board)#untuk menjalankan perintah minimax dan apla-beta pruning
        board[move] = PLAYER_X #untuk memprint X pada kolom yang telah di pilih komputer.