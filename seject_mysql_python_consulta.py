# Importamos a biblioteca:
import pymysql

# Abrimos uma conexão com o banco de dados:
conexao = pymysql.connect(db='cadastro', user='aulateste', passwd='123456')

# Cria um cursor e transforma em um dicionario:
cursor = conexao.cursor(pymysql.cursors.DictCursor)

# Executa o comando:
cursor.execute("SELECT * FROM gafanhotos ")

# Recupera o resultado:
resultado = cursor.fetchall()

cursor.execute('SELECT COUNT(nome) FROM gafanhotos')
res = cursor.fetchall()
a = (res[0]['COUNT(nome)'])
for c in range (0, a):
    cursor.execute("SELECT * FROM gafanhotos")
    h = cursor.fetchall()
    print(h[c]['id'], h[c]['nome'],h[c]['sexo'])



# Mostra o resultado:
print('resultados: ')

for linha in resultado :
    print(linha)

p = resultado
print(p[0]['nome'])
# Finaliza a conexão
conexao.close()