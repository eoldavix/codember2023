#!/usr/bin/env python3
import requests

"""** El reto **
Un espía está enviando mensajes encriptados.

Tu misión es crear un programa que nos ayude a buscar patrones...

Los mensajes son palabras separadas por espacios como este:
gato perro perro coche Gato peRRo sol

Necesitamos que el programa nos devuelva el número de veces que aparece cada
palabra en el mensaje, independientemente de si está en mayúsculas o
minúsculas.

El resultado será una cadena de texto con la palabra y el número de veces que
aparece en el mensaje, con este formato:
gato2perro3coche1sol1

¡Las palabras son ordenadas por su primera aparición en el mensaje!

** Más ejemplos: **
llaveS casa CASA casa llaves -> llaves2casa3
taza ta za taza -> taza2ta1za1
casas casa casasas -> casas1casa1casasas1
"""


def find_patterns(message: str) -> str:
    """
    :example:
    >>> find_patterns('gato perro perro coche Gato peRRo sol')
    'gato2perro3coche1sol1'
    >>> find_patterns('llaveS casa CASA casa llaves')
    'llaves2casa3'
    >>> find_patterns('taza ta za taza')
    'taza2ta1za1'
    >>> find_patterns('casas casa casasas')
    'casas1casa1casasas1'
    """
    patterns = {}

    for word in message.split(" "):
        if word.lower() in patterns.keys():
            patterns[word.lower()] += 1
        else:
            patterns[word.lower()] = 1

    return_string = ""
    for key, value in patterns.items():
        return_string += key
        return_string += str(value)

    return return_string


if __name__ == "__main__":
    test_string = requests.get(
        "https://codember.dev/data/message_01.txt"
    ).text.strip()
    print(find_patterns(test_string))
