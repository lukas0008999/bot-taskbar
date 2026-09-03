import tkinter as tk
from tkinter import ttk
import pyautogui
import time
import threading

# Configurações iniciais
pyautogui.FAILSAFE = True

# Variável de controle
executando = False

def aguardar_e_clicar(nome_imagem, mensagem, quantidade_clicks):
    """Função que aguarda até encontrar a imagem na tela e clica."""
    global executando
    print(f"Aguardando: {mensagem}...")

    while executando:
        try:
            posicao = pyautogui.locateCenterOnScreen(f"{nome_imagem}.png", confidence=0.95)
            if posicao:
                print(f"Encontrado {mensagem}, clicando...")
                if quantidade_clicks == 1:
                    pyautogui.click(posicao)
                elif quantidade_clicks == 2:
                    pyautogui.doubleClick(posicao)
                return True
        except:
            pass
        time.sleep(0.5)
    return False

def rodar_bot():
    global executando
    while executando:
        passos = [
            ("1-9", "Foto 1-9", 2, 4),
            ("blue", "Blue", 0, 2),
            ("act3", "Act 3", 2, 2),
            ("3-5", "Foto 3-5", 2, 2),
            ("blue", "Blue", 0, 2),
            ("nightmare", "Nightmare", 2, 2),
            ("hell", "Hell", 2, 2),
            ("act2", "Act 2", 2, 2),
            ("2-7", "Foto 2-7", 2, 2),
            ("blue", "Blue", 0, 2),
            ("hell2", "Hell2", 2, 2),
            ("nightmare2", "Nightmare2", 2, 2),
            ("act1", "Act 1", 2, 2)
        ]
        for img, msg, clicks, espera in passos:
            if not executando: break
            if aguardar_e_clicar(img, msg, clicks):
                time.sleep(espera)
            else:
                break
        if executando:
            aguardar_e_clicar("1-9", "Foto 1-9", 2)

def iniciar():
    global executando
    executando = True
    btn_iniciar.config(state="disabled")
    btn_parar.config(state="normal")
    status_label.config(text="RODANDO", foreground="#00ff9d")
    threading.Thread(target=rodar_bot, daemon=True).start()

def parar():
    global executando
    executando = False
    btn_iniciar.config(state="normal")
    btn_parar.config(state="disabled")
    status_label.config(text="PARADO", foreground="#ff4d4d")

# --- Interface Gráfica Estilizada ---
root = tk.Tk()
root.title("TaskBarHero - Bot Control")
root.geometry("320x380")
root.configure(bg="#1a1a1a")

# Estilos
style = ttk.Style()
style.theme_use('clam')
style.configure("TLabel", background="#1a1a1a", foreground="#ffffff", font=("Segoe UI", 10))

# Título
tk.Label(root, text="TASKBAR HERO", font=("Orbitron", 18, "bold"), bg="#1a1a1a", fg="#00d4ff").pack(pady=25)

# Painel de Status
tk.Label(root, text="STATUS DO BOT:", font=("Segoe UI", 8, "bold"), bg="#1a1a1a", fg="#888").pack()
status_label = tk.Label(root, text="PARADO", font=("Segoe UI", 14, "bold"), bg="#1a1a1a", fg="#ff4d4d")
status_label.pack(pady=5)

# Botões
btn_frame = tk.Frame(root, bg="#1a1a1a")
btn_frame.pack(pady=30)

btn_iniciar = tk.Button(btn_frame, text="INICIAR", command=iniciar, bg="#008c5a", fg="white",
                        font=("Segoe UI", 10, "bold"), width=12, relief="flat", activebackground="#005e3b")
btn_iniciar.pack(pady=10)

btn_parar = tk.Button(btn_frame, text="PARAR", command=parar, bg="#8c1c1c", fg="white",
                      font=("Segoe UI", 10, "bold"), width=12, relief="flat", state="disabled", activebackground="#5e1212")
btn_parar.pack(pady=10)

root.mainloop()