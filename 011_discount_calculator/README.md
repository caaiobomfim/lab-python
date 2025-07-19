# 💸 Product Discount Calculator in Python

---

## 🔥 Descrição

Este programa calcula o valor final de um produto após aplicar um **desconto percentual** informado pelo usuário. Ele realiza o cálculo do valor do desconto em reais e exibe tanto o valor original quanto o valor com desconto.

Utiliza operações básicas com porcentagem, entrada de dados com `input()` e saída formatada com `f-strings`.

## 📌 Objetivo

Criar um programa que:
1. Solicite o valor original de um produto;
2. Solicite o percentual de desconto (%);
3. Calcule o valor do desconto em reais;
4. Exiba o valor final após aplicar o desconto.

## 🧪 Como executar

```bash
python main.py
```

## 🚀 Resultado

```bash
Enter the product price (R$): 120
Enter the discount percentage (%): 15

Original price: R$120.00
Discount: 15.0% (R$18.00)
Final price after discount: R$102.00
```

## 📘 Conceitos abordados
- Entrada de dados com `input()`
- Conversão de tipos com `float()`
- Cálculo de porcentagem (`(porcentagem / 100) * valor`)
- Subtração para aplicar o desconto
- Formatação com `f-strings` para exibição monetária (`:.2f`)

> 💡 Pode ser adaptado para promoções progressivas, cupons ou simulação de parcelamento com/sem juros.