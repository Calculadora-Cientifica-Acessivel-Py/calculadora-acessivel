def exibir_ajuda_basica():
    """Imprime o guia de ajuda para os modos básico, de matriz e de funções."""
    print("\n--- Ajuda da Calculadora Acessível ---")
    
    print("\nModo Básico (Expressões):")
    print("  Digite expressões como 'sin(pi/2) + (ans * 2)'")
    print("  status        : Exibe o modo de ângulo e o último resultado (ans).")
    print("  modo rad      : Define o modo de ângulo para Radianos (padrão).")
    print("  modo gra      : Define o modo de ângulo para Graus.")
    
    print("\nModo Matriz (prefixo 'mat'):")
    print("  mat help      : Mostra todos os comandos de matriz.")
    print("  mat def [NOME]: Inicia o assistente para criar uma matriz (ex: 'mat def A').")
    print("  mat lista     : Lista todas as matrizes salvas (ex: A, B, ANS).")
    
    print("\nModo Funções (prefixo 'fn'):")
    print("  fn help       : Mostra todos os comandos de funções.")
    print("  fn def f(x)=..: Define uma nova função (ex: 'fn def f(x) = x**2').")
    print("  fn f(val)     : Avalia a função f no ponto val (ex: 'fn f(5)').")

    print("\nComandos Gerais:")
    print("  help          : Mostra esta ajuda.")
    print("  arquivo [nome]: Salva todos os cálculos futuros em [nome].txt.")
    print("  sair          : Encerra a calculadora.")
    print("----------------------------------------\n")

def exibir_ajuda_matriz():
    """Imprime a ajuda específica para o modo de matriz."""
    print("\n--- Ajuda do Modo Matriz ---")
    print("Use 'ANS' para se referir ao resultado da última operação de matriz.")
    print("\nComandos:")
    print("  mat def [NOME]   : Define uma nova matriz (ex: mat def A).")
    print("  mat lista        : Lista todas as matrizes salvas.")
    print("  mat print [NOME] : Imprime uma matriz salva (ex: mat print A).")
    print("  mat clear        : Limpa todas as matrizes da memória.")
    print("  mat add [A]  : Soma A e B (ex: mat add A B).")
    print("  mat sub [A]  : Subtrai B de A (ex: mat sub A B).")
    print("  mat mult [A] : Multiplica A por B (ex: mat mult A B).")
    print("  mat det [A]      : Calcula o determinante de A (ex: mat det A).")
    print("  mat trans [A]    : Calcula a transposta de A (ex: mat trans A).")
    print("  mat inv [A]      : Calcula a inversa de A (ex: mat inv A).")
    print("----------------------------------------\n")

def exibir_ajuda_funcao():
    """Imprime a ajuda específica para o modo de funções."""
    print("\n--- Ajuda do Modo Funções ---")
    print("Defina funções personalizadas para usar em seus cálculos.")
    print("\nComandos:")
    print("  fn def [f(x)] = [exp] : Define uma nova função (ex: fn def f(x) = x + 2).")
    print("  fn [nome]([valor])    : Avalia a função salva no valor dado (ex: fn f(5)).")
    print("  fn lista              : Lista todas as funções salvas.")
    print("  fn clear              : Limpa todas as funções da memória.")
    print("  fn help               : Exibe esta ajuda.")
    print("----------------------------------------\n")