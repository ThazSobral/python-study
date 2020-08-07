# O script é destinado a manipular dicionários a partir de um arquivo de texto

# abrimos o arquivo
file = open(r'intermediary\examples\read-surf-score\surf-score.txt')
# e definimos um dicionário
scores = {}
# percorremos todo o arquivo e armazenamos no dicionário
for line in file:
    name, score = line.split(': ')
    scores[name] = float(score)

# percorremos o dicionário e ordenamos pela pontuação e deixamos de forma reversa (do maior para o menor)
for item in sorted(scores, key=scores.get, reverse=True):
    # mostramos as chaves e valores do item
    print(f'{scores[item]} -> {item}')
