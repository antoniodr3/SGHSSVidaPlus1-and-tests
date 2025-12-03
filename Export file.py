
import os

# Diretórios de origem
diretorios = [
    r"C:\Users\AcessHigh\Documents\Novo projeto\PythonVidaPlus1",
    r"C:\Users\AcessHigh\Documents\Novo projeto\tests"
]

# Caminho do arquivo consolidado
saida = r"C:\Users\AcessHigh\Documents\Novo projeto\Projeto_Completo.txt"

with open(saida, "w", encoding="utf-8") as f_saida:
    for pasta in diretorios:
        for raiz, _, arquivos in os.walk(pasta):
            for arquivo in arquivos:
                caminho = os.path.join(raiz, arquivo)
                try:
                    with open(caminho, "r", encoding="utf-8", errors="ignore") as f_origem:
                        conteudo = f_origem.read()

                    # Escreve cabeçalho para separar cada arquivo
                    f_saida.write(f"\n\n===== {caminho} =====\n\n")
                    f_saida.write(conteudo)

                    print(f"Adicionado: {caminho}")
                except Exception as e:
                    print(f"⚠️ Erro ao ler {caminho}: {e}")

print("✅ Arquivo consolidado gerado:", saida)
