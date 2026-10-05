import os
import tkinter as tk
from tkinter import ttk, filedialog
import qrcode
from PIL import Image, ImageTk


def escolher_pasta():
    escolhida = filedialog.askdirectory()
    if escolhida:
        pasta.set(escolhida)


def gerar(event=None):
    url = caixa_url.get().strip()
    nome = caixa_nome.get().strip()

    if not url:
        mensagem.config(text="Digite o link!", foreground="red")
        return
    if not nome:
        mensagem.config(text="Digite o nome do arquivo!", foreground="red")
        return

    if not url.startswith("http"):
        url = f"https://{url}"

    caminho = os.path.join(pasta.get(), f"{nome}.png")
    imagem = qrcode.make(url)
    imagem.save(caminho)

    foto = Image.open(caminho).resize((250, 250))
    foto_tk = ImageTk.PhotoImage(foto)
    area_qr.config(image=foto_tk)
    area_qr.image = foto_tk

    mensagem.config(text=f"Salvo em: {caminho}", foreground="green")
    caixa_url.delete(0, tk.END)
    caixa_nome.delete(0, tk.END)
    caixa_url.focus()


janela = tk.Tk()
janela.title("Gerador de QR Code")
janela.resizable(False, False)

pasta = tk.StringVar(value=os.path.expanduser("~"))

quadro = ttk.Frame(janela, padding=20)
quadro.pack()

ttk.Label(quadro, text="Gerador de QR Code", font=("Helvetica", 20, "bold")).pack(pady=(0, 15))

ttk.Label(quadro, text="Link do site").pack(anchor="w")
caixa_url = ttk.Entry(quadro, width=40)
caixa_url.pack(fill="x", pady=(2, 10))

ttk.Label(quadro, text="Nome do arquivo").pack(anchor="w")
caixa_nome = ttk.Entry(quadro, width=40)
caixa_nome.pack(fill="x", pady=(2, 10))

ttk.Label(quadro, text="Salvar na pasta").pack(anchor="w")
ttk.Label(quadro, textvariable=pasta, wraplength=300).pack(anchor="w")
ttk.Button(quadro, text="Escolher pasta...", command=escolher_pasta).pack(anchor="w", pady=(2, 15))

ttk.Button(quadro, text="Gerar QR Code", command=gerar).pack(fill="x")

mensagem = ttk.Label(quadro, text="")
mensagem.pack(pady=10)

area_qr = ttk.Label(quadro)
area_qr.pack()

caixa_url.bind("<Return>", gerar)
caixa_nome.bind("<Return>", gerar)
caixa_url.focus()

janela.mainloop()
