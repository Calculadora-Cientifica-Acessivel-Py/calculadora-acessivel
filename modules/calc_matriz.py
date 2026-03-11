import numpy as np

# --- Funções de Matriz (Refatoradas do seu código) ---
def obter_dimensoes(matriz_nome):
    """Solicita e retorna as dimensões (linhas, colunas) de uma matriz."""
    while True:
        try:
            linhas = int(input(f"Digite o número de linhas para a Matriz {matriz_nome}: "))
            colunas = int(input(f"Digite o número de colunas para a Matriz {matriz_nome}: "))
            if linhas > 0 and colunas > 0:
                return linhas, colunas
            else:
                print("Erro: O número de linhas e colunas deve ser positivo.")
        except ValueError:
            print("Erro: Por favor, digite um número inteiro válido.")

def obter_matriz(linhas, colunas, matriz_nome):
    """Solicita os elementos de uma matriz e a retorna como um array NumPy."""
    matriz = np.zeros((linhas, colunas))
    print(f"Agora, insira os valores para a Matriz {matriz_nome}.")
    print(f"Para cada linha, digite os {colunas} elementos separados por espaço.")

    for i in range(linhas):
        while True:
            try:
                entrada = input(f"Digite os elementos da linha {i + 1}: ")
                elementos = [float(e) for e in entrada.split()]
                if len(elementos)!= colunas:
                    print(f"Erro: Você deve inserir exatamente {colunas} elementos. Você inseriu {len(elementos)}.")
                    continue
                matriz[i, :] = elementos
                break
            except ValueError:
                print("Erro: Um ou mais elementos não são números válidos. Por favor, tente novamente.")
    return matriz

def imprimir_matriz_acessivel(matriz, nome_matriz):
    """
    Imprime uma matriz de forma acessível para leitores de tela.
    """
    if not isinstance(matriz, np.ndarray):
        print(f"Erro: Tentativa de imprimir algo que não é uma matriz ({nome_matriz}).")
        return
        
    try:
        linhas, colunas = matriz.shape
        # 1. O SUMÁRIO (Princípio da "Visão Geral")
        print(f"\nMatriz '{nome_matriz}' ({linhas} linhas por {colunas} colunas):")
        
        # 2. OS DADOS (Leitura linear)
        for i, linha in enumerate(matriz):
            elementos_formatados = ' '.join([str(round(elem, 4)) for elem in linha])
            print(f"  Linha {i + 1}: {elementos_formatados}")
        print() 
    except Exception as e:
        print(f"Erro ao imprimir matriz: {e}")

def obter_matriz_do_armazem(nome, armazem):
    """Função auxiliar para buscar uma matriz do 'armazém'."""
    nome_upper = nome.upper()
    if nome_upper in armazem:
        return armazem[nome_upper]
    else:
        print(f"Erro: Matriz '{nome_upper}' não encontrada. Use 'mat lista' para ver as matrizes salvas.")
        return None

# --- Processador de Comandos de Matriz ---

def obter_duas_matrizes(partes, armazem):
    """Obtém duas matrizes do armazém para operações binárias."""
    if len(partes) < 4:
        print(f"Erro: Uso: 'mat {partes[1]} [A] [B]'")
        return None, None
    
    mat_a = obter_matriz_do_armazem(partes[2], armazem)
    mat_b = obter_matriz_do_armazem(partes[3], armazem)
    return mat_a, mat_b

