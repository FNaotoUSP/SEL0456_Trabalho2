import hashlib

class User:
    def __init__(self, nome, password, access_level):
        self.__set_nome(nome)
        self.__password_hash = self.__hash_password(password)
        self.__set_access_level(access_level)
    
    def __set_nome(self, nome):
        if not (1 <= len(nome) <= 20):
            raise ValueError('Nome deve ter entre 1 e 20 caracteres')
        if not nome.isalpha():
            raise ValueError('Nome deve ter apenas caracteres alfanumericos')
        self.__nome = nome
    
    def __hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    def __set_access_level(self, access_level):
        if access_level not in [1, 2, 3]:
            raise ValueError('Nivel de acesso deve ser 1, 2, ou 3')
        self.__access_level = access_level

    def verify_password(self, password):
        return self.__password_hash == self.__hash_password(password)
    
    def verify_access(self, access_level):
        return self.__access_level == self.access_level

def main():
    # usuario teste: user: sel, password: usp 
    user = User('sel', 'usp', 3)
    
    # Entrada do usuario
    nome_input = input('User name: ')
    password_input = input('Password: ')

    # Verifica o usuario e senha
    if nome_input == user._User__nome and user.verify_password(password_input):
        print(f'OK\nAccess Level = {user._User__access_level}')
    else:
        print('Acesso negado')

if __name__ == '__main__':
    main()