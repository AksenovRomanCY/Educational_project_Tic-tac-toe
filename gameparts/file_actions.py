
def save_result(winner: str = None) -> None:
    with open('results.txt', 'w', encoding='utf-8') as f:
        if winner:
            f.write(f'Победили {winner}.')
        else:
            f.write('Ничья!')