# 🌡️ Temperature Converter in Python

---

## 🔥 Descrição

Este programa converte uma temperatura informada em **graus Celsius (°C)** para:

- **Fahrenheit (°F)**
- **Kelvin (K)**

Utiliza fórmulas matemáticas padrão, entrada de dados com `input()` e formatação com `f-strings` para exibir as temperaturas com duas casas decimais.

## 📌 Objetivo

Criar um programa que:
1. Solicite uma temperatura em Celsius (°C);
2. Converta para Fahrenheit e Kelvin;
3. Exiba os resultados formatados.

## 🧪 Como executar

```bash
python main.py
```

## 🚀 Resultado

```bash
Enter the temperature in Celsius (°C): 25

Temperature in Celsius: 25.00°C
In Fahrenheit: 77.00°F
In Kelvin: 298.15K
```

## 📘 Conceitos abordados
- Entrada com `input()` e conversão para `float()`
- Cálculo com fórmulas matemáticas:
  - Fahrenheit = `(°C × 9/5) + 32`
  - Kelvin = `°C + 273.15`
- Formatação com `f-strings` (`:.2f`) para saída legível

> 💡 Esse programa pode ser expandido para aceitar qualquer unidade de entrada e converter para as demais com menus interativos.