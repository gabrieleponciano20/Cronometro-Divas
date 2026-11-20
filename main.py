import tkinter as tk

class Cronometro:
    def __init__(self, janela):
        self.janela = janela
        self.janela.title("Cronometro")
        self.janela.geometry("520x330")
        self.janela.resizable(False, False)
        self.janela.configure(bg="#faadf3")

        # Variáveis de Estado
        self.tempo_atual = "00:00:00"
        self.segundo = 0
        self.rodando = False
        self.timer_id = None

        # Criar a interface
        self.criar_interface()

    def criar_interface(self):
        # Container Principal
        container = tk.Frame(self.janela, bg="#e601a1")
        container.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)

        # Card Principal
        card = tk.Frame(container, bg="#ffffff", relief="ridge", bd=2)
        card.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)

        # Título
        titulo = tk.Label(
            card,
            text="Cronômetro das Divas",
            font=("Montserrat", 15, "bold"),
            bg="#ffffff",
            fg="#333333",
        )
        titulo.pack(pady=(10, 5))

        # Display Tempo
        self.display_tempo = tk.Label(
            card,
            text=self.tempo_atual,
            font=("Montserrat", 48, "bold"),
            bg="#ffffff",
            fg="#58007A",
        )
        self.display_tempo.pack(pady=10)

        # Frame Botão
        frame_botoes = tk.Frame(card, bg="#ffffff")
        frame_botoes.pack(pady=10)

        # Botão Iniciar
        self.btn_iniciar = tk.Button(
            frame_botoes,
            command=self.iniciar,
            text="Iniciar",
            font=("Montserrat", 10, "bold"),
            bg="#00BE19",
            fg="#e1f0df",
            padx=20,
            pady=8,
            relief="raised",
            bd=2,
            width=10,
        )
        self.btn_iniciar.grid(row=0, column=0, padx=5)

        # Botão Parar
        self.btn_parar = tk.Button(
            frame_botoes,
            command=self.parar,
            text="Parar",
            font=("Montserrat", 10, "bold"),
            bg="#CC001B",
            fg="#ffffff",
            padx=20,
            pady=8,
            relief="raised",
            bd=2,
            width=10,
        )
        self.btn_parar.grid(row=0, column=1, padx=5)

        # Botão Reiniciar
        self.btn_reiniciar = tk.Button(
            frame_botoes,
            command=self.reiniciar,
            text="Reiniciar",
            font=("Montserrat", 10, "bold"),
            bg="#0BBAFF",
            fg="#ffffff",
            padx=20,
            pady=8,
            relief="raised",
            bd=2,
            width=10,
        )
        self.btn_reiniciar.grid(row=0, column=2, padx=5)


# Gatinho deitado no canto inferior direito do card
        self.desenhar_gatinho(card)

    def desenhar_gatinho(self, parent):
        canvas_gato = tk.Canvas(
            parent,
            width=130,
            height=52,
            bg="#ffffff",
            highlightthickness=0,
        )
        canvas_gato.pack(side=tk.BOTTOM, anchor="e", padx=(0, 12), pady=(0, 4))

        cor_gato = "#F4A261"
        cor_detalhe = "#333333"

        # Rabinho curvo
        canvas_gato.create_line(
            98, 38, 118, 34, 122, 22,
            smooth=True, width=4, fill=cor_gato, capstyle=tk.ROUND
        )

        # Corpo deitado (oval horizontal)
        canvas_gato.create_oval(45, 22, 102, 44, fill=cor_gato, outline=cor_gato)

        # Cabeça apoiada na frente
        canvas_gato.create_oval(22, 16, 52, 42, fill=cor_gato, outline=cor_gato)

        # Orelha esquerda e direita
        canvas_gato.create_polygon(25, 21, 28, 8, 35, 18, fill=cor_gato, outline=cor_gato)
        canvas_gato.create_polygon(39, 18, 46, 8, 49, 21, fill=cor_gato, outline=cor_gato)

        # Olhinhos fechados (dormindo/relaxando)
        canvas_gato.create_arc(28, 26, 35, 32, start=180, extent=180, style=tk.ARC, width=1.5, outline=cor_detalhe)
        canvas_gato.create_arc(39, 26, 46, 32, start=180, extent=180, style=tk.ARC, width=1.5, outline=cor_detalhe)

        # Narizinho rosa e bigodes
        canvas_gato.create_polygon(35, 32, 39, 32, 37, 35, fill="#FF758F", outline="#FF758F")
        canvas_gato.create_line(16, 30, 24, 31, fill=cor_detalhe, width=1)
        canvas_gato.create_line(16, 34, 24, 33, fill=cor_detalhe, width=1)
        canvas_gato.create_line(50, 31, 58, 30, fill=cor_detalhe, width=1)
        canvas_gato.create_line(50, 33, 58, 34, fill=cor_detalhe, width=1)


    # Isso aqui é o que vai fazer o cronometro ser funcional
    def atualizar_tempo(self):
        if self.rodando:
            self.segundo += 1
            horas = self.segundo // 3600
            minutos = (self.segundo % 3600) // 60
            segundos = self.segundo % 60
            self.tempo_atual = f"{horas:02d}:{minutos:02d}:{segundos:02d}"
            self.display_tempo.config(text=self.tempo_atual)
            self.timer_id = self.janela.after(1000, self.atualizar_tempo)

    def iniciar(self):
        if not self.rodando:
            self.rodando = True
            self.atualizar_tempo()

    def parar(self):
        self.rodando = False
        if self.timer_id is not None:
            self.janela.after_cancel(self.timer_id)
            self.timer_id = None

    def reiniciar(self):
        self.parar()
        self.segundo = 0
        self.tempo_atual = "00:00:00"
        self.display_tempo.config(text=self.tempo_atual)

if __name__ == "__main__":
    janela = tk.Tk()
    app = Cronometro(janela)
    janela.mainloop()
   
                         
