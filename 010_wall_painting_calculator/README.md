# 🎨 Wall Paint Calculator in Python

---

## 🔥 Descrição

Este programa calcula a quantidade de **tinta necessária** para pintar uma parede, a partir das dimensões informadas pelo usuário (altura e largura).

É considerado que **1 litro de tinta cobre 2 metros quadrados**. O programa utiliza operações de multiplicação e divisão, além de `f-strings` para exibir os valores com duas casas decimais.

## 📌 Objetivo

Criar um programa que:
1. Solicite a **altura** e a **largura** da parede (em metros);
2. Calcule a **área total**;
3. Informe a **quantidade de litros de tinta necessária**, considerando a cobertura de 2 m² por litro.

## 🧪 Como executar

```bash
python main.py
```

## 🚀 Resultado

```bash
Enter the height of the wall (in meters): 2.5
Enter the width of the wall (in meters): 4.0

Wall dimensions: 2.50m x 4.00m
Total area: 10.00 square meters
Paint required: 5.00 liters
```

## 📘 Conceitos abordados
- Entrada de dados com `input()`
- Conversão para `float()`
- Cálculo de área (`altura * largura`)
- Regra de três para consumo de tinta
- Formatação com `f-string` (`:.2f`)

> 💡 O programa pode ser adaptado para considerar janelas/portas ou diferentes rendimentos de tinta.