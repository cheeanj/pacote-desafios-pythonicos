"""
07. front_back

Considere dividir uma string em duas metades.
Caso o comprimento seja par, a metade da frente e de trás tem o mesmo tamanho.
Caso o comprimento seja impar, o caracter extra fica na metade da frente.

Exemplo: 'abcde', a metade da frente é 'abc' e a de trás é 'de'.

Finalmente, dadas duas strings a e b, retorne uma string na forma:
a-frente + b-frente + a-trás + b-trás
"""
import math


def front_back(a, b):
    # +++ SUA SOLUÇÃO +++
    if len(a) % 2 == 0:
        af = a[:len(a) // 2]
        at = a[len(a) // 2:]
    else:
        af = a[:len(a) // 2 + 1]
        at = a[len(a) // 2 + 1:]

    if len(b) % 2 == 0:
        bf = b[:len(b) // 2]
        bt = b[len(b) // 2:]
    else:
        bf = b[:len(b) // 2 + 1]
        bt = b[len(b) // 2 + 1:]

    # return af + bf + at + bt
    return ''.join(af + bf + at + bt)


def front_back_02(a, b):
    return ''.join([a[:(math.ceil(len(a) / 2))], b[:(math.ceil(len(b) / 2))], a[(math.ceil(len(a) / 2)):],
                    b[(math.ceil(len(b) / 2)):]])


# --- Daqui para baixo são apenas códigos auxiliáries de teste. ---

def test(f, in_, expected):
    """
    Executa a função f com o parâmetro in_ e compara o resultado com expected.
    :return: Exibe uma mensagem indicando se a função f está correta ou não.
    """
    out = f(*in_)

    if out == expected:
        sign = '✅'
        info = ''
    else:
        sign = '❌'
        info = f'e o correto é {expected!r}'

    print(f'{sign} {f.__name__}{in_!r} retornou {out!r} {info}')


if __name__ == '__main__':
    # Testes que verificam o resultado do seu código em alguns cenários.
    test(front_back, ('abcd', 'xy'), 'abxcdy')
    test(front_back, ('abcde', 'xyz'), 'abcxydez')
    test(front_back, ('Kitten', 'Donut'), 'KitDontenut')
