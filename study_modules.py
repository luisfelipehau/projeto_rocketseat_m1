# Importa módulos padrão
from math import sqrt

# Importa funções personalizadas do módulo meu_modulo
from functions.study_operations import greeting, double

# Exibe um exemplo de utilização de um módulo personalizado
print("\nExemplo de criação e utilização de um módulo personalizado")

# Exemplo de utilização de funções personalizadas
greeting_message = greeting("Luis")
double_result = double(5)

# Exibe os resultados das funções personalizadas
print(greeting_message)
print(f"O dobro de 5 é {double_result}")

# Exibe um exemplo de utilização de um módulo padrão
print("\nExemplo de importação de um módulo padrão:")
square_root = sqrt(25)
print(f"A raiz quadrada de 25 é {square_root}")
