# Importamos a biblioteca:
import pymysql

c = str(input('Consulta ID numero: '))

# Abrimos uma conexão com o banco de dados:
conexao = pymysql.connect(db='cadastro', user='aulateste', passwd='123456')

# Cria um cursor e transforma em um dicionario:
cursor = conexao.cursor(pymysql.cursors.DictCursor)

# função para criar o SELECT
def select(fields, tables, where=None):
    global cursor
    query = ('SELECT ' + fields + ' FROM ' + tables) # colocar espaço entre a palavra e as aspas ' xx '
    if where:
        query = (query + ' where id= ' + where)
    cursor.execute(query)
    return cursor.fetchall()


a = select('nome, profissao', 'gafanhotos', c)
print (a[0]['nome'],'-->', a[0]['profissao'])
# Executa o comando:
'''cursor.execute("SELECT nome FROM gafanhotos where id = 1")

# Recupera o resultado:
resultado = cursor.fetchall()
print(resultado)

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
conexao.close() '''
