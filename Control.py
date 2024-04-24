from Exercicios import Exercicios

class Control:
    def __init__(self):
        self.opcao = -1
        self.exer = Exercicios()




    def coletar(self):
        self.exer.num1 = int(input("Informe o primeiro número: "))
        self.exer.num2 = int(input("Informe o segundo número: "))

    def menu(self):
        self.opcao = int(input("-------Menu-------\n\n"+
              "\n0. Sair"             +
              "\n1. Somar"            +
              "\n2. Subtrair"         +
              "\n3. Dividir"          +
              "\n4. Multiplicar"      +
              "\n5. Exercicio 1"      +
              "\n6. Exercicio 2"      +
              "\n7. Exercicio 3"      +
              "\n8. Exercicio 4"      +
              "\n9. Exercicio 5"      +
              "\n10. Exercicio 6"     +
              "\n11. Exercicio 7"     +
              "\n12. Exercicio 8"     +
              "\n13. Exercicio 9"     +
              "\n14. Exercicio 10"    +
              "\n15. Exercicio 11"    +
              "\n16. Exercicio 12"    +
              "\n17. Exercicio 13"    +
              "\n18. Exercicio 14"    +
              "\n19. Exercicio 15"    +
              "\n20. Exercicio 16"    +
              "\n21. Exercicio 17"    +
              "\n22. Exercicio 18"    +
              "\n23. Exercicio 19"    +
              "\n24. Exercicio 20"    +
              "\nEscolha uma das opções acima: "))

    def operacao(self):
        while(self.opcao !=0):
            self.menu() #Mostrando o menu
            if(self.opcao == 0):
                print("Obrigado!")
            elif(self.opcao == 1):
                self.coletar()
                print(self.exer.somar())
            elif(self.opcao == 2):
                self.coletar()
                print(self.exer.subtrair())
            elif (self.opcao == 3):
                self.coletar()
                print(self.exer.dividir())
            elif (self.opcao == 4):
                self.coletar()
                print(self.exer.multiplicar())
            elif (self.opcao == 5):
                print(self.exer.ex1())
            elif (self.opcao == 6):
                print(self.exer.ex2())
            elif (self.opcao == 7):
                print(self.exer.ex3())
            elif (self.opcao == 6):
                print(self.exer.ex2())


            else:
                print("Código escolhido não é válido!")




