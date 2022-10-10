
opc=str(input("Escolha qual operação você deseja realizar:\n 1-SOMA \n 2-SUBTRAÇÃO \n 3-MULTICAÇÃO \n 4-DIVISÃO. \n Digite: "))
while opc == "1" or opc == "SOMA" or opc == "soma" or opc == "2" or opc == "SUBTRAÇÃO" or opc =="subtração" or opc=="3" or opc=="MULTIPLICAÇÃO" or opc=="multiplicação" or opc=="4" or opc=="DIVISÃO" or opc=="divisão":
    if opc == "1" or opc == "SOMA" or opc == "soma":
        n1=float(input("Informe o primeiro número: "))
        n2=float(input("Informe o segundo número número: "))
        adicao=n1+n2
        print(adicao)
    elif opc == "2" or opc == "SUBTRAÇÃO" or opc =="subtração":
        n1=float(input("Informe o primeiro número: "))
        n2=float(input("Informe o segundo número: "))
        subtracao=n1-n2
        print(subtracao)
    elif opc=="3" or opc=="MULTIPLICAÇÃO" or opc=="multiplicação":
        n1=float(input("Informe o primeiro número: "))
        n2=float(input("Informe o segundo número: "))
        multiplicacao=n1*n2
        print(multiplicacao)
    else:
        n1=float(input("Informe o primeiro número: "))
        n2=float(input("Informe o segundo número: "))
        divisao=n1/n2
        print(divisao)
else:
    print("Operação inválida. \n por favor insira a opção correta descrita na tabela. ")

    
