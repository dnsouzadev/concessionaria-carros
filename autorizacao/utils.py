def formatar_preco(preco):
    if preco >= 1000000:
        return f'R$ {preco / 1000000:.1f} milhão'
    elif preco >= 1000:
        return f'R$ {preco / 1000:.1f} mil'
    else:
        return f'R$ {preco:.2f}'
