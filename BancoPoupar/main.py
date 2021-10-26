import os
from datetime import datetime

def bank_statement():
    # asking the cpf
    cpf = input('Digite o CPF cadastrado: ')
    lista=[] # this list was made to basically access the file with more assurance than change that directly.
    #checking if the cpf is correct
    if os.path.isfile('./custumers/' + cpf + '.txt'):
        registration = open('./custumers/' + cpf + '.txt', 'r')
        #transfering each line as a list to the lista list
        for linha in registration.readlines():
            lista.append(linha)
        registration.close()
        # now, i will ask for the password
        senha = input('Digite a senha cadastrada: ')
        # verification if the password is correct
        if senha == lista[4].strip():
            # gambiarra to take the type of the account
            account_type = lista[2].strip()
            account_type.split(' ')
            #the first part of the print
            print('\nNome: {0}\nCPF: {1}\nConta: {2}' .format(lista[0].strip(), lista[1].strip(), lista[2].strip()))
            # now, i will use loops to print every transaction the client ever made
            for p in range(5, len(lista)):
                print('%s' %lista[p].strip())
        else:
            print('Senha incorreta!')
            return

def balance():
    cpf = input('Digite o CPF cadastrado: ')
    lista=[]
    #checking if the cpf is correct
    if os.path.isfile('./custumers/' + cpf + '.txt'):
        registration = open('./custumers/' + cpf + '.txt', 'r')
        #transfering each line as a list to the lista list
        for linha in registration.readlines():
            lista.append(linha)
        registration.close()
        # now, asking the password to keep the task
        senha = input('Digite a senha cadastrada: ')
        #verification if its correct
        if senha == lista[4].strip():
            saldo = float(lista[3].strip())
            print('\nO saldo da sua conta é: %.2f' % saldo)
        #wheter it's not correct, the program will restart the same function, in this case, balance
        else:
            print('Senha Incorreta!')
            return balance()
    else:
        print('CPF errado ou não cadastrado!')
        return

def deposit():
    data_e_hora_atuais = datetime.now()
    data_e_hora_em_texto = data_e_hora_atuais.strftime('%Y-%m-%d %H:%M')
    lista=[]
    cpf = input('\nDigite o CPF cadastrado: ')
    #checking if the cpf is correct
    if os.path.isfile('./custumers/' + cpf + '.txt'):
        registration = open('./custumers/' + cpf + '.txt', 'r')
        for linha in registration.readlines():
            lista.append(linha)
        registration.close()
        #asking the value to be deposited
        deposited_value = float(input('Digite o valor a ser depositado: '))
        balance = float(lista[3].strip()) + deposited_value
        lista.append('\nData {0}   + {1}   Tarifa: 0.00   Saldo: {2}' .format(data_e_hora_em_texto, deposited_value, balance))
        lista[3] = str(balance)+'\n'
        #overwriting the file with the new informations
        registration = open('./custumers/' + cpf + '.txt', 'w')
        for p in range(0,len(lista)):   
            registration.writelines(lista[p])
        registration.close()
        print('\nDepósito realizado com sucesso!')
    else:
        print('CPF incorreto ou não cadastrado!')
        return

def debit():
    data_e_hora_atuais = datetime.now()
    data_e_hora_em_texto = data_e_hora_atuais.strftime('%Y-%m-%d %H:%M')
    account_salary_tax = 1.05
    account_common_tax = 1.97
    account_plus_tax = 1.99    
    lista = []
    cpf = input('\nDigite o seu cpf cadastrado: ')
    senha = input('Digite a sua senha cadastrada: ')
    # making the verification of the cpf, and then, the password
    if os.path.isfile('./custumers/' + cpf + '.txt'):
        # now, im going to check if that really has a line which goes through with the password
        registration = open('./custumers/' + cpf + '.txt', 'r')
        for linha in registration.readlines():
            lista.append(linha)
        registration.close()
        if senha == lista[4].strip():
            valor_debito = float(input('Digite o valor a ser debitado: '))
            account_type = lista[2]
            balance = float(lista[3].strip())
            #salary account
            if account_type == 'Salário\n' and balance - valor_debito > 0:
                tax = (valor_debito*account_salary_tax) - valor_debito  
                balance = balance - (valor_debito*account_salary_tax)
                lista.append('\nData {0}   - {1}   Tarifa: {2}   Saldo: {3}' .format(data_e_hora_em_texto, valor_debito, tax, balance))
                lista[3] = str(balance)+'\n'
                registration = open('./custumers/' + cpf + '.txt', 'w')
                for p in range(0,len(lista)):   
                    registration.writelines(lista[p])
                registration.close()
                print('Débito realizado com sucesso!')
            #commom account
            elif account_type == 'Comum\n' and balance - valor_debito > -500:
                tax = (valor_debito*account_salary_tax) - valor_debito
                balance = balance - (valor_debito*account_common_tax)
                lista.append('\nData {0}   - {1}   Tarifa: {2}   Saldo: {3}' .format(data_e_hora_em_texto, valor_debito, tax, balance))
                registration = open('./custumers/' + cpf + '.txt', 'w')
                lista[3] = str(balance)+'\n'
                for j in range(0,len(lista)):   
                    registration.writelines(lista[j])
                registration.close()
                print('Débito realizado com sucesso!')
            #plus account
            elif account_type == 'Plus\n' and balance - valor_debito > -5000:
                tax = (valor_debito*account_salary_tax) - valor_debito
                balance = balance - (valor_debito*account_plus_tax)
                lista.append('\nData {0}   - {1}   Tarifa: {2}   Saldo: {3}' .format(data_e_hora_em_texto, valor_debito, tax, balance))
                registration = open('./custumers/' + cpf + '.txt', 'w')
                lista[3] = str(balance)+'\n'
                for k in range(0,len(lista)):   
                    registration.writelines(lista[k])
                registration.close()
                print('Débito realizado com sucesso!')
            else:
                print('Tipo de conta não atende aos seus requisitos\n')
    else:
        print('CPF errado ou não cadastrado!')
        return

