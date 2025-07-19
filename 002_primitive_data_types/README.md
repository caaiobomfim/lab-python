# 🧠 Data Types and String Methods in Python

---

## 🔥 Descrição

Este exercício explora diferentes **tipos primitivos** da linguagem Python — `str`, `int`, `float` e `bool` — por meio de entradas do usuário e uso da função `print()`. Também demonstra o uso de **métodos de string** nativos, como `isnumeric()`, `isalpha()`, `isalnum()` e `isupper()`.

Além disso, utiliza `format()` como uma das formas de formatar a saída no terminal.

## 📌 Objetivo

Criar um programa que:

1. Solicite duas strings e exiba a concatenação;
2. Solicite dois números inteiros e exiba a soma formatada;
3. Solicite dois números com ponto flutuante e exiba a soma formatada;
4. Solicite um valor booleano e exiba o tipo;
5. Aplique métodos de verificação (`isnumeric`, `isalpha`, etc.) em uma string informada pelo usuário.

## 🧪 Como executar

```bash
python main.py
```

## 🚀 Resultado

```bash
Enter the first string: Hello
Enter the second string: World
Concatenated string: HelloWorld
Type: <class 'str'>

Enter the first number: 10
Enter the second number: 5
Result(int): 15
Result(int): 15
The sum of 10 and 5 is 15
Type: <class 'int'>

Enter the first number: 2.5
Enter the second number: 1.5
Result(float): 4.0
Result(float): 4.0
The sum of 2.5 and 1.5 is 4.0
Type: <class 'float'>

Enter the boolean: True
Result(boolean): True
Type: <class 'bool'>

Enter any text: Python3
False
True
True
False
```

## 📘 Conceitos abordados
- Tipos primitivos: str, int, float, bool.
- Conversão de tipos (int(), float(), bool(), str()).
- Concatenação de strings.
- Formatação de saída com format().
- Métodos de string: isnumeric(), isalpha(), isalnum(), isupper().
- Leitura de entrada com input().
- Uso da função type() para identificar tipos.