def processar_comando_matriz(expressao, armazem_matrizes):
    """
    Analisa a 'expressao' e executa a operação de matriz.
    Retorna o novo 'ultimo_resultado_matriz' ou o antigo em caso de falha.
    """
    partes = expressao.lower().split()
    comando = partes[1] if len(partes) > 1 else ""

    try:
        if comando == 'def':
            if len(partes) < 3:
                print("Erro: Especifique um nome para a matriz. Ex: 'mat def A'")
            else:
                nome_matriz = partes[2].upper()
                if nome_matriz == 'ANS':
                    print("Erro: 'ANS' é um nome reservado para o último resultado.")
                    return armazem_matrizes.get('ANS')
                
                linhas, colunas = obter_dimensoes(nome_matriz)
                matriz = obter_matriz(linhas, colunas, nome_matriz)
                armazem_matrizes[nome_matriz] = matriz
                print(f"Matriz {nome_matriz} ({linhas}x{colunas}) salva com sucesso.")

        elif comando == 'lista':
            if not armazem_matrizes:
                print("Nenhuma matriz salva na memória.")
            else:
                print("Matrizes salvas:")
                for nome, mat in armazem_matrizes.items():
                    print(f"  {nome} ({mat.shape[0]}x{mat.shape[1]})")

        elif comando == 'print':
            if len(partes) < 3:
                print("Erro: Especifique qual matriz imprimir. Ex: 'mat print A'")
            else:
                mat = obter_matriz_do_armazem(partes[2], armazem_matrizes)
                if mat is not None:
                    imprimir_matriz_acessivel(mat, partes[2].upper())

        elif comando == 'clear':
            armazem_matrizes.clear()
            print("Todas as matrizes foram limpas da memória.")
            return None
        
        elif comando in ['add', 'sub', 'mult']:
            mat_a, mat_b = obter_duas_matrizes(partes, armazem_matrizes)
            if mat_a is None or mat_b is None:
                return armazem_matrizes.get('ANS')

            if comando == 'add':
                if mat_a.shape != mat_b.shape:
                    print("Erro: As matrizes devem ter as mesmas dimensões para adição.")
                    return armazem_matrizes.get('ANS')
                resultado = mat_a + mat_b
            
            elif comando == 'sub':
                if mat_a.shape != mat_b.shape:
                    print("Erro: As matrizes devem ter as mesmas dimensões para subtração.")
                    return armazem_matrizes.get('ANS')
                resultado = mat_a - mat_b

            elif comando == 'mult':
                if mat_a.shape[1] != mat_b.shape[0]:
                    print(f"Erro: O número de colunas de A ({mat_a.shape[1]}) deve ser igual ao número de linhas de B ({mat_b.shape[0]}).")
                    return armazem_matrizes.get('ANS')
                resultado = np.dot(mat_a, mat_b)

            imprimir_matriz_acessivel(resultado, "ANS")
            armazem_matrizes['ANS'] = resultado
            return resultado

        elif comando in ['det', 'trans', 'inv']:
            if len(partes) < 3:
                print(f"Erro: Uso: 'mat {comando} [A]'")
                return armazem_matrizes.get('ANS')

            mat = obter_matriz_do_armazem(partes[2], armazem_matrizes)
            if mat is None:
                return armazem_matrizes.get('ANS')

            if mat.shape[0] != mat.shape[1] and comando != 'trans':
                 print(f"Erro: Operação '{comando}' só existe para matrizes quadradas.")
                 return armazem_matrizes.get('ANS')

            if comando == 'det':
                resultado = np.linalg.det(mat)
                return resultado
            
            elif comando == 'trans':
                resultado = mat.T

            elif comando == 'inv':
                try:
                    resultado = np.linalg.inv(mat)
                except np.linalg.LinAlgError:
                    print("Erro: A matriz não é invertível (determinante é zero).")
                    return armazem_matrizes.get('ANS')
            
            imprimir_matriz_acessivel(resultado, "ANS")
            armazem_matrizes['ANS'] = resultado
            return resultado
        
        else:
            print(f"Erro: Comando de matriz '{comando}' não reconhecido. Digite 'mat help'.")

    except Exception as e:
        print(f"Ocorreu um erro inesperado no processamento de matriz: {e}")

    return armazem_matrizes.get('ANS') # Retorna o 'ans' antigo se nada novo foi gerado