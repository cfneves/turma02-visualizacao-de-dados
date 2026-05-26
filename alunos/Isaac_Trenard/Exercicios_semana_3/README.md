cat > README.md << 'EOF'
# Semana 3 - Configuração do Ambiente de Trabalho/Estudo

Nesta semana, preparei meu computador para programar em Python e usar Git/GitHub. Foi uma semana mais de configuração, mas aprendi coisas essenciais para o curso.

---

### 1. Instalação do Python

## O que é Python?
É a linguagem de programação que uso para escrever códigos, fazer cálculos e analisar dados.

# Como instalei:
1. Fui no site [python.org]
2. Baixei a versão para Windows
3. **Importante:** Marquei a opção `"Add Python to PATH"` antes de instalar
4. Cliquei em "Install Now"
5. Verifiquei no **CMD** com o comando:
   python --version

### 2. Instalação do VS Code e Extensões

## O que é VS Code?
É o editor onde escrevo meus códigos.

## O que instalei:
Baixei o VS Code no site oficial
Instalei a extensão Python (da Microsoft) - ajuda a escrever código
Instalei a extensão Jupyter

## A.1 ⚠️ Mas deu problema com o Jupyter e como resolvi

### O que aconteceu?

Quando tentei trabalhar com arquivos `.ipynb` (notebooks do Jupyter), tive duas dificuldades:

# B.1 **O VS Code não abria arquivos `.ipynb`** – aparecia uma mensagem dizendo que não era possível abrir porque faltava a extensão do Jupyter.
# C.1 **O terminal não reconhecia o comando `jupyter`** – sempre que tentava executar `jupyter --version` ou `jupyter notebook`, o sistema dizia que o comando não era encontrado.

### Por que aconteceu?

**Primeiro problema:** Faltava instalar a extensão correta no VS Code.
**Segundo problema:** O Python foi instalado, mas a pasta onde ficam os executáveis (como `jupyter.exe` e `pip.exe`) **não estava no PATH do sistema**. Por isso, o terminal não conseguia encontrar o comando `jupyter`.

> **O que é PATH?**  
> O PATH é uma lista de pastas que o Windows usa para encontrar programas quando você digita um comando no terminal. Se a pasta do Python não está nessa lista, você precisa dar o endereco completo ou usar uma alternativa.

### Como resolvi:

## D.1 Instalei a extensão Jupyter no VS Code

Abri o VS Code, fui na aba de extensões (`Ctrl + Shift + X`)
Pesquisei por **Jupyter** e instalei a extensão da Microsoft
Depois disso, o VS Code passou a abrir arquivos `.ipynb` normalmente

## E.1 Passei a usar `python -m` para executar o Jupyter

Como o `jupyter` não era reconhecido diretamente, comecei a usar o Python para executar o Jupyter como um módulo:

# Para verificar a instalação
python -m jupyter --version

# Para abrir o Jupyter Notebook
python -m notebook

#### 3. Comandos que pratiquei no terminal do VS CODE

Comando	O que faz
dir  -	Lista os arquivos da pasta
cd nome_da_pasta	Entra em uma pasta ESPECIFICA
cd ..	Volta uma pasta
mkdir nome_da_pasta	Cria uma nova pasta
New-Item NOME_DO_ARQUIVO.py	Cria um arquivo Python

#### 4. Fluxo Git que aprendi
Aprendi o ciclo básico para enviar meus códigos para o GitHub:

git pull          # Baixar novidades do GitHub CHEGA DO TRABALHO/ESCOLA FAZ PR
git add .         # Preparar os arquivos GUARDA O EXERCICIOS FEITO (espaço entre add e .)
git commit -m "mensagem"   # Salvar versão com descrição PERSONALIZADA PAAR ORIENTACAO PARA O PROFESSOR
git push          # Enviar para o GitHub REPOSITORIO NA NUVEM