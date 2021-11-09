class OlaMundo:  # Para nomear classes, a primeira letra de cada palavra é maiúscula e nomes compostos não utilizam espaços ou '_'
    def __init__(self, nome, sexo, cpf):  # '__init__' é o construtor
        #  Para nomear atributos, sempre usar letras minúsculas e separar nomes compostos com '_'
        #  Para nomear constantes, sempre usar letras maiúsculas e separar nomes compostos com '_'
        self.DATA_DE_NASCIMENTO = '15/07/1982'
        self.ola_mundo = 'Olá Mundo!'
        self._nome = nome  # '_' no início do nome do atributo indica acesso protegido
        self.sexo = sexo
        self.__cpf = cpf  # '__' no início do nome do atributo indica acesso privado

    def get_cpf(self):
        return self.__cpf

    def get_nome(self):
        return self._nome


if __name__ == '__main__':  # método 'main'
    pessoa1 = OlaMundo('João', 'M', '123456')
    print(pessoa1.ola_mundo)
    print(pessoa1.get_nome())
    print(pessoa1.sexo)
    print(pessoa1.get_cpf())

#  'if a is not b' é melhor que 'if not a is b'
#  'if not lista' é melhor que 'if len(lista) == 0'
#  'import os print(os.getcwd())' é melhor que 'from os import * print(getcwd())'
