import math

# --- Funções Trigonométricas (Modo Básico) ---

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

def processar_calculo_basico(expressao, ultimo_resultado_basico, modo_angulo, log_file):
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
        resultado = eval(expressao, {"__builtins__": {}}, ambiente_basico)
        print(f"Resultado: {resultado}")

        if log_file:
            with open(log_file, "a", encoding="utf-8") as f:
                f.write(f"[{modo_angulo.upper()}] {expressao} = {resultado}\n")
        
        return resultado # Retorna o novo resultado em caso de sucesso

    # Erros específicos do modo básico
    except ZeroDivisionError:
        print("Erro: Tentativa de divisão por zero.")
    except SyntaxError:
        print("Erro: Expressão mal formada. Verifique parênteses ou operadores.")
    except NameError as ne:
        try:
            nome_invalido = str(ne).split("'")[1]
        except:
            nome_invalido = "(desconhecido)"
        print(f"Erro: Função ou constante '{nome_invalido}' não reconhecida. Digite 'help'.")
    except TypeError:
         print("Erro: Tipo de argumento inválido (ex: sin('texto')).")
    except Exception as e:
        print(f"Erro inesperado no cálculo: {e}")
    
    return ultimo_resultado_basico # Retorna o resultado antigo em caso de falha