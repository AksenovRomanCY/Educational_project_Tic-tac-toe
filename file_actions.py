
def save_result(winner: str = None) -> None:
    file = open('results.txt', 'w', encoding='utf-8')
    if winner:
        file.write(f'Победили {winner}.')
    else:
        file.write('Ничья!')
    file.close()
