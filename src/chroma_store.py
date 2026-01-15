#we store docs, their embeddings and vectors here and call the embedding function to store the embeddings here too

from langchain_community.vectorstores import Chroma

CHROMA_PATH = "chroma"

def create_vector_store(docs, embeddings):
    db = Chroma.from_documents(
        docs,
        embeddings,
        persist_directory=CHROMA_PATH
    )
    db.persist() #save db
    return db
