from pymongo import MongoClient #importa a biblioteca pymongo que oferece diversos comandos e serviçoes para integrar o python ao mongodb

#cria uma string de conexão (linka o programa ao servidor a partir da string de conexão)
connection_string = "mongodb://localhost:27017/"
client = MongoClient(connection_string)
#referencia o banco a partir do client
db_connection = client["ecomerce"]

print(db_connection)
print()

#seleciona a collection que você deseja verificar/modificar
collection = db_connection.get_collection("pedidos")
#toda modificação que for feita após a collection será adicionada/alterada nessa collection
print(collection)
print()

search_filter = {

    "marca" : "iphone"
                 
}

#realiza um filtro e cria uma variavel "response" que recebe a função collection.find. A função recebe o parametro que representa o filtro "(search_filter)"
response = collection.find(search_filter)
print(response)

for registry in response: print(registry)

#fazer as inserções no db
collection.insert_one({

    "produto":"smartPhone",
    "marca":"iphone",
    "preco":"4000.00"

})