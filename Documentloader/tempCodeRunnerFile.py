from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(file_path='social_network.csv', encoding='utf-8', csv_args={'delimiter': ','})

docs = loader.load()

print(len(docs))
print(docs[1])