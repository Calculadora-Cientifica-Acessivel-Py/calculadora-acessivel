# Manual do Usuário: Calculadora Acessível

A **Calculadora Acessível** é uma aplicação de linha de comando (CLI) desenvolvida para oferecer autonomia técnica a estudantes e profissionais, com foco absoluto na experiência de usuários de leitores de tela.

---

## 🧑‍🦯 Compromisso com a Acessibilidade

Este manual e a aplicação foram projetados seguindo estas premissas:
1.  **Navegação Previsível**: Comandos curtos e consistentes.
2.  **Saída Verbosa e Estruturada**: Resultados que fazem sentido ao serem lidos de cima para baixo.
3.  **Sem Ambiguidade Visual**: Informações críticas não dependem de cores ou disposição espacial complexa.
4.  **Aritmética Limpa**: Tratamento de erros de ponto flutuante para evitar a leitura de dízimas científicas desnecessária.

---

## 📖 Sumário
- [Manual do Usuário: Calculadora Acessível](#manual-do-usuário-calculadora-acessível)
  - [🧑‍🦯 Compromisso com a Acessibilidade](#-compromisso-com-a-acessibilidade)
  - [📖 Sumário](#-sumário)
  - [1. Primeiros Passos](#1-primeiros-passos)
    - [Como Iniciar](#como-iniciar)
    - [O Prompt de Comando](#o-prompt-de-comando)
  - [2. Interpretação da Saída](#2-interpretação-da-saída)
  - [3. Modo Básico: Cálculos Diretos](#3-modo-básico-cálculos-diretos)
    - [Memória de Curto Prazo (`ans`)](#memória-de-curto-prazo-ans)
    - [Funções e Constantes](#funções-e-constantes)
  - [4. Modo de Matrizes: Álgebra Linear](#4-modo-de-matrizes-álgebra-linear)
    - [Criando uma Matriz (Passo a Passo)](#criando-uma-matriz-passo-a-passo)
    - [Como as Matrizes são lidas?](#como-as-matrizes-são-lidas)
  - [5. Modo de Funções: Fórmulas Personalizadas](#5-modo-de-funções-fórmulas-personalizadas)
    - [Criando uma Função](#criando-uma-função)
    - [Usando a Função](#usando-a-função)
  - [6. Registro de Sessão (Logs)](#6-registro-de-sessão-logs)
  - [7. Referência Rápida de Comandos](#7-referência-rápida-de-comandos)

---

## 1. Primeiros Passos

### Como Iniciar
Execute o arquivo calculadora_acessivel.exe

### O Prompt de Comando
Ao iniciar, você ouvirá: `[RAD]>`. 
- Isso indica que a calculadora está pronta e no modo **Radianos**.
- Se você mudar para graus, o prompt mudará para `[GRA]>`.

---

## 2. Interpretação da Saída

Diferente de calculadoras visuais onde o resultado aparece em um visor fixo, aqui o resultado é uma nova linha de texto.

- **Para usuários de NVDA/JAWS**: Após pressionar `Enter`, o leitor geralmente lerá a linha do resultado automaticamente. Se não ler, use as teclas de navegação do leitor (seta para cima) para ouvir o resultado anterior.
- **Formato do Resultado**: Sempre seguirá o padrão `Resultado: [VALOR]`.

---

## 3. Modo Básico: Cálculos Diretos

Basta digitar a conta e dar Enter.

### Memória de Curto Prazo (`ans`)
O resultado do último cálculo básico é salvo na variável `ans`.
- Exemplo: Digite `10 + 10`. O resultado é `20`.
- Em seguida, digite `ans * 2`. O resultado será `40`.

### Funções e Constantes
- **Constantes matemática**: `pi` e `e`, onde e refere-se ao número de Euler sendo e=2,718281828.
- **Trigonometria**: `sin()`, `cos()`, `tan()`.
- **Raiz e Potência**: `sqrt(16)` (raiz), `pow(2, 3)` (2 elevado a 3) ou `2**3`.
- **Logaritmos**: `log(100)` (base 10), `ln(e)` (logaritmo natural).

---

## 4. Modo de Matrizes: Álgebra Linear

As operações de matriz usam o prefixo `mat`. Este modo é **interativo**.

### Criando uma Matriz (Passo a Passo)
1.  Digite `mat def A` e `Enter`.
2.  O sistema perguntará: "Digite o número de linhas". Digite um número e `Enter`.
3.  Perguntará o número de colunas. Digite e `Enter`.
4.  O sistema pedirá os elementos de cada linha. Digite os números separados por espaço.
    - *Dica*: O leitor dirá "Digite os elementos da linha 1". Isso ajuda você a se localizar.

### Como as Matrizes são lidas?
Ao usar `mat print A`, a saída será:
`Matriz 'A' (2 linhas por 2 colunas):`
`  Linha 1: 1.0 2.0`
`  Linha 2: 3.0 4.0`
Isso permite que você entenda a estrutura da matriz lendo linha por linha.

---

## 5. Modo de Funções: Fórmulas Personalizadas

Útil para quando você tem uma fórmula que usa várias vezes. Usa o prefixo `fn`.

### Criando uma Função
Para definir $f(x) = x^2 + 5$:
Digite: `fn def f(x) = x**2 + 5`

### Usando a Função
Para calcular $f$ no valor 10:
Digite: `fn f(10)`
A calculadora responderá: `Avaliando f(10.0)... Resultado: 105.0`.

---

## 6. Registro de Sessão (Logs)

Se você precisa entregar um trabalho ou revisar seus cálculos:
Digite: `arquivo meu_calculo`

Um arquivo chamado `meu_calculo.txt` será criado. Tudo o que você digitar e todos os resultados que aparecerem na tela serão gravados nele até você fechar a calculadora.

---

## 7. Referência Rápida de Comandos

| Comando | O que faz |
| :--- | :--- |
| `help` | Ajuda geral |
| `status` | Mostra modo de ângulo e memórias |
| `modo gra` | Muda para Graus |
| `modo rad` | Muda para Radianos |
| `mat lista` | Lista matrizes salvas |
| `fn lista` | Lista funções salvas |
| `mat clear` | Limpa memória de matrizes |
| `sair` | Fecha o programa |

---

*Manual versão 1.1*
