
class Calculadora:
    def __init__(self, operacao, a, b):                             #  #     ###      #####     #   #
        self._resultado = 0                                         # #    #     #    #    #    ##  # 
        self._operacao = operacao                                   ##     #     #    # ###     # # #
        self._a = a                                                 # #    #     #    #   #     #  ##
        self._b = b                                                 #  #     ###      #    #    #   #
    
    def somar(self):
        self._resultado = self._a + self._b

    def subtrair(self):
        self._resultado = self._a - self._b

    def multiplicar(self):
        self._resultado = self._a * self._b

    def dividir(self):
        self._resultado = self._a / self._b

    def get_resultado(self):
        if self._operacao == 1:
            self.somar()
        elif self._operacao == 2:
            self.subtrair()
        elif self._operacao == 3:
            self.multiplicar()
        elif self._operacao == 4:
            self.dividir()
        else:
            print("nao deu.")
        return self._resultado

    def reset(self):
        self._resultado = 0


operacao = int(input("Digite a operação (1. +, 2. -, 3. *, 4. /): "))
a = float(input("Digite o valor A: "))
b = float(input("Digite o valor B: "))
calc = Calculadora(operacao, a, b)

print(calc.get_resultado())  # Saída: 6.0
calc.reset()