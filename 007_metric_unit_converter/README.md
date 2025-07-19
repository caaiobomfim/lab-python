# 📏 Metric Unit Converter in Python

---

## 🔥 Descrição

Este programa realiza a conversão de uma medida informada em **metros** para outras unidades do **sistema métrico decimal**:

- milímetros (mm)
- centímetros (cm)
- decímetros (dm)
- decâmetros (dam)
- hectômetros (hm)
- quilômetros (km)

Ele utiliza operadores aritméticos simples (`*` e `/`) e formatação de string para exibir os valores com a precisão apropriada.

## 📌 Objetivo

Criar um programa que:
1. Solicite um valor em metros ao usuário;
2. Converta esse valor para outras medidas métricas;
3. Exiba os resultados de forma organizada e legível.

## 🧪 Como executar

```bash
python main.py
```

## 🚀 Resultado

```bash
Enter a value in meters: 1.75
1.75 meters is equivalent to:
- 1750 millimeters (mm)
- 175 centimeters (cm)
- 17 decimeters (dm)
- 0.18 decameters (dam)
- 0.02 hectometers (hm)
- 0.002 kilometers (km)
```

## 📘 Conceitos abordados
- Conversão de medidas com operadores `*` e `/`
- Entrada de dados com `input()`
- Uso de `float()` para lidar com números decimais
- Formatação de saída com `f-strings` e precisão decimal

> 💡 A conversão entre unidades métricas é baseada em múltiplos de 10, o que facilita os cálculos com operações básicas.