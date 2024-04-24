
class Exercicios:
    def __init__(self):
        # Construtor
        self.num1 = 0
        self.num2 = 0
        self.numRes = ""

    def somar(self):
       return f"{self.num1} + {self.num2} = {self.num1 + self.num2}"

    def subtrair(self):
        return f"{self.num1} - {self.num2} = {self.num1 - self.num2}"

    def dividir(self):
       if(self.num2 == 0):
            return "Impossível dividir por zero!"
        else:
            return f"{self.num1} / {self.num2} = {self.num1 / self.num2}"

    def multiplicar(self):

        return f"{self.num1} * {self.num2} = {self.num1 * self.num2}"


    #Exercicio 1 - Faça um programa que imprima os números 1 a 10.
    def ex1(self):
        for i in range(1,11,1):
            self.numRes += f"{i}",

        return self.numRes


    #Exercício 2 - Faça um programa que imprima os números pares de 1 ao 20.
    def ex2(self):
        for i in range(2,21,2):
            self.numRes += f"{i}",

        return self.numRes

    #Exercício 3 - Faça um programa que calcule a soma dos números de 1 a 100.
    def ex3(self):
        for i in range(1,101,1):
            self.num1 += i

        return self.num1

    #Exercicio 4- Faça um programa que imprima os multiplos de 5 de 1 a 50.
    def ex4(self):
        for i in range (1,51,1):
            if(i % 5 == 0):
                self.numRes += f"{i}",

        return self.numRes

    #Exercicio 5- Faça um programa que peça ao usuário um número e imprima se ele é Par ou Impar.
    def ex5(self):
        if (self.num1 % 2 ==0):
            return "Par"
        else:
            return "Impar"
    #Exercício 6-Faça um programa que peça ao usuário um numero e imprima se é positivo, negativo ou zero.
    def ex6(self):
        if(self.num1 > 0):
            return "Positivo"
        elif(self.num1< 0):
            return"Negativo"
        else:
            return"zero"
    #Exercicio Faca um programa que peça ao usuário um número   e imprima a tabuada desse número

    def ex07(self):
        self.numRes =""

        for i in range (0,11,1):
            self.numRes +=f"{self.num1} * {i} = {self.num1 * i}\n"

        return f"tabuada do {self.num1}:\n{self.numRes}"
    def ex08(self):
        self.numRes=""



