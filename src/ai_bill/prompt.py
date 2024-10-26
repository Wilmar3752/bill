from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "Eres un algoritmo experto en extraccion de datos de facturas en pdf"
            "Solo extraes informacion relevante del texto"
            "si no conoces el atributo a extraer, "
            "retorna null en el valor del atributo.",
        ),
        # Please see the how-to about improving performance with
        # reference examples.
        # MessagesPlaceholder('examples'),
        ("human", "{text}"),
    ]
)
