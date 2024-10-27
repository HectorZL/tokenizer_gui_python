import spacy
from excepciones import IdiomaNoSoportadoError, ModeloNoEncontradoError  # Add this line

# Carga de modelos en inglés y español
try:
    nlp_en = spacy.load("en_core_web_sm")
    nlp_es = spacy.load("es_core_news_sm")
except OSError:
    raise ModeloNoEncontradoError("No se encuentran los modelos de Spacy necesarios. Instálalos con 'python -m spacy download en_core_web_sm' y 'python -m spacy download es_core_news_sm'.")

# Carga de modelos en inglés y español
try:
    nlp_en = spacy.load("en_core_web_sm")
    nlp_es = spacy.load("es_core_news_sm")
except OSError:
    raise ModeloNoEncontradoError(
        "No se encuentran los modelos de Spacy necesarios. "
        "Instálalos con 'python -m spacy download en_core_web_sm' "
        "y 'python -m spacy download es_core_news_sm'."
    )

def count_tokens(text, language="english"):
    """Cuenta tokens en el idioma especificado."""
    if language == "english":
        doc = nlp_en(text)
    elif language == "spanish":
        doc = nlp_es(text)
    else:
        raise IdiomaNoSoportadoError("Idioma no soportado: elige 'english' o 'spanish'.")
    tokens = [token.text for token in doc]
    return len(tokens), tokens

def divide_text(text, max_tokens=7500, language="english"):
    """Divide el texto en partes según el máximo de tokens especificado."""
    if language == "english":
        doc = nlp_en(text)
    elif language == "spanish":
        doc = nlp_es(text)
    else:
        raise IdiomaNoSoportadoError("Idioma no soportado: elige 'english' o 'spanish'.")

    tokens = [token.text for token in doc]
    parts = [tokens[i:i + max_tokens] for i in range(0, len(tokens), max_tokens)]
    divided_texts = [" ".join(part) for part in parts]
    return divided_texts
