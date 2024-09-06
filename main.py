import tkinter as tk

# Classe principal da calculadora
class Calculadora:
    def __init__(self):
        self.resultado = 0
        self.operacao = ''
        self.ultimo_valor = 0
        self.historico = []  # Lista para armazenar o histórico de operações

    def calcular(self, operacao, a, b):
        if operacao == '+':
            resultado = a + b
        elif operacao == '-':
            resultado = a - b
        elif operacao == '*':
            resultado = a * b
        elif operacao == '/':
            if b == 0:
                return 'Erro: Divisão por zero'
            resultado = a / b
        else:
            return 'Operação inválida'

        self.armazena_historico(operacao, a, b, resultado)
        return resultado

    def armazena_historico(self, operacao, a, b, resultado):
        # Formata a string do cálculo e adiciona ao histórico
        operacao_str = f"{a} {operacao} {b} = {resultado}"
        self.historico.append(operacao_str)

    def reset(self):
        self.resultado = 0
        self.operacao = ''
        self.ultimo_valor = 0
        self.historico.clear()  # Limpa o histórico ao resetar

    def obter_historico(self):
        return "\n".join(self.historico)  # Retorna o histórico como uma única string


# Classe para gerenciar a interface gráfica
class CalculadoraGUI:
    def __init__(self, root):
        self.calc = Calculadora()
        self.janela = root
        self.janela.title("Calculadora")
        self.display = tk.Entry(self.janela, width=20, font=("Arial", 24), borderwidth=2, relief="solid")
        self.display.grid(row=0, column=0, columnspan=4)
        self.criar_botoes()
        self.criar_area_historico()

    def criar_botoes(self):
        botoes = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3)
        ]

        for (texto, linha, coluna) in botoes:
            botao = tk.Button(self.janela, text=texto, width=5, height=2, font=("Arial", 18),
                              command=lambda t=texto: self.on_click(t))
            botao.grid(row=linha, column=coluna)

    def criar_area_historico(self):
        # Cria uma área de texto para exibir o histórico de operações
        self.area_historico = tk.Text(self.janela, height=6, width=30, font=("Arial", 12), state='disabled')
        self.area_historico.grid(row=5, column=0, columnspan=4)

    def on_click(self, texto):
        if texto in '0123456789':
            self.display.insert(tk.END, texto)
        elif texto in '+-*/':
            self.calc.operacao = texto
            self.calc.ultimo_valor = float(self.display.get())
            self.display.delete(0, tk.END)
        elif texto == '=':
            valor_atual = float(self.display.get())
            resultado = self.calc.calcular(self.calc.operacao, self.calc.ultimo_valor, valor_atual)
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, resultado)
            self.atualizar_historico()
        elif texto == 'C':
            self.calc.reset()
            self.display.delete(0, tk.END)
            self.atualizar_historico()

    def atualizar_historico(self):
        # Atualiza a área de histórico com as operações realizadas
        self.area_historico.config(state='normal')
        self.area_historico.delete(1.0, tk.END)
        self.area_historico.insert(tk.END, self.calc.obter_historico())
        self.area_historico.config(state='disabled')


if __name__ == "__main__":
    root = tk.Tk()
    app = CalculadoraGUI(root)
    root.mainloop()