# ask to remove the registration
def remove_custumer():
    lista = []
    aux = False
    #making sure that what he wants
    print('\nVocê tem certeza que quer apagar a sua conta?')
    print(' 1 - Sim, quero apagar a minha conta\n 0 - Não, não quero apagar a conta')
    yes_or_no = int(input('Digite 0 ou 1: '))
    if yes_or_no == 0:
        return 
    elif yes_or_no == 1:
        # to remove the account, we gonna ask for cpf and password
        cpf = input('Digite o CPF cadastrado: ')
        senha = input('Digite a sua senha: ')
    # the question is, how to check if the cpf and the password are correct?
    # i had thought in a way to read the files
    # making sure that the cpf registrationt really exists
    if os.path.isfile('./custumers/' + cpf + '.txt'):
        # now, im going to check if that really has a line which goes through with the password
        registration = open('./custumers/' + cpf + '.txt', 'r')
        for linha in registration.readlines():
            lista.append(linha)
            for p in range(len(lista)):
                if senha == lista[p].strip():
                    os.remove('./custumers/' + cpf + '.txt')
                    print('\n Conta removida com sucesso!')
                    aux = True
        if aux == False:
            print('Senha inválida')
            remove_custumer()
    else:
        print('CPF inválido ou conta inexistente')
        remove_custumer()
    registration.close()

# new custumer registration
def new_custumer():
    # each input is to get the enough informations to make the complete registration
    name = input('\nDigite o nome: ')
    cpf = input('Digite o CPF(xxxxxxxxxxx): ')
    print('\n-------Tipo de Conta-------')
    print('\n 1 - Conta Salário - cobra taxa de 5% a cada débito realizado, Não permite débitos que deixem a conta com saldo negativo\n 2 - Conta Comum - cobra taxa de 3% a cada débito realizado, Permite um saldo negativo de até (R$ 500,00)\n 3 - Conta Plus - cobra taxa de 1% a cada débito realizado, Permite um saldo negativo de até (R$ 5.000,00)')
    account_type = int(input('\nDigite o número do tipo de conta desejado: '))
    # thinking about assurance that the custumer wont make shit, while the account type havent the right numbers to type the account, the computer will keep asking for a right number
    while account_type < 1 or account_type > 3:
        print('\n 1 - Conta Salário - cobra taxa de 5% a cada débito realizado, Não permite débitos que deixem a conta com saldo negativo\n 2 - Conta Comum - cobra taxa de 3% a cada débito realizado, Permite um saldo negativo de até (R$ 500,00)\n 3 - Conta Plus - cobra taxa de 1% a cada débito realizado, Permite um saldo negativo de até (R$ 5.000,00)')
        account_type = int(input('\nTIPO DE CONTA INVÁLIDO\nDigite o número do tipo de conta desejado: '))
    #initial money input
    balance = float(input('Digite o valor inicial da conta: '))
    #password input
    password = int(input('Cadastre a sua senha: '))
    
    # Verification if the custumer registration already exists
    if os.path.isfile('./custumers/' + cpf + '.txt'):
        print('Cliente já está registrado!')
    # if the client isnt registered, we gonna open a file and put every information we asked for in those inputs
    else:
        custumer_registration = open('custumers/'+cpf+'.txt', 'w')
        custumer_registration.write('%s\n' % name)
        custumer_registration.write('%s\n' % cpf)
        # what type of account the custumer asked for:
        if account_type == 1:
            custumer_registration.write('Salário\n')
        elif account_type == 2:
            custumer_registration.write('Comum\n')
        elif account_type == 3:
            custumer_registration.write('Plus\n')
        custumer_registration.write('%.2f\n' % balance)
        custumer_registration.write('%d' % password)
        custumer_registration.close()
    

def main():
    #just to keep the program alive
    while True:
        #instructions:
        print('\n----------MENU----------')
        print('1 - Novo Cliente')
        print('2 - Apaga Cliente')
        print('3 - Debitar')
        print('4 - Depositar')
        print('5 - Saldo')
        print('6 - Extrato')
        print('\n')
        print('0 - sair')
        #input to ask for what option he wants
        option_input = int(input('\nEscolha uma das opções: '))
        #conditional block to initiate those functions.
        if option_input == 1:
            new_custumer()
        elif option_input == 2:
            remove_custumer()
        elif option_input == 3:
            debit()
        elif option_input == 4:
            deposit()
        elif option_input == 5:
            balance()
        elif option_input == 6:
            bank_statement()
        else:
            break
main()