from typing import Dict, List

class ProdutosRepository:
    def __init__(self,db_connection) -> None:
        self.__collection_name = "produtos"
        self.__db_connection = db_connection

    def insert_document(self, document: Dict) -> Dict:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.insert_one(document)
        return document
    
    def insert_list_of_documents(self, list_of_documents: List[Dict]) -> List[Dict]:

        list_of_documents[list_of_documents]

        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.insert_many(list_of_documents)
        return list_of_documents

    def select_many(self, filter) -> list[Dict]:
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.find(
            filter, # Filtro
            {"_id": 0} #serve para inibir algum dado de aparecer na pesquisa, nesse caso, o id
        )
        
        response = []
        for elem in data: response.append(elem)
        return response
    
    def select_one(self, filter) -> Dict:
        collection = self.__db_connection.get_collection(self.__collection_name)
        response = collection.find_one(filter, {"_id" : 0})
        return response
    
    def select_if_property_exists(self) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.find({"descricao":{"$exists":True}})
        for elem in data: print(elem)

    def select_many_order(self):
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.find(
            { "marca": "sony" }, # Filtro
            {"_id": 0} #serve para inibir algum dado de aparecer na pesquisa, nesse caso, o id
        ).sort([("preco", 1)])
        
        response = []
        for elem in data: print(elem)

