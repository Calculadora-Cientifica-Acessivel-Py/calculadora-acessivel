# Calculadora Acessível

Uma calculadora de linha de comando desenvolvida em Python, focada em acessibilidade e funcionalidade. O projeto oferece dois modos principais de operação: uma calculadora para expressões matemáticas e um módulo avançado para operações com matrizes.

## Recursos

### 1. Calculadora Básica
Permite a avaliação de expressões matemáticas complexas diretamente na linha de comando.

- **Funções Trigonométricas:** `sin()`, `cos()`, `tan()`.
- **Modos de Ângulo:** Suporte para Graus (`modo gra`) e Radianos (`modo rad`).
- **Funções Matemáticas:** `log()` (base 10), `ln()` (logaritmo natural), `log2()` (base 2), `sqrt()` (raiz quadrada), `exp()`, `pow()`.
- **Constantes:** `pi` e `e`.
- **Memória:** A variável `ans` armazena o último resultado para ser usado em cálculos subsequentes.

### 2. Calculadora de Matrizes
Um conjunto de ferramentas para álgebra linear, ativado com o prefixo `mat`.

- **Definição de Matrizes:** Crie e armazene matrizes com nomes personalizados (ex: `mat def A`).
- **Operações:** Adição (`mat add`), subtração (`mat sub`), multiplicação (`mat mult`).
- **Cálculos:** Determinante (`mat det`), transposta (`mat trans`), inversa (`mat inv`).
- **Gerenciamento:** Liste todas as matrizes (`mat lista`), imprima uma específica (`mat print A`) ou limpe a memória (`mat clear`).
- **Memória:** A matriz `ANS` guarda o resultado da última operação.

### 3. Recursos de Acessibilidade
- **Saída Amigável:** A impressão de matrizes é formatada para ser clara e legível por leitores de tela, descrevendo as dimensões e lendo linha por linha.
- **Comandos Claros:** A sintaxe é simples e consistente, com mensagens de erro detalhadas para guiar o usuário.

### 4. Comandos Gerais
- `help`: Exibe a ajuda completa para os modos básico e de matriz.
- `status`: Mostra o modo de ângulo atual e os últimos resultados salvos (`ans` e `ANS`).
- `arquivo [nome]`: Salva um log de todas as expressões e resultados em um arquivo de texto.
- `sair`: Encerra a aplicação.

## Como Usar

1.  **Pré-requisitos:** Certifique-se de ter o Python instalado, juntamente com a biblioteca `numpy`.
    ```shell
    pip install numpy
    ```

2.  **Executar a Calculadora:**
    Navegue até o diretório do projeto e execute o arquivo `main.py`.
    ```shell
    python main.py
    ```

### Exemplos de Uso

**Modo Básico:**
```
[RAD]> (sin(pi/2) + 5) * 2
Resultado: 12.0
[RAD]> ans / 3
Resultado: 4.0
```

**Modo Matriz:**
```
[RAD]> mat def A
Digite o número de linhas para a Matriz A: 2
Digite o número de colunas para a Matriz A: 2
Agora, insira os valores para a Matriz A.
Para cada linha, digite os 2 elementos separados por espaço.
Digite os elementos da linha 1: 1 2
Digite os elementos da linha 2: 3 4
Matriz A (2x2) salva com sucesso.

[RAD]> mat det A
Resultado (escalar): -2.0

[RAD]> mat inv A

Matriz 'ANS' (2 linhas por 2 colunas):
  Linha 1: -2.0 1.0
  Linha 2: 1.5 -0.5
```
