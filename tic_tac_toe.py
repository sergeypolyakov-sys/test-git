from typing import List, Optional




def print_board(b: List[str]) -> None:
"""Печать доски в консоль"""
print()
print(f" {b[0]} | {b[1]} | {b[2]} ")
print("---+---+---")
print(f" {b[3]} | {b[4]} | {b[5]} ")
print("---+---+---")
print(f" {b[6]} | {b[7]} | {b[8]} ")
print()




def check_win(b: List[str]) -> Optional[str]:
"""Возвращает 'X' или 'O' если кто-то выиграл, иначе None"""
wins = [
(0, 1, 2), (3, 4, 5), (6, 7, 8), # строки
(0, 3, 6), (1, 4, 7), (2, 5, 8), # столбцы
(0, 4, 8), (2, 4, 6) # диагонали
]
for a, bidx, c in wins:
if b[a] != ' ' and b[a] == b[bidx] == b[c]:
return b[a]
return None




def is_draw(b: List[str]) -> bool:
return all(cell != ' ' for cell in b)




def input_move(player: str, board: List[str]) -> int:
"""Просим у игрока номер клетки 1..9. Возвращаем индекс 0..8"""
while True:
try:
raw = input(f"Игрок {player}, выбери клетку (1-9): ")
pos = int(raw.strip())
if pos < 1 or pos > 9:
print("Введите число от 1 до 9.")
continue
idx = pos - 1
if board[idx] != ' ':
print("Клетка занята, выбери другую.")
continue
return idx
except ValueError:
print("Неверный ввод. Введите число от 1 до 9.")




def main() -> None:
print("Крестики-нолики — игра для двух игроков")
while True:
board = [' '] * 9
current = 'X'
winner = None


print("Позиции клеток:")
print(" 1 | 2 | 3\n---+---+---\n 4 | 5 | 6\n---+---+---\n 7 | 8 | 9\n")


while True:
print_board(board)
idx = input_move(current, board)
board[idx] = current


winner = check_win(board)
if winner:
print_board(board)
print(f"Победил {winner}!")
break
if is_draw(board):
print_board(board)
print("Ничья!")
break


current = 'O' if current == 'X' else 'X'


again = input("Сыграть ещё? (y/n): ").strip().lower()
if again != 'y':
print("До новых встреч!")
break




if __name__ == '__main__':
try:
main()
except (KeyboardInterrupt, EOFError):
print('\nВыход. Пока!')
