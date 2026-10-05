import qrcode

while True:
    url = input("Digite sua url (ou 'sair') ").strip()
    if not url:
        print("Sua url está vazia!, escreva alguma")
        continue

    if url.lower() == "sair":
        break

    nome_arquivo = input("Digite o nome que você queira que o arquivo tenha: ").strip()

    if not nome_arquivo:
        print("O nome do seu arquivo esta vazio! escreva um")
        continue

    if not url.startswith("http"):
        url = f"https://{url}"

    imagem = qrcode.make(url)
    imagem.save(f"{nome_arquivo}.png")
    print("QR Code salvo!")
