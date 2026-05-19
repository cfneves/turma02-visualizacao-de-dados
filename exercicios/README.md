# Exercícios de Python — Turma Visualização de Dados

Materiais práticos do curso, organizados por módulo temático e progressão didática.
Cada pasta representa uma etapa do aprendizado — do mais simples ao mais complexo.

> Estes exercícios acompanham as aulas da **Semana 03**. Consulte os guias em [`aulas/semana_03/`](../aulas/semana_03/) para referência paralela.

---

## Pré-requisitos

- Python 3.8 ou superior instalado
- Editor de código (VS Code recomendado)
- Terminal (PowerShell, CMD ou bash)

Para verificar se o Python está instalado:

```bash
python --version
```

---

## Estrutura dos Modulos

```
exercicios/
├── 01.sintaxe/          → Primeiros passos: print, input e comentários
├── 02.variaveis/        → Tipos de dados e manipulação de variáveis
├── 03.Estruturas/       → Estruturas de controle: condicionais e loops
└── 04. Exercicios/      → Desafios práticos para fixação do conteúdo
```

---

## Modulo 01 — Sintaxe Basica

**Objetivo:** Aprender os comandos essenciais para interagir com o Python.

| Arquivo | Conceito | O que voce vai aprender |
|---------|----------|--------------------------|
| `exe01.py` | `print()` | Exibir textos, números e múltiplos valores na tela |
| `exe02.py` | `input()` | Receber dados digitados pelo usuário |
| `exe03.py` | Comentários | Usar `#` e `"""` para documentar o código |

**Como executar:**

```bash
python exercicios/01.sintaxe/exe01.py
```

**Conceitos abordados:**
- `print("texto")` — exibe mensagem na tela
- `print(a, b, c)` — exibe múltiplos valores separados por espaço
- `input("mensagem")` — aguarda o usuário digitar algo e retorna como texto
- `int(input(...))` — converte a entrada para número inteiro
- `#` — comentário de uma linha
- `"""..."""` — comentário de múltiplas linhas (docstring)

---

## Modulo 02 — Variaveis e Tipos de Dados

**Objetivo:** Entender os quatro tipos primitivos do Python e como trabalhar com eles.

| Arquivo | Tipo | Descrição |
|---------|------|-----------|
| `int.py` | `int` | Números inteiros positivos e negativos |
| `float.py` | `float` | Números com casas decimais |
| `str.py` | `str` | Textos entre aspas simples ou duplas |
| `bool.py` | `bool` | Valores `True` ou `False` |
| `concatenacao.py` | `str` | Juntar textos com o operador `+` |
| `tipos_de_dados.py` | Todos | Visão geral e conversão entre tipos (casting) |

**Como executar:**

```bash
python exercicios/02.variaveis/tipos_de_dados.py
```

**Conceitos abordados:**

```python
idade = 25          # int  — número inteiro
altura = 1.75       # float — número decimal
nome = "João"       # str  — texto
ativo = True        # bool — verdadeiro ou falso

type(idade)         # verifica o tipo: <class 'int'>
int("123")          # casting: converte string para inteiro
```

> **Dica:** Use `type()` sempre que tiver dúvida sobre o tipo de uma variável.

---

## Modulo 03 — Estruturas de Controle

**Objetivo:** Aprender a tomar decisões e repetir ações no código.

| Arquivo | Estrutura | Descrição |
|---------|-----------|-----------|
| `01.condicionais.py` | `if / elif / else` | Executar código com base em condições |
| `02.loop_for.py` | `for` | Repetir ações um número fixo de vezes |
| `03.loop_while.py` | `while` | Repetir enquanto uma condição for verdadeira |

**Como executar:**

```bash
python exercicios/03.Estruturas/01.condicionais.py
```

**Conceitos abordados:**

```python
# Condicionais
if nota >= 9.0:
    print("Excelente!")
elif nota >= 7.0:
    print("Bom trabalho!")
else:
    print("Insuficiente.")

# Loop for — número fixo de repetições
for i in range(1, 11):
    print(i)          # imprime de 1 a 10

# Loop while — repete até condição ser falsa
contador = 0
while contador < 5:
    print(contador)
    contador += 1
```

> **Cuidado com o `while`:** sempre garanta que a condição vai se tornar `False`
> em algum momento, caso contrário o programa fica em loop infinito.

---

## Modulo 04 — Exercicios Praticos

**Objetivo:** Aplicar todos os conceitos anteriores em desafios reais.

| Arquivo | Desafio |
|---------|---------|
| `calculadora.py` | 4 exercícios progressivos (calculadora, par/ímpar, média, tabuada) |
| `cadastro_produtos.py` | Desafio final: simulador de caixa de loja com desconto |

### calculadora.py — Exercicios Progressivos

```
Exercicio 1 → Calculadora: soma, subtracao, multiplicacao e divisao
Exercicio 2 → Par ou Impar: uso do operador % (modulo)
Exercicio 3 → Media de Notas: media e resultado (Aprovado/Reprovado)
Exercicio 4 → Tabuada: loop for com range(1, 11)
```

### cadastro_produtos.py — Desafio Final

```
1. Pedir nome e preco de 3 produtos
2. Calcular o total da compra
3. Aplicar desconto de 10% se total > R$ 100
4. Exibir o valor final formatado
```

---

## Como Entregar os Exercicios

1. Faça um **fork** do repositório (botão Fork no GitHub)
2. Clone o fork na sua máquina:
   ```bash
   git clone https://github.com/SEU-USUARIO/turma-visualizacao-de-dados.git
   ```
3. Crie sua pasta dentro de `alunos/`:
   ```bash
   alunos/seu-nome/exercicios/exercicio_01/
   ```
4. Resolva os exercícios e salve seus arquivos `.py`
5. Faça commit e push:
   ```bash
   git add .
   git commit -m "feat(alunos): adiciona solucao exercicio_01 - seu-nome"
   git push origin master
   ```
6. Abra um **Pull Request** no repositório original seguindo o [guia de contribuição](../CONTRIBUTING.md)

---

## Lista de Exercícios

| # | Semana | Módulo | Tema | Arquivo | Status |
|---|--------|--------|------|---------|--------|
| 01 | 03 | Sintaxe | Print e saída de dados | `01.sintaxe/exe01.py` | Disponível |
| 02 | 03 | Sintaxe | Input e entrada de dados | `01.sintaxe/exe02.py` | Disponível |
| 03 | 03 | Sintaxe | Comentários no código | `01.sintaxe/exe03.py` | Disponível |
| 04 | 03 | Variáveis | Tipos primitivos | `02.variaveis/tipos_de_dados.py` | Disponível |
| 05 | 03 | Variáveis | Concatenação de strings | `02.variaveis/concatenacao.py` | Disponível |
| 06 | 03 | Estruturas | Condicionais if/elif/else | `03.Estruturas/01.condicionais.py` | Disponível |
| 07 | 03 | Estruturas | Loop for | `03.Estruturas/02.loop_for.py` | Disponível |
| 08 | 03 | Estruturas | Loop while | `03.Estruturas/03.loop_while.py` | Disponível |
| 09 | 03 | Prática | Exercícios mistos | `04. Exercicios/calculadora.py` | Disponível |
| 10 | 03 | Prática | Desafio final — caixa de loja | `04. Exercicios/cadastro_produtos.py` | Disponível |

---

> Dúvidas? Abra uma [Issue](https://github.com/cfneves/turma-visualizacao-de-dados/issues) no repositório.
> Material de apoio: [`aulas/semana_03/guia-python-fundamentos.html`](../aulas/semana_03/guia-python-fundamentos.html)
