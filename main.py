from credenciais import credencial

class Conexao:
    def __init__(self):
        self.usuario = credencial.get('usuario')
        self.__senha = credencial.get('senha')

if __name__ == '__main__':
    x = Conexao()
    print(x.__senha)
