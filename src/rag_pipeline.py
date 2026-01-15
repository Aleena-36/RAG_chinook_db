from db_connect import get_connection
from load_docs import load_documents
from embeddings import get_embeddings
from chroma_store import create_vector_store
from langchain_openai import ChatOpenAI

docs = load_documents()
embeddings = get_embeddings()
vectorstore = create_vector_store(docs, embeddings)

#Now we create a Retriever
#According to query, find the top-5 most similar vectors-SimilaritySearch
retriever = vectorstore.as_retriever(search_kwargs={"k": 5})

# Load LLM
llm = ChatOpenAI(model="gpt-4o-mini")

def ask(question):
    docs = retriever.get_relevant_documents(question)
    context = "\n".join([d.page_content for d in docs])

    #Generator
    response = llm.invoke(
        f"Answer using only this context:\n{context}\n\nQuestion: {question}"
    )
    return response.content

print(ask("Which tracks are by Queen?"))
