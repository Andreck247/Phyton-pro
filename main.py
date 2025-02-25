meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "GG": "Se usa para felicitar cuando se juega bien",
            "IDK": "Se usa para expresar que no se sabe algo",
            "BTW": "Se utiliza cuando se está hablando sobre un tema concreto y se quiere añadir algo relacionado"
            }
word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")
if word in meme_dict.keys():
    print(meme_dict[word])
    # ¿Qué debemos hacer si se encuentra la palabra?
else:
    print("No tenemos esa palabra en el diccionario")
    # ¿Qué hacer si no se encuentra la palabra?
