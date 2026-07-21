'''

'''

leitura_arquivo = open('leitura_arquivo_yasmin.txt','r', encoding='utf-8')

conteudo_arquivo = leitura_arquivo.readlines()

print(conteudo_arquivo[4].strip())
print(conteudo_arquivo[8].strip())

leitura_arquivo.close()