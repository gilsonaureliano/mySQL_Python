# Importamos a biblioteca:
import pymysql

# Abrimos uma conexão com o banco de dados:
conexao = pymysql.connect(db='cadastro', user='aulateste', passwd='123456')

# Cria um cursor:
cursor = conexao.cursor()

# Executa o comando:
cursor.execute("UPDATE gafanhotos SET profissao = 'Físico' WHERE nome = 'Daniel Morais'")

# Efetua um commit no banco de dados.
# Por padrão, não é efetuado commit automaticamente. Você deve commitar para salvar
# suas alterações.
conexao.commit()

# Finaliza a conexão
conexao.close()