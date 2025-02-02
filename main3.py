import tkinter as tk
import speech_recognition as sr
from src.frontend.screens.chat_screen import ChatScreen

screen = ChatScreen()
screen.render()

# Função para capturar a voz e exibir no campo de texto
# def capturar_voz():
#   print('voz capturada')

# # Configuração da janela principal
# root = tk.Tk()
# root.title("Reconhecimento de Voz com Tkinter")

# # Configuração do campo de texto para mostrar o que foi reconhecido
# texto_voz = tk.Text(root, height=5, width=40)
# texto_voz.pack(padx=10, pady=10)

# # Botão para iniciar a captura de voz
# botao_voz = tk.Button(root, text="Falar", command=capturar_voz, height=2, width=10)
# botao_voz.pack(pady=10)

# # Label para mostrar o status
# status_label = tk.Label(root, text="Pronto para ouvir...", font=("Arial", 12))
# status_label.pack(pady=10)

# # Inicia a interface gráfica
# root.mainloop()
