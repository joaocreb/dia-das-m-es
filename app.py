from datetime import datetime

def criar_cartao(nome_mae,mensagem):

    data = datetime.now().strftime("%d/%m/%y")

    with open("template.html", "r", encoding="utf-8") as arquivo:
        html = arquivo.read()

    html = html.replace("{nome}", nome_mae)
    html = html.replace("{mensagem}", mensagem)
    html = html.replace("{data}", data)

    with open("cartao.html", "w", encoding="utf-8") as arquivo:
        arquivo.write(html)

    print("\n❤ Cartão criado com sucesso!")
    print("abra o arquivo cartao.html no navegaor.")

def main():

        print("🌹 GERADOR DE CARTÃO. 🌹")

        nome = input("Digite o nome da sua mãe:")

        mensagem = input("Digite uma mensagem ")

        criar_cartao(nome, mensagem)

main()