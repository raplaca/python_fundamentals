import MySQLdb


# try:
#     con = MySQLdb.connect(host="localhost", user="admin", passwd="4linux", db="projetos")

#     cur = con.cursor()

#     cur.execute("insert into clientes(nome, endereco) values ('Carlos', 'Madureira') ")

#     con.commit()
#     print('Registro criado com sucesso!')

# except Exception as e:
#     print(f'Erro: {e}')
#     print('Fazendo rollback')
#     con.rollback

# finally:
#     print('Finalizando conexão com banco de dados')
#     cur.close()
#     con.close()



####### lendo ######

try:
    con = MySQLdb.connect(host="localhost", user="admin", passwd="4linux", db="projetos")
    cur = con.cursor()
    # cur.execute("insert into clientes(nome, endereco) values ('Carlos', 'Madureira')")
    # con.commit()
    # print('Registro criado com sucesso!')

    cur.execute("select * from clientes")
    # print('Primeiro registro da tabela:\n', cur.fetchone())
    print('Todos os registros:\n', cur.fetchall())
except Exception as e:
    print(f'Erro: {e}')
    # print('Fazendo rollback')
    # con.rollback()

finally:
    print('Finalizando conexão com o banco de dados')
    cur.close()
    con.close()