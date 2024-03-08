print("Exemplo de captura de exceções")

try:
    # Solicita ao usuário um número inteiro
    number = int(input("Digite um número inteiro: "))

    # Realiza uma operação matemática
    result = 10 / number

# Captura um erro caso o valor inserido não seja um número inteiro
except ValueError as e:
    # Exibe uma mensagem de erro específica para o tipo de exceção
    print(f"Erro de valor: {e}")

    # Lança uma exceção personalizada informando que os tipos de variáveis são incompatíveis
    raise ValueError("Tipo de variáveis incompatíveis")

# Captura qualquer outra exceção não prevista
except Exception as e:
    # Exibe uma mensagem de erro genérica
    print(f"Erro: {e}")

# Executado caso nenhuma exceção seja lançada
else:
    # Exibe o resultado da operação matemática
    print(f"Resultado: {result}")

# Executado independentemente de ter ocorrido uma exceção ou não
finally:
    # Exibe uma mensagem indicando que a operação foi finalizada
    print("Operação finalizada")
