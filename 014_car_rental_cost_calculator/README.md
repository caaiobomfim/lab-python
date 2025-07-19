# 🚗 Car Rental Cost Calculator in Python

---

## 🔥 Descrição

Este programa calcula o valor total a ser pago pelo aluguel de um carro, com base em:

- A quantidade de **dias de aluguel**
- A distância total percorrida em **quilômetros**

A fórmula usada é:

total = (dias × R$60.00) + (km × R$0.15)

## 📌 Objetivo

Criar um programa que:
1. Solicite a quantidade de dias que o carro foi alugado;
2. Solicite a quantidade de quilômetros rodados;
3. Calcule o valor total a pagar com base nas tarifas definidas;
4. Exiba o resultado formatado com duas casas decimais.

## 🧪 Como executar

```bash
python main.py
```

## 🚀 Resultado

```bash
How many days was the car rented? 3
How many kilometers did the car travel? 240.5

Rental duration: 3 day(s)
Distance traveled: 240.5 km
Total amount to pay: R$192.08
```

## 📘 Conceitos abordados
- Entrada de dados com `input()`
- Conversão para `int` e `float`
- Multiplicações e soma de valores monetários
- Formatação de saída com `f-string` (`:.2f`)

> 💡 Este programa pode ser expandido para considerar tipos de veículos, seguros adicionais ou tarifas variáveis.