import json

def descobrir_linguagem_json(caminho_arquivo, linguagem):

        with open(caminho_arquivo) as arquivo:
            dados = json.load(arquivo)
        
        dados_str = json.dumps(dados)
        

        if linguagem in dados_str:
            return "Sim"
        else:
            return "Não"
    

caminho_arquivo = "database.json"  
linguagem = input("digite um curso/tecnologia que deseja aprender:")


resultado = descobrir_linguagem_json(caminho_arquivo, linguagem.lower())
print(f"Você pode aprender {linguagem} conosco {resultado}!")
