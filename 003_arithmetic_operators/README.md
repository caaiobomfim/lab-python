# ➕ Arithmetic Operators and String Formatting in Python

---

## 🔥 Descrição

Este programa demonstra o uso dos **principais operadores aritméticos em Python**, além do **operador de igualdade** e técnicas de **formatação de strings com alinhamento**.

Através de exemplos simples, o código realiza operações com duas variáveis (`a = 10` e `b = 3`), imprime os resultados no terminal com mensagens explicativas, e exibe diferentes estilos de formatação usando o método `format()`.

Também é apresentado o operador `==`, utilizado para comparação de igualdade entre valores.

Além disso, vale destacar que:
- Python segue uma **ordem de precedência** dos operadores matemáticos (similar à matemática tradicional).
- O limite para tipos como `int` ou `float` não é fixo como em outras linguagens, pois o Python lida com **valores inteiros arbitrariamente grandes** — **o limite é a memória disponível da máquina.**

## 📌 Objetivo

Criar um programa que:
1. Utilize os operadores aritméticos: `+`, `-`, `*`, `/`, `//`, `%`, `**`;
2. Compare valores com o operador de igualdade `==`;
3. Aplique formatação de strings com alinhamento à esquerda, direita e centralizado.

## 🧮 Operadores utilizados

| Operador  | Nome (inglês)     | Descrição                                 |
|-----------|-------------------|-------------------------------------------|
| `+`       | Addition          | Soma dois valores                         |
| `-`       | Subtraction       | Subtrai um valor do outro                 |
| `*`       | Multiplication    | Multiplica dois valores                   |
| `/`       | Division          | Retorna a divisão com casas decimais      |
| `//`      | Floor Division    | Retorna apenas a parte inteira da divisão |
| `%`       | Modulus           | Retorna o resto da divisão                |
| `**`      | Exponentiation    | Potenciação (ex: 2 elevado a 3)           |
| `==`      | Equality Operator | Compara se dois valores são iguais        |

## 🧭 Ordem de precedência (do maior para o menor)

1. `()` – Parênteses
2. `**` – Exponenciação
3. `*`, `/`, `//`, `%` – Multiplicação e divisões
4. `+`, `-` – Soma e subtração
5. `==`, `!=`, `<`, `>`, `<=`, `>=` – Comparações

> ⚠️ Python executa expressões respeitando essa ordem, como em: `2 + 3 * 4` → resultado será `14`, e **não** `20`.

## 🧪 Como executar

```bash
python main.py
```

## 🚀 Resultado

```bash
Addition: 13
Subtraction: 7
Multiplication: 30
Division: 3.33
Floor Division: 3
Modulus: 1
Exponentiation: 1000
Equality operator: False
=====

Your name is CAIO                !
Your name is                CAIO!
Your name is         CAIO         !
Your name is ========CAIO========!
```

## 🧠 Observação sobre tipos em Python
Tipos como `int` e `float` não possuem um limite fixo como em linguagens como C ou Java.

Python é capaz de trabalhar com números inteiros extremamente grandes, limitado apenas pela quantidade de memória disponível na máquina onde está sendo executado.