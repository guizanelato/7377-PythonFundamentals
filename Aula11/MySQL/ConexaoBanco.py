import pymysql
# import/ variaveis de ambiente

class BD:
    def __init__(self):
        self.host = 'localhost'
        self.usuario= 'root'
        self.senha = '4linux'
        self.banco = 'pessoa'
        self.charset = 'utf8mb4'
        self.conexao = ''
        
    def iniciaConexao(self):
        try:
            self.conexao = pymysql.connect(
                host = self.host,
                user = self.usuario,
                password = self.senha,
                db = self.banco,
                charset = self.charset,
                cursorclass = pymysql.cursors.DictCursor)
        except Exception as err:
            print('Erro ao conectar com o Banco de Dados', err)
                
    def executaSQL(self, string_sql):
        with self.conexao.cursor() as cursor:
            cursor.execute(string_sql)
            self.conexao.commit()
            return cursor         
    
    def terminaConexao(self):
        self.conexao.close() 
