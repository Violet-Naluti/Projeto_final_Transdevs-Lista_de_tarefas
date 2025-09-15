def adicionar_tarefa(lista_de_tarefas, tarefa):
    """Adiciona nova tarefa a uma lista pré-existente"""
    lista_de_tarefas.append(tarefa)
    print(f"{"-"*50}")
    print("Tarefa acidionada com sucesso!")
    return lista_de_tarefas

def listar_tarefas(lista_de_tarefas):
    """Exibe lista de tarefas numerada"""
    print("Lista de Tarefas: ")
    n = 1
    print("*"*50)
    print("Gotta:")
    print("-"*50)
    for tarefa in lista_de_tarefas:
            print(f"{n} - {tarefa}")
            n+=1
    print("-"*50)

def deletar_tarefa(lista_de_tarefas, tarefa):
    """Deleta tarefa de uma lista pré-existente a partir do index dela"""
    lista_de_tarefas.pop((tarefa-1))
    print("-"*10)
    print("Tarefa deletada com sucesso!")
    return(lista_de_tarefas)

def exibir_menu():
    """Exibe menu de opções para usuárie"""
    print("\nEscolha uma opcao:\n" \
        "1 - Inserir nova tarefa\n"\
        "2 - Listar tarefas\n" \
        "3 - Deletar tarefa\n"\
        "4 - Sair")     
    print(f"{'-'*50}")
    print("\n")


#Inicialização de variáveis    
lista_de_tarefas = []
continuar = True

#cabeçalho do programa
print("-"*50)
print ("Inciando a Lista de Tarefas")
print("-"*50)

#Loop principal
while continuar:
    exibir_menu()    
    opcao =input("Insira o que deseja fazer: \n")
    print(f"{'-'*50}")

    if opcao =="1":
        tarefa = input ('Insira uma nova tarefa: ')
        lista_de_tarefas = adicionar_tarefa(lista_de_tarefas, tarefa)
    elif opcao == "2":
        listar_tarefas(lista_de_tarefas)
    elif opcao=="3":
        # A validação verifica se o valor é numérico e se está dentro do limite da lista
        tarefa=input("Insira o número da tarefa que deseja deletar: ")
        if not tarefa.isnumeric():
            print("Número inválido! Tente novamente.")    
        elif int(tarefa) > len(lista_de_tarefas) or int(tarefa)<=0:
            print("Número inválido! Tente novamente.")
        else:
            deletar_tarefa(lista_de_tarefas, int(tarefa))
    elif opcao =="4":
        continuar = False
    
    else:
        print("Opção inválida! Tente novamente")
    print("\n")
