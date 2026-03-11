import math
import modules.calc_basica as calc_basica

def processar_comando_funcao(expressao, armazem_funcoes, ultimo_resultado_basico, modo_angulo):
    """
    Processa comandos com o prefixo 'fn'.
    Exemplos: 
    fn def f(x) = x**2 + sin(x)
    fn f(2)
    fn lista
    """
    partes = expressao.split()
    if len(partes) < 2:
        print("Erro: Comando 'fn' incompleto. Digite 'fn help'.")
        return ultimo_resultado_basico

    comando = partes[1].lower()

    # --- Comando: fn def ---
    if comando == 'def':
        # Esperado: fn def f(x) = x + 2
        try:
            # Pega tudo depois de 'fn def '
            resto = expressao[len("fn def "):].strip()
            if '=' not in resto:
                print("Erro: Use o formato 'fn def f(x) = expressão'.")
                return ultimo_resultado_basico
            
            assinatura, corpo = resto.split('=', 1)
            assinatura = assinatura.strip()
            corpo = corpo.strip()

            if '(' not in assinatura or ')' not in assinatura:
                print("Erro: Defina a variável entre parênteses. Ex: 'f(x)'.")
                return ultimo_resultado_basico

            nome_fn = assinatura.split('(')[0].strip()
            variavel = assinatura.split('(')[1].split(')')[0].strip()

            if not nome_fn or not variavel:
                print("Erro: Nome da função ou variável inválidos.")
                return ultimo_resultado_basico

            armazem_funcoes[nome_fn] = {"var": variavel, "exp": corpo}
            print(f"Função '{nome_fn}({variavel}) = {corpo}' salva com sucesso.")
            
        except Exception as e:
            print(f"Erro ao definir função: {e}")
        return ultimo_resultado_basico

    # --- Comando: fn lista ---
    elif comando == 'lista':
        if not armazem_funcoes:
            print("Nenhuma função personalizada definida.")
        else:
            print("Funções definidas:")
            for nome, dados in armazem_funcoes.items():
                print(f"  {nome}({dados['var']}) = {dados['exp']}")
        return ultimo_resultado_basico

    # --- Comando: fn clear ---
    elif comando == 'clear':
        armazem_funcoes.clear()
        print("Todas as funções personalizadas foram removidas.")
        return ultimo_resultado_basico

    # --- Avaliação: fn f(val) ---
    else:
        # Tenta identificar se o comando é uma chamada de função: f(5)
        try:
            if '(' in expressao and ')' in expressao:
                # Extrai nome da função e o valor entre parênteses
                # Ex: 'fn f(2)' -> nome 'f', valor '2'
                inicio_par = expressao.find('(')
                fim_par = expressao.rfind(')')
                
                nome_chamada = expressao[len("fn "):inicio_par].strip()
                valor_str = expressao[inicio_par+1:fim_par].strip()

                if nome_chamada in armazem_funcoes:
                    fn_dados = armazem_funcoes[nome_chamada]
                    var_nome = fn_dados['var']
                    corpo_exp = fn_dados['exp']

                    # Avalia o valor passado (pode ser uma expressão como 'pi/2')
                    val_avaliado = calc_basica.processar_calculo_basico(
                        valor_str, ultimo_resultado_basico, modo_angulo, None
                    )

                    # Substitui a variável no corpo da função
                    # Usamos um truque de ambiente para o eval
                    expressao_final = corpo_exp.replace(var_nome, f"({val_avaliado})")
                    
                    print(f"Avaliando {nome_chamada}({val_avaliado})...")
                    resultado = calc_basica.processar_calculo_basico(
                        expressao_final, ultimo_resultado_basico, modo_angulo, None
                    )
                    return resultado
                else:
                    print(f"Erro: Função '{nome_chamada}' não encontrada.")
            else:
                print(f"Erro: Comando '{comando}' não reconhecido.")
        except Exception as e:
            print(f"Erro ao avaliar função: {e}")
        
    return ultimo_resultado_basico
