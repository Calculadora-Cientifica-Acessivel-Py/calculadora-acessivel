import math

# --- Funções Trigonométricas (Modo Básico) ---
# Voltamos à precisão total. O ruído é inerente ao ponto flutuante.

def _sin(x, modo):
    if modo == 'gra':
        x = math.radians(x)
    return math.sin(x)

def _cos(x, modo):
    if modo == 'gra':
        x = math.radians(x)
    return math.cos(x)

def _tan(x, modo):
    if modo == 'gra':
        x = math.radians(x)
    return math.tan(x)

def limpar_resultado(valor):
    """
    Trata ruídos de ponto flutuante (ex: 1.22e-16 -> 0 ou 0.9999999999999 -> 1).
    Apenas se o valor for extremamente próximo de uma representação 'limpa'.
    """
    if not isinstance(valor, (int, float)):
        return valor
    
    # Se for quase zero (menor que 1e-15)
    if abs(valor) < 1e-15:
        return 0.0
    
    # Se for quase um inteiro (ex: 0.9999999999999999)
    res_arredondado = round(valor, 14)
    if math.isclose(valor, res_arredondado, rel_tol=1e-15):
        return res_arredondado
    
    return valor

def processar_calculo_basico(expressao, ultimo_resultado_basico, modo_angulo, log_file, imprimir=True):
    """
    Tenta avaliar a expressão básica.
    Retorna o novo resultado em caso de sucesso, ou o último resultado em caso de falha.
    """
    
    ambiente_basico = {
        "sin": lambda x: _sin(x, modo_angulo),
        "cos": lambda x: _cos(x, modo_angulo),
        "tan": lambda x: _tan(x, modo_angulo),
        "log": math.log10, "ln": math.log, "log2": math.log2,
        "sqrt": math.sqrt, "exp": math.exp, "pow": math.pow,
        "pi": math.pi, "e": math.e, "round": round,
        "ans": ultimo_resultado_basico
    }

    try:
        # Avalia a expressão com precisão total
        resultado_bruto = eval(expressao, {"__builtins__": {}}, ambiente_basico)
        
        # Limpa apenas para exibição e armazenamento do ans
        resultado = limpar_resultado(resultado_bruto)
        
        if imprimir:
            print(f"Resultado: {resultado}")

        if log_file and imprimir: # Apenas loga se for para imprimir (evita duplicação em funções)
            with open(log_file, "a", encoding="utf-8") as f:
                f.write(f"[{modo_angulo.upper()}] {expressao} = {resultado}\n")
        
        return resultado 

    # Erros específicos do modo básico
    except ZeroDivisionError:
        if imprimir: print("Erro: Tentativa de divisão por zero.")
    except SyntaxError:
        if imprimir: print("Erro: Expressão mal formada. Verifique parênteses ou operadores.")
    except NameError as ne:
        if imprimir:
            try:
                nome_invalido = str(ne).split("'")[1]
            except:
                nome_invalido = "(desconhecido)"
            print(f"Erro: Função ou constante '{nome_invalido}' não reconhecida. Digite 'help'.")
    except TypeError:
         if imprimir: print("Erro: Tipo de argumento inválido (ex: sin('texto')).")
    except Exception as e:
        if imprimir: print(f"Erro inesperado no cálculo: {e}")
    
    return ultimo_resultado_basico