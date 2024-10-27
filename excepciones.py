# excepciones.py

class ModeloNoEncontradoError(Exception):
    """Excepción personalizada para cuando no se encuentran modelos de Spacy necesarios."""
    pass

class IdiomaNoSoportadoError(Exception):
    """Excepción personalizada para cuando el idioma seleccionado no está soportado."""
    pass
