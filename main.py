import numpy as np
import ajuda             # Importa o arquivo ajuda.py
import calc_basica       # Importa o arquivo calc_basica.py
import calc_matriz       # Importa o arquivo calc_matriz.py

def calculadora_principal():
    """
    Função principal que gerencia o loop de entrada e o estado da calculadora.
    """
    # --- Estado da Calculadora Básica ---
    log_file = None
    ultimo_resultado_basico = 0
    modo_angulo = 'rad'  # 'rad' ou 'gra'
    
    # --- Estado da Calculadora de Matriz ---
    matrizes_armazenadas = {}
    ultimo_resultado_matriz = None

    print("Calculadora Acessível. Digite 'help' para ajuda ou 'sair' para encerrar.")

    while True:
        try:
            expressao = input(f"[{modo_angulo.upper()}]> ").strip()
        
        except EOFError:
            print("\nCalculadora encerrada.")
            break

        if not expressao:
            continue

        cmd_lower = expressao.lower()

        # --- Gerenciador de Comandos Gerais ---
        if cmd_lower == 'sair':
            print("Calculadora encerrada.")
            break
        
        if cmd_lower == 'help':
            ajuda.exibir_ajuda_basica()
            continue

        if cmd_lower.startswith("arquivo "):
            try:
                _, nome_arquivo = expressao.split(" ", 1)
                log_file = nome_arquivo.strip()
                if not log_file.endswith(".txt"):
                    log_file += ".txt"
                print(f"Arquivo de log '{log_file}' sendo utilizado.")
                with open(log_file, "a", encoding="utf-8") as f:
                    f.write(f"\n--- Log iniciado. Modo: {modo_angulo.upper()} ---\n")
            except Exception as e:
                print(f"Erro ao tentar criar arquivo de log: {e}")
            continue

        if cmd_lower == 'modo rad':
            modo_angulo = 'rad'
            print("Modo de ângulo definido para Radianos.")
            continue
        
        if cmd_lower == 'modo gra':
            modo_angulo = 'gra'
            print("Modo de ângulo definido para Graus.")
            continue
        
        if cmd_lower == 'status':
            print(f"Modo de ângulo atual (básico): {modo_angulo.upper()}")
            print(f"Último resultado (básico/ans): {ultimo_resultado_basico}")
            # Verifica se 'ANS' existe no armazém
            ans_matriz = "Definido" if 'ANS' in matrizes_armazenadas else "Nenhum"
            print(f"Último resultado (matriz/ANS): {ans_matriz}")
            continue
        
        # --- Roteador: Envia o comando para o módulo correto ---
        
        if cmd_lower.startswith('mat '):
            # Envia para o processador de matriz
            if cmd_lower == 'mat help':
                ajuda.exibir_ajuda_matriz()
                continue
            
            novo_res_mat = calc_matriz.processar_comando_matriz(
                expressao, 
                matrizes_armazenadas
            )

            # Se um novo resultado foi gerado, atualiza o estado
            if isinstance(novo_res_mat, np.ndarray):
                ultimo_resultado_matriz = novo_res_mat
                matrizes_armazenadas['ANS'] = novo_res_mat
            elif isinstance(novo_res_mat, float):
                ultimo_resultado_basico = novo_res_mat
                print(f"Resultado (escalar): {novo_res_mat}")
            elif novo_res_mat is None and cmd_lower == 'mat clear':
                # Limpa o estado se 'mat clear' foi chamado
                ultimo_resultado_matriz = None
                matrizes_armazenadas.clear()
        
        else:
            # Envia para o processador básico
            ultimo_resultado_basico = calc_basica.processar_calculo_basico(
                expressao, 
                ultimo_resultado_basico, 
                modo_angulo, 
                log_file
            )

# Ponto de entrada do programa
if __name__ == "__main__":
    calculadora_principal()