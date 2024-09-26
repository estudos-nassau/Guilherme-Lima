from models.connection_options.connection import DBConnectionHandler
from models.repository.produtos_repository import ProdutosRepository

db_handle = DBConnectionHandler()
db_handle.connect_to_db()
db_connection = db_handle.get_db_connection()

produtos_repository = ProdutosRepository(db_connection)

response = produtos_repository.select_many({"produto":"console"}) 
print(response)
print()

response2 = produtos_repository.select_one({ "marca": "sony" })
 #print(response2)

# produtos_repository.select_if_property_exists()

produtos_repository.select_many_order()









# insert_document = {
    
#     "produto":"console",
#     "marca":"sony",
#     "preco":"4000.00",

#         "descricao" : {
#         "geracao" : "5",
#         "modelo" : "playstation"
#     }


# }

# produtos_repository.insert_document(insert_document)


# list_of_documents = [

#     { "name": "Guilherme Lima",
#      "endereco": "avenida professor andrade bezerra",
#      "pedido":{
#          "produtos":"smartPhone, console",
#          "marcas":"iphone, sony",
#          "preco":"4000.00 + 4500.00",        
#      },

#      "total":"8500.00"
# },
#     {     "name": "Cleber Gomes",
#      "endereco": "Hipodromo",
#      "pedido":{
#          "produtos":" 2 smartPhone",
#          "marcas":"iphone, iphone",
#          "preco":"4000.00 + 4000.00",        
#      },

#      "total":"8000.00"
# },
#     {     "name": "Hester Almeida",
#      "endereco": "Avenida Jose Rufino",
#      "pedido":{
#          "produtos":"smartPhone, console",
#          "marcas":"xiaomi, microsoft",
#          "preco":"2999.00 + 4000.00",        
#      },

#      "total":"6999.00"
# },
#     {     "name": "Roberta Campos",
#      "endereco": "Corrego do Abacaxi",
#      "pedido":{
#          "produtos":"2 console",
#          "marcas":"microsoft, sony",
#          "preco":"4000.00 + 4500.00",        
#      },

#      "total":"8500.00"
# }


# ]

# pedidos_repository.insert_list_of_documents(list_of_documents)