"""
06. not_bad

Dada uma string, encontre a primeira aparição das
substrings 'not' e 'bad'. Se 'bad' aparecer depois
de 'not', troque todo o trecho entre 'not' e 'bad'
por 'good' e retorne a string resultante.

Exemplo: 'The dinner is not that bad!' retorna 'The dinner is good!'
"""


def not_bad(s):
    # +++ SUA SOLUÇÃO +++
    notbad = s.replace(s[s.find('not'):s.find('bad') + 3], 'good')
    # if s.find('bad') > s.find('not'):
    #     return notbad
    # else:
    #     return s
    return notbad if s.find('bad') > s.find('not') else s


def not_bad_01(s):
    palavra1 = 0
    palavra2 = 0
    resultado = s
    cont = 0
    if 'not' in s:
        palavra1 = s.index('not')
        if 'bad' in s:
            palavra2 = s.index('bad')
            if palavra2 > palavra1:
                cont = palavra2 + 3
                resultado = s.replace(s[palavra1:cont], 'good')


def not_bad_02(s):
    mensagem = s
    if 'not' in s:
        indice_not = s.index('not')

        if 'bad' in s:
            indice_bad = s.index('bad')

            if indice_bad > indice_not:
                mensagem = s.replace(s[indice_not:indice_bad + 3], 'good')
                

# --- Daqui para baixo são apenas códigos auxiliáries de teste. ---

def test(f, in_, expected):
    """
    Executa a função f com o parâmetro in_ e compara o resultado com expected.
    :return: Exibe uma mensagem indicando se a função f está correta ou não.
    """
    out = f(in_)

    if out == expected:
        sign = '✅'
        info = ''
    else:
        sign = '❌'
        info = f'e o correto é {expected!r}'

    print(f'{sign} {f.__name__}({in_!r}) retornou {out!r} {info}')


if __name__ == '__main__':
    # Testes que verificam o resultado do seu código em alguns cenários.
    test(not_bad, 'This movie is not so bad', 'This movie is good')
    test(not_bad, 'This dinner is not that bad!', 'This dinner is good!')
    test(not_bad, 'This tea is not hot', 'This tea is not hot')
    test(not_bad, "It's bad yet not", "It's bad yet not")
