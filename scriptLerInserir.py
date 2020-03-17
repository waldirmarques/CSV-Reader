import csv

arquivo = open('Comentários SEMOB - Página1.csv')

linhas = csv.reader(arquivo)

arquivo = open('V120200313104100__insert_table_comentario_usuario.sql','w')
for linha in linhas:
    listaComentario = linha[2]
    arquivo.write("INSERT INTO comentario (comentario, usuario_id) VALUES(\'"+listaComentario+"\'"+", 1)"+";\n")