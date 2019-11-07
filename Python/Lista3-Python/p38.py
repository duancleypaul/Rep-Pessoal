def valuesort(dicionario):
    sorted_keys = sorted(dicionario.keys())
    return [dicionario[key] for key in sorted_keys]