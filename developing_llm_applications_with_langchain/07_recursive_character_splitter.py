from langchain.text_splitter import RecursiveCharacterTextSplitter

qoute = 'One machine can do the work of fifty ordinary humans. No machine can do the work of one extraordinary human.'

chunk_size = 24
chunk_overlap = 3

recursive_character_splitter = RecursiveCharacterTextSplitter( 
                                    chunk_size=chunk_size,
                                    chunk_overlap=chunk_overlap
                                )

splits = recursive_character_splitter.split_text(qoute)
print(splits)