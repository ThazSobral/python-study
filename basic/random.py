# random é uma biblioteca muito útil para randomizar valores, seja para utiliza-los de forma sequencial ou randômico mesmo
import random

text = 'ana paula luiza fabio'.split()

print(text)

# podemos escolher de forma aleatória uma posição na lista
choice = random.choice(text)
print(choice)

# podemos misturar de forma aleatória os valores dentro da lista
random.shuffle(text)
print(text)

# podemos também gerar uma amostra com SAMPLE
sample = random.sample(range(100), 10)
print(sample)
