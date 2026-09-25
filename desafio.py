# Entrada de dados
nome = input("Nome completo: ")
idade = int(input("Idade: "))
cpf = input("CPF: ")


print("\nEscolha sua escolaridade:")
print("1 - Ensino Médio")
print("2 - Ensino Superior")
print("3 - Pós-graduação")
opcao_escolaridade = int(input("Digite a opção: "))

if idade < 18:
    print("\nInscrição não permitida.")
    print("O candidato precisa ter 18 anos ou mais.")
    status = "INSCRIÇÃO COM PENDÊNCIAS"
else:
    idade;

if opcao_escolaridade == 1:
        escolaridade = "Ensino Médio"
elif opcao_escolaridade == 2:
        escolaridade = "Ensino Superior"
elif opcao_escolaridade == 3:
        escolaridade = "Pós-graduação"
else:
        escolaridade = "Escolaridade inválida"

sexo = input("\nSexo (M/F): ").upper()

if sexo == "M":
        documento = "Certificado de Reservista"
elif sexo == "F":
        documento = "Não há necessidade de documento militar"
else:
        documento = "Sexo inválido"

print("\nEscolha a área desejada:")
print("1 - Administração")
print("2 - Tecnologia da Informação")
print("3 - Educação")

opcao_area = int(input("Digite a opção: "))

if opcao_area == 1:
        area = "Administração"
        cargo = "Analista Administrativo"
elif opcao_area == 2:
        area = "Tecnologia da Informação"
        cargo = "Analista de Sistemas"
elif opcao_area == 3:
        area = "Educação"
        cargo = "Professor"
else:
        area = "Área inválida"
        cargo = "Cargo não definido"

if (escolaridade != "Escolaridade inválida"
            and sexo in ["M", "F"]
            and area != "Área inválida"):
        status = "INSCRIÇÃO APROVADA"
else:
        status = "INSCRIÇÃO COM PENDÊNCIAS"

print("Nome:", nome)
print("CPF:", cpf)
print("Idade:", idade)
print("Escolaridade:", escolaridade)
print("Área profissional:", area)
print("Cargo:", cargo)
print("Documento adicional:", documento)
print("Status:", status)

