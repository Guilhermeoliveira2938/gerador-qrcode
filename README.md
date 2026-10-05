# 📱 Gerador de QR Code

Programa simples que gera um **QR Code** (imagem `.png`) a partir de um link.

Tem duas versões:

| Arquivo | O que é |
|---|---|
| `app.py` | Versão com **janela**: digite o link e o nome do arquivo, escolha a pasta e veja o QR Code na tela |
| `qr.py` | Versão de **terminal**, mais simples (digite `sair` para encerrar) |

Se o link não começar com `http`, o programa coloca `https://` sozinho.

## ⬇️ Baixar o programa para Windows (sem instalar nada)

1. Abra a aba [**Releases**](../../releases) deste repositório.
2. Na versão mais recente, baixe o arquivo **`Gerador QR Code.exe`**.
3. Dê duplo clique para abrir.

### ⚠️ Avisos importantes

- **Tela azul do Windows (SmartScreen):** ao abrir, pode aparecer *"O Windows protegeu o seu PC"*. É porque o programa não tem uma assinatura digital paga. Clique em **Mais informações** e depois em **Executar assim mesmo**.
- **Antivírus:** alguns antivírus podem reclamar de programas `.exe` feitos com PyInstaller. É um alarme falso conhecido. O código-fonte está todo neste repositório para você conferir.

## ▶️ Rodar pelo código (Mac, Linux ou Windows)

1. Instale o [Python 3](https://www.python.org/downloads/).
2. Instale as dependências:
   ```bash
   pip install "qrcode[pil]"
   ```
3. Rode a versão com janela:
   ```bash
   python3 app.py
   ```
   ou a versão de terminal:
   ```bash
   python3 qr.py
   ```

> No Windows, use `python` no lugar de `python3`.

## 🤖 Como o .exe é gerado

O arquivo `.exe` é criado automaticamente pelo **GitHub Actions** (arquivo `.github/workflows/build-windows.yml`) em um computador Windows na nuvem, usando o [PyInstaller](https://pyinstaller.org/). Ao criar uma tag de versão (por exemplo `v1.0`), o `.exe` é anexado à aba Releases.

## 🧰 Tecnologias

- Python 3
- [qrcode](https://pypi.org/project/qrcode/) e [Pillow](https://pypi.org/project/pillow/)
- Tkinter
- PyInstaller + GitHub Actions
