import os
import shutil
import pandas as pd
import unidecode

#Config

path_pdf_antigo = 'input/PDF'
path_pdf_renomeado = 'output/PDF'
path_nomes_para_renomear = 'input/planilha/nomes_novos.xlsx'

os.makedirs(path_pdf_renomeado, exist_ok=True)

try:
    df = pd.read_excel(path_nomes_para_renomear)
    lista = df['Nomes'].tolist()

except Exception as e:
    print(f'Erro ao lear a planilha: {e}')

for i, nomes_novos in enumerate(lista, start=1):
    nome_antigo = f'all-{i}.pdf'
    nome_formatado = unidecode.unidecode(nomes_novos.strip().lower().replace('','_'))
    nome_novo = f'{nome_formatado}.pdf'

    path_nomes_antigos = os.path.join(path_pdf_antigo, nome_antigo)
    path_nomes_renomeados = os.path.join(path_pdf_renomeado, nome_novo)

    if os.path.exists(path_pdf_antigo):
        shutil.copyfile(path_nomes_antigos, path_nomes_renomeados)
        print(f'{nome_antigo} => {nome_novo}')

    else:
        print(f'Arquivo não encontrado: {nome_antigo}')

print('\n TODOS OS ARQUIVOS RENOMEADOS')
