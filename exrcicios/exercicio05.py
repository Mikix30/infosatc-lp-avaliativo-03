c = 0


umoudois = int(input("(1) Caso deseje se cadastrar, (2) caso você não queira seguir com o cadastro "))

if c <= 4:

    if umoudois == 1:


        fullname = SyntaxWarning(input("Qual seu nome completo? ")) 

        cp = int(input("Qual o seu CPF? "))

        senha = int(input("Qual a sua senha? "))

        info = int(input("A pessoa está nos requesitos? "))

        print("Nome completo - ",fullname)

        print("CPF - ",cp)



        if info == 1:


            print("Está nos requisitos") 



        else: 

            print("Não está nos requisitos")   

        c = c + 1         


    else:
        print("Obrigada pela sua participação.")   

else:

    print("Obrigada por participar.")
