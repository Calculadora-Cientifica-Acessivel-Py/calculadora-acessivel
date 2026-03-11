# Gerar um executável (Windows)

Este documento descreve como gerar um executável Windows (.exe) da calculadora usando o PyInstaller.

Pré-requisitos
--------------
- Python 3.10+ instalado e o comando `python` disponível no PATH.
- Recomendado: criar um virtualenv para isolar dependências.

Passos rápidos (cmd.exe)
------------------------
1. Abra um terminal no diretório do projeto.
2. Ative um virtualenv (opcional):

```
python -m venv .venv
.\.venv\Scripts\activate.bat
```

3. Instale dependências e gere o exe:

```
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
build_exe.bat --onefile
```

Passos rápidos (PowerShell)
--------------------------
1. Abra PowerShell no diretório do projeto.
2. Ative um virtualenv (opcional):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

3. Instale dependências e gere o exe:

```powershell
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
.\build_exe.ps1 -OneFile
```

Resultado
--------
- O executável será criado em `dist\calculadora_acessivel.exe`.

Solução de problemas
--------------------
- "Python was not found": instale o Python e marque a opção para adicionar ao PATH no instalador, ou use o caminho absoluto para o interpretador.
- "pyinstaller: command not found": verifique `pip show pyinstaller` e se o scripts folder do Python está no PATH (ou use o Python do ambiente virtual).

Notas
-----
- O modo `--onefile` produz um único exe que é conveniente para distribuição, mas pode tornar o startup um pouco mais lento.
- Teste a aplicação executável em uma máquina limpa (ou VM) para confirmar bundling de dependências.
