# Calculadora Acessível ♿

Uma calculadora de linha de comando (CLI) desenvolvida em Python, projetada especificamente para oferecer autonomia técnica a usuários de leitores de tela. O projeto une cálculos matemáticos avançados, álgebra linear e funções personalizadas com uma interface textual clara e semântica.

## 🌟 Principais Diferenciais

- **Foco em Acessibilidade**: Saída de dados formatada para leitura linear (NVDA, JAWS, Narrador).
- **Aritmética Inteligente**: Eliminação de ruídos de ponto flutuante em funções trigonométricas (ex: `sin(pi)` retorna `0.0`).
- **Módulos Avançados**: Suporte completo para Álgebra Linear (matrizes) e Definição de Funções.
- **Persistência de Sessão**: Registro automático de cálculos em arquivos de log para auditoria e revisão.

## 🛠️ Tecnologias Utilizadas

- **Python 3.11+**: Linguagem base.
- **NumPy**: Motor de processamento para álgebra linear.
- **PyInstaller**: Utilizado para gerar os executáveis independentes.

## 📂 Estrutura do Projeto

```text
calculadora-acessivel/
├── modules/            # Lógica dos submódulos (Matrizes, Funções, Base)
├── executavel/         # Versão compilada para Windows (.exe)
├── main.py             # Ponto de entrada e orquestração do CLI
├── MANUAL_DO_USUARIO.md # Documentação detalhada para o usuário final
└── README.md           # Visão geral do projeto
```

## 🚀 Como Começar

### Pré-requisitos
- Python 3.11 ou superior instalado.
- Biblioteca NumPy instalada: `pip install numpy`

### Execução Direta
```bash
python main.py
```

### Usando o Executável
Navegue até a pasta `executavel/` e rode o arquivo `calculadora_acessivel.exe`. Não é necessário instalar o Python neste caso.

## 📖 Documentação

Para instruções detalhadas de todos os comandos (básico, `mat` e `fn`), consulte o nosso [Manual do Usuário](MANUAL_DO_USUARIO.md).

## 🤝 Contribuição

Contribuições que melhorem a experiência de acessibilidade são muito bem-vindas!
1. Faça um Fork do projeto.
2. Crie uma Branch para sua feature (`git checkout -b feature/NovaFuncao`).
3. Comite suas mudanças.
4. Abra um Pull Request.

---
*Desenvolvido com foco em inclusão e precisão técnica.*
