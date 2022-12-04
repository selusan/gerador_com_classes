import random

class ColecaoDados:
    def __init__(self):
        self.nome = ['Juarez','Natalia','Igor','Mateus','Livia'] 
        self.telefone = ['43991876543','4199765434','44994235678','4599637388','43991564789']
        self.email = ['jr@email.com','ig@email.com','hr@email.com','mt@email.com','lv@email.com']

    def gerar_nomes(self):
        nome_escolhido = random.choice(self.nome)
        return print(nome_escolhido)

    def gerar_telefones(self):
        telefone_escolhido = random.choice(self.telefone)
        return print(telefone_escolhido)

    def gerar_email(self):
        email_escolhido = random.choice(self.email)
        return print(email_escolhido)
        

