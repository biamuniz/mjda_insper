# -*- coding: utf-8 -*-
"""Atividade2_PensamentoComputacional.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1kdK99HKQKpc8bWkaXpSRF5Midswz8w6g
"""

#Definindo perguntas e alternativas
instrucao = print("Responda com a alternativa que melhor se encaixa na sua rotina")
pergunta1 = print("1) Você dorme: \na) Sempre no mesmo horário\nb) Sempre no mesmo horário, exceto fim de semana\nc) Cada dia da semana em um horário\nd) Não tenho horário fixo para dormir")
r1 = input("Sua resposta: "\n)
pergunta2 = print("2) Durante a noite, seu celular fica: \na) Em outro cômodo\nb) No quarto, mas longe da cama\nc) No quarto, mas na mesa de cabeceira\nd) Do meu lado, na cama")
r2 = input("Sua resposta: ")
pergunta_3 = print("3) Quantas horas você tem para dormir diariamente?\na) 7 a 9 horas\nb) 6 horas\nc) 5 horas\nd) Menos de 5 horas")
r3 = input("Sua resposta: ")
pergunta_4 = print("4) Você usa telas até quanto tempo antes de dormir?\na) 2 horas\nb) 1 hora\nc) Até a hora de dormir\nd) Adormeço assistindo a telas")
r4 = input("Sua resposta: ")
pergunta_5 = print("Você faz exercícios\na) Pela manhã\nb) Pela tarde\nc) Pela noite\nd) Não faço exercícios diariamente")
r5 = input("Sua resposta: ")

#Atribuindo valores para cada alternativa
if r1 == "a":
  pontor1 = 15
elif r1 == "b": 
  pontor1 = 10
elif r1 == "c":
  pontor1 = 5
else:
  pontor1 = 0

if r2 == "a":
  pontor2 = 15
elif r2 == "b": 
  pontor2 = 10
elif r2 == "c":
  pontor2 = 5
else:
  pontor2 = 0

if r3 == "a":
  pontor3 = 15
elif r3 == "b": 
  pontor3 = 10
elif r3 == "c":
  pontor3 = 5
else:
  pontor3 = 0

if r4 == "a":
  pontor4 = 15
elif r4 == "b": 
  pontor4 = 10
elif r4 == "c":
  pontor4 = 5
else:
  pontor4 = 0

if r5 == "a":
  pontor5 = 15
elif r5 == "b": 
  pontor5 = 10
elif r5 == "c":
  pontor5 = 5
else:
  pontor5 = 0

#Cálculo do resultado
resultado = int(pontor1) + int(pontor2) + int(pontor3) + int(pontor4) + int(pontor5)

#Definição do resultado
if resultado > 60:
  print("Parabéns, você está fazendo uma higiene do seu sono correta")
elif resultado > 41:
  print("Você poderia melhorar algumas coisas na sua noite")
elif resultado > 21:
  print("Que tal pensar melhor nas suas noites de sono?")
elif resultado < 20:
  print("Dê valor ao seu sono!")