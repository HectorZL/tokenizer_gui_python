# logic.py
import os
from transformers import AutoTokenizer

# Load the pre-trained tokenizer
tokenizer = AutoTokenizer.from_pretrained('bert-base-uncased')

def clean_tokens(tokens):
    """Cleans subword tokens by removing the '##' prefix and joining words."""
    cleaned_text = ''
    for token in tokens:
        if token.startswith('##'):
            cleaned_text += token[2:]  # Append without '##' if it's a subword
        else:
            cleaned_text += ' ' + token  # Start a new word with a space
    return cleaned_text.strip()

def count_tokens(archivo):
    """Counts the tokens in a file using the tokenizer."""
    with open(archivo, 'r', encoding='utf-8') as f:
        texto = f.read()
    
    tokens = tokenizer.tokenize(texto)
    return len(tokens)

def dividir_archivo(archivo, tokens_por_archivo=512, tokens_por_grupo=7500):
    """Splits the file into smaller files with a specified number of tokens per file."""
    with open(archivo, 'r', encoding='utf-8') as f:
        texto = f.read()
    tokens = tokenizer.tokenize(texto)
    num_tokens = len(tokens)

    if num_tokens <= tokens_por_archivo:
        print(f"El archivo tiene {num_tokens} tokens, no es necesario dividirlo.")
        return

    # Create initial chunks
    initial_chunks = [tokens[i:i + tokens_por_archivo] for i in range(0, num_tokens, tokens_por_archivo)]
    print(f"Initial chunks created: {len(initial_chunks)} chunks of {tokens_por_archivo} tokens each.")

    # Group initial chunks into larger groups
    grouped_tokens = []
    current_group = []

    for chunk in initial_chunks:
        current_group.extend(chunk)
        if len(current_group) >= tokens_por_grupo:
            grouped_tokens.append(current_group[:tokens_por_grupo])
            current_group = current_group[tokens_por_grupo:]

    if current_group:
        grouped_tokens.append(current_group)

    # Save each group to a file
    for i, group in enumerate(grouped_tokens, start=1):
        # Clean tokens in each group before saving
        cleaned_text = clean_tokens(group)
        nombre_archivo = os.path.splitext(archivo)[0] + f"_group_{i}.txt"
        
        with open(nombre_archivo, 'w', encoding='utf-8') as f:
            f.write(cleaned_text)
        
        print(f"Archivo {nombre_archivo} creado con {len(group)} tokens.")

    print(f"Total de archivos creados: {len(grouped_tokens)} archivos de hasta {tokens_por_grupo} tokens cada uno.")
