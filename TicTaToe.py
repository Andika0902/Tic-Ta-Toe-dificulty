ascii = '''
........................................................
..._______._........_______..........._______...........
..|__   __(_)......|__   __|.........|__   __|..........
.....| |..._..___.....| |.__._..___.....| |.___...___...
.....| |..| |/ __|....| |/ _  |/ __|....| |/ _ \./ _ \..
.....| |..| | (__.....| | (_| | (__.....| | (_) |  __/..
.....|_|..|_|\___|__..|_|\__,_|\___|....|_|\___/.\___|..
..............__..__...___...__..__...___...............
..............\ \/ /../ _ \..\ \/ /../ _ \..............
...............>  <..| (_) |..>  <..| (_) |.............
............../_/\_\..\___/../_/\_\..\___/..............
........................................................
'''
print(ascii)


pilihan = 'y'
while(pilihan !='n'):
    print("""Select: 
      
        Start         Exit""")
    select = input("\nMasukan Pilihan : ")
    if select=="Start" or select=="start":
        mode = input("\nPilih Mode[player/bot]: ") #Memilih mode permainan
        if mode=="player":
            board = {1: ' ', 2: ' ', 3: ' ',
                4: ' ', 5: ' ', 6: ' ',         # Ukuran Board
                7: ' ', 8: ' ', 9: ' '}
            # X dan O
            player1 = 'O'
            player2 = 'X'

            def printBoard(board): # Print Board
                print(board[1] + ' | ' + board[2] + ' | ' + board[3])
                print('--+---+--')
                print(board[4] + ' | ' + board[5] + ' | ' + board[6])
                print('--+---+--')
                print(board[7] + ' | ' + board[8] + ' | ' + board[9])
                print("\n")


            def spaceIsFree(position): 
                if board[position] == ' ':
                    return True
                else:
                    return False

            # Cek Apakah Menang Atau Seri
            def insertLetter(letter, position):
                if spaceIsFree(position):
                    board[position] = letter
                    printBoard(board)
                    if (checkDraw()): 
                        print("Draw!")
                        
                    if checkForWin():
                        if letter == 'X':
                            print("Player2 wins!")
                            
                        else:
                            print("Player1 wins!") 
                            

                    return


                else:
                    print("Can't insert there!") # Jika input Posisi Sama/Salah
                    position = int(input("Please enter new position:  "))
                    insertLetter(letter, position)
                    return


            def checkForWin(): # Mengecek Posisi X dan O untuk menentukan Kemenangan
                if (board[1] == board[2] and board[1] == board[3] and board[1] != ' '):
                    return True
                elif (board[4] == board[5] and board[4] == board[6] and board[4] != ' '):
                    return True
                elif (board[7] == board[8] and board[7] == board[9] and board[7] != ' '):
                    return True
                elif (board[1] == board[4] and board[1] == board[7] and board[1] != ' '):
                    return True
                elif (board[2] == board[5] and board[2] == board[8] and board[2] != ' '):
                    return True
                elif (board[3] == board[6] and board[3] == board[9] and board[3] != ' '):
                    return True
                elif (board[1] == board[5] and board[1] == board[9] and board[1] != ' '):
                    return True
                elif (board[7] == board[5] and board[7] == board[3] and board[7] != ' '):
                    return True
                else:
                    return False


            def checkDraw(): # Mengecek Jika Seri
                for key in board.keys():
                    if (board[key] == ' '):
                        return False
                return True


            def playerMove(): # Turn Player 1
                position = int(input("Enter the position for 'O':  "))
                insertLetter(player1, position)
                return


            def compMove(): # Turn Player 2
                position = int(input("Enter the position for 'X':  "))
                insertLetter(player2, position)
                return

            printBoard(board) # Memanggil Board

            while not checkForWin():
                compMove()
                if checkForWin():
                    pilihan=input("Apakah anda ingin mengulang kembali (y/n)?")
                    break
                playerMove()
                if checkForWin():
                    pilihan=input("Apakah anda ingin mengulang kembali (y/n)?")
                    break
        elif mode=="bot": # Mode Bot
            kesulitan = input("Pilih Tingkat kesulitan[easy/hard]: ") # Memilih Tingkat kesulitan 
            if kesulitan=="easy":
                import random

                def cetak_papan(papan):
                    print(f"\n{papan[0]} | {papan[1]} | {papan[2]}")
                    print("--|---|--")
                    print(f"{papan[3]} | {papan[4]} | {papan[5]}")
                    print("--|---|--")
                    print(f"{papan[6]} | {papan[7]} | {papan[8]}")

                def cek_pemenang(papan):
                    aturan_pemenang = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                                    (0, 3, 6), (1, 4, 7), (2, 5, 8),
                                    (0, 4, 8), (2, 4, 6)]

                    for aturan in aturan_pemenang:
                        if papan[aturan[0]] == papan[aturan[1]] == papan[aturan[2]] and papan[aturan[0]] != ' ':
                            return papan[aturan[0]]

                    return None

                def permainan_berakhir(papan):
                    return ' ' not in papan or cek_pemenang(papan) is not None

                def main():
                    papan = [' '] * 9
                    simbol_pemain = 'X'
                    simbol_bot = 'O'

                    while not permainan_berakhir(papan):
                        cetak_papan(papan)

                        if simbol_pemain == 'X':
                            langkah = int(input("Pilih langkah (1-9): ")) - 1

                            if papan[langkah] == ' ':
                                papan[langkah] = simbol_pemain
                            else:
                                print("Langkah tidak valid. Coba lagi.")
                                continue
                        else:
                            # Bot's turn
                            langkah_bot = random.randint(0, 8)

                            while papan[langkah_bot] != ' ':
                                langkah_bot = random.randint(0, 8)

                            papan[langkah_bot] = simbol_bot

                        pemenang = cek_pemenang(papan)
                        if pemenang:
                            cetak_papan(papan)
                            print(f"Permainan berakhir. {pemenang} menang!")
                            break

                        simbol_pemain = 'O' if simbol_pemain == 'X' else 'X'

                    if not pemenang:
                        cetak_papan(papan)
                        print("Permainan berakhir. Seri!")

                if __name__ == "__main__":
                    main()
                    pilihan=input("Apakah anda ingin mengulang kembali (y/n)?")

            elif kesulitan=="hard":
                board = {1: ' ', 2: ' ', 3: ' ',
                4: ' ', 5: ' ', 6: ' ',             # Jarak Board
                7: ' ', 8: ' ', 9: ' '}
                player = 'O'
                computer = 'X'

                # Game Board
                def printBoard(board):
                    print(board[1] + " | " + board[2] + " | " + board[3])
                    print("--+---+--")
                    print(board[4] + " | " + board[5] + " | " + board[6])
                    print("--+---+--")
                    print(board[7] + " | " + board[8] + " | " + board[9])
                    print("\n")

                def spaceIsFree(position):
                    if board[position] == ' ':
                        return True 
                    return False 

                # Cek apakah Menang, Kalah atau seri
                def insertLetter(letter, position):
                    if spaceIsFree(position):
                        board[position] = letter 
                        printBoard(board)
                        if checkDraw():
                            print("Draw!")

                        if checkWin():
                            if letter == 'X':
                                print("Bot wins!")
                                
                            else:
                                print("Player wins!")
                                
                        return 
                    else:
                        print("Invalid position")
                        position = int(input("Please enter a new position: "))
                        insertLetter(letter, position)
                        return   

                def checkWin():
                    if (board[1] == board[2] and board[1] == board[3] and board[1] != ' '):
                        return True
                    elif (board[4] == board[5] and board[4] == board[6] and board[4] != ' '):
                        return True
                    elif (board[7] == board[8] and board[7] == board[9] and board[7] != ' '):
                        return True
                    elif (board[1] == board[4] and board[1] == board[7] and board[1] != ' '):
                        return True
                    elif (board[2] == board[5] and board[2] == board[8] and board[2] != ' '):
                        return True
                    elif (board[3] == board[6] and board[3] == board[9] and board[3] != ' '):
                        return True
                    elif (board[1] == board[5] and board[1] == board[9] and board[1] != ' '):
                        return True
                    elif (board[7] == board[5] and board[7] == board[3] and board[7] != ' '):
                        return True
                    else:
                        return False

                def checkWhichMarkWon(mark):
                    if (board[1] == board[2] and board[1] == board[3] and board[1] == mark):
                        return True
                    elif (board[4] == board[5] and board[4] == board[6] and board[4] == mark):
                        return True
                    elif (board[7] == board[8] and board[7] == board[9] and board[7] == mark):
                        return True
                    elif (board[1] == board[4] and board[1] == board[7] and board[1] == mark):
                        return True
                    elif (board[2] == board[5] and board[2] == board[8] and board[2] == mark):
                        return True
                    elif (board[3] == board[6] and board[3] == board[9] and board[3] == mark):
                        return True
                    elif (board[1] == board[5] and board[1] == board[9] and board[1] == mark):
                        return True
                    elif (board[7] == board[5] and board[7] == board[3] and board[7] == mark):
                        return True
                    else:
                        return False

                def checkDraw():
                    for key in board.keys():
                        if board[key] == ' ':
                            return False 
                    return True 

                # Turn Player
                def playerMove():
                    position = int(input("Enter a position for 'O': "))
                    insertLetter(player, position)
                    return 

                # Turn Bot
                def compMove():
                    bestScore = -800
                    bestMove = 0
                    for key in board.keys():
                        if board[key] == ' ':
                            board[key] = computer
                            score = minimax(board, False)
                            board[key] = ' '
                            if score > bestScore:
                                bestScore = score 
                                bestMove = key
                    insertLetter(computer, bestMove)
                    return
                def minimax(board, isMaximizing):
                    if checkWhichMarkWon(computer):
                        return 1 
                    elif checkWhichMarkWon(player):
                        return -1 
                    elif checkDraw():
                        return 0
                        
                    if isMaximizing:
                        bestScore = -800 
                        for key in board.keys():
                            if board[key] == ' ':
                                board[key] = computer 
                                score = minimax(board, False)
                                board[key] = ' '
                                if score > bestScore:
                                    bestScore = score
                        return bestScore 
                    else:
                        bestScore = 800 
                        for key in board.keys():
                            if board[key] == ' ':
                                board[key] = player 
                                score = minimax(board, True)
                                board[key] = ' '
                                if score < bestScore:
                                    bestScore = score 
                        return bestScore


                while not checkWin():
                    compMove()
                    if checkWin():
                        pilihan=input("Apakah anda ingin mengulang kembali (y/n)?")
                        break
                    elif checkDraw():
                        pilihan=input("Apakah anda ingin mengulang kembali (y/n)?")
                        break
                    playerMove()
                    if checkWin():
                        pilihan=input("Apakah anda ingin mengulang kembali (y/n)?")
                        break
                    elif checkDraw():
                        pilihan=input("Apakah anda ingin mengulang kembali (y/n)?")
                        break
            else:
                print("Tingkat kesulitan tidak diketahui")
        else:
            print("Mode tidak diketahui")
    elif select=='Exit' or select=='exit':
        exit()
    else:
        print("Pilihan Tidak Diketahui")
        pilihan=input("Apakah anda ingin mengulang kembali (y/n)?")


"""Berikut adalah penjelasan fungsi-fungsi pada kode Python yang diberikan:

1.  `printBoard(board)`: Mencetak papan permainan tic-tac-toe dengan posisi yang diberikan.

2.  `spaceIsFree(position)`: Memeriksa apakah suatu posisi di papan masih kosong atau sudah diisi.

3.  `insertLetter(letter, position)`: Memasukkan huruf (X atau O) ke dalam posisi tertentu 
    di papan permainan dan memanggil fungsi `printBoard()`.

4.  `checkForWin()`: Mengecek apakah ada pemain yang menang berdasarkan kondisi pada papan permainan.

5.  `checkDraw()`: Mengecek apakah permainan berakhir dengan seri.

6.  `playerMove()`: Mengambil input dari pemain untuk langkah berikutnya.

7.  `compMove()`: Mengambil langkah berikutnya untuk komputer dalam permainan dengan pemain atau bot.

8.  `cetak_papan(papan)`: Mencetak papan permainan untuk mode bot (easy).

9.  `cek_pemenang(papan)`: Mengecek apakah ada pemenang pada papan permainan untuk mode bot (easy).

10.  `permainan_berakhir(papan)`: Mengecek apakah permainan telah berakhir (seri atau ada pemenang) untuk mode bot (easy).

11.  `main()`: Menjalankan permainan mode bot (easy).

12.  `minimax(board, isMaximizing)`: Fungsi algoritma minimax untuk menentukan langkah terbaik bagi komputer pada mode bot (hard).

13.  `checkWhichMarkWon(mark)`: Mengecek apakah suatu mark (X atau O) menang pada mode bot (hard).

14.  `printBoard(board)`: Mencetak papan permainan untuk mode bot (hard).

15.  `spaceIsFree(position)`: Memeriksa apakah suatu posisi di papan permainan (mode bot - hard) masih kosong atau sudah diisi.

16.  `insertLetter(letter, position)`: Memasukkan huruf (X atau O) ke dalam posisi tertentu di papan permainan mode bot (hard).

17.  `checkWin()`: Mengecek apakah ada pemain yang menang pada mode bot (hard).

18.  `checkWhichMarkWon(mark)`: Mengecek apakah suatu mark (X atau O) menang pada mode bot (hard).

19.  `checkDraw()`: Mengecek apakah permainan pada mode bot (hard) berakhir dengan seri.

20.  `playerMove()`: Mengambil input dari pemain untuk langkah berikutnya pada mode bot (hard).

21.  `compMove()`: Mengambil langkah berikutnya untuk komputer pada mode bot (hard).

22.  `minimax(board, isMaximizing)`: Fungsi algoritma minimax untuk menentukan langkah terbaik bagi komputer pada mode bot (hard).


Semua fungsi ini berperan dalam menjalankan logika permainan tic-tac-toe baik untuk mode pemain melawan pemain, pemain
melawan bot (easy), atau pemain melawan bot (hard)."""
