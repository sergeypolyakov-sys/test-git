#!/usr/bin/env python3
"""
tic_tac_toe.py

Простой CLI-игра "Крестики-нолики" для двух игроков (Python 3).

Теперь с возможностью передавать заранее подготовленные ходы через список и безопасным обходом input() для сред без интерактивного ввода.
"""

from typing import List, Optional, Iterator


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
    wins = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]
    for a, bidx, c in wins:
        if b[a] != ' ' and b[a] == b[bidx] == b[c]:
            return b[a]
    return None


def is_draw(b: List[str]) -> bool:
    return all(cell != ' ' for cell in b)


def input_move(player: str, board: List[str], moves_iter: Optional[Iterator[int]] = None) -> int:
    """Получаем ход игрока из итератора или, если невозможно input(), автоматически выбираем первую пустую клетку"""
    while True:
        try:
            if moves_iter is not None:
                idx = next(moves_iter)
                if board[idx] != ' ':
                    continue
                print(f"Игрок {player} выбрал клетку {idx+1} (предзаданный ход)")
                return idx
            else:
                try:
                    raw = input(f"Игрок {player}, выбери клетку (1-9): ")
                    pos = int(raw.strip())
                except (OSError, EOFError):
                    # input недоступен, выбираем первую свободную клетку
                    idx = next(i for i, cell in enumerate(board) if cell == ' ')
                    print(f"Игрок {player} выбрал клетку {idx+1} (авто-выбор)")
                    return idx
                if pos < 1 or pos > 9:
                    print("Введите число от 1 до 9.")
                    continue
                idx = pos - 1
                if board[idx] != ' ':
                    print("Клетка занята, выбери другую.")
                    continue
                return idx
        except StopIteration:
            raise RuntimeError("Предзаданные ходы закончились")
        except ValueError:
            print("Неверный ввод. Введите число от 1 до 9.")


def main(predefined_moves: Optional[List[int]] = None) -> None:
    moves_iter = iter(predefined_moves) if predefined_moves is not None else None
    print("Крестики-нолики — игра для двух игроков")
    while True:
        board = [' '] * 9
        current = 'X'
        winner = None

        print("Позиции клеток:")
        print(" 1 | 2 | 3\n---+---+---\n 4 | 5 | 6\n---+---+---\n 7 | 8 | 9\n")

        while True:
            print_board(board)
            idx = input_move(current, board, moves_iter)
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

        if moves_iter is not None:
            break

        try:
            again = input("Сыграть ещё? (y/n): ").strip().lower()
        except (OSError, EOFError):
            print("Автоматический выход из игры")
            break
        if again != 'y':
            print("До новых встреч!")
            break


if __name__ == '__main__':
    try:
        # main([0, 1, 4, 2, 8])  # пример для теста
        main()
    except (KeyboardInterrupt, EOFError):
        print('\nВыход. Пока!')
