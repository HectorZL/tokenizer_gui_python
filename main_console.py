import os

def dividir_archivo(archivo, tokens_por_archivo=7500):
    # Lee el archivo y cuenta los tokens
    with open(archivo, 'r') as f:
        texto = f.read()

    tokens = texto.split()
    num_tokens = len(tokens)

    if num_tokens <= tokens_por_archivo:
        print(f"El archivo tiene {num_tokens} tokens, no es necesario dividirlo.")
        return  # No se divide si no es necesario

    # Si necesita dividir
    num_archivos = -(-num_tokens // tokens_por_archivo)  # Redondea hacia arriba

    for i in range(num_archivos):
        # Definir el rango de tokens para el archivo actual
        inicio = i * tokens_por_archivo
        fin = min((i + 1) * tokens_por_archivo, num_tokens)
        
        # Extraer el segmento de tokens para el archivo actual
        tokens_slice = tokens[inicio:fin]
        
        # Crear un nuevo archivo con el segmento de tokens
        nombre_archivo = os.path.splitext(archivo)[0] + f"_{i+1}.txt"
        with open(nombre_archivo, 'w') as f:
            f.write(' '.join(tokens_slice))

        print(f"Archivo {nombre_archivo} creado con {len(tokens_slice)} tokens.")

# Ejemplo de uso
dividir_archivo('conferencia6.txt')
