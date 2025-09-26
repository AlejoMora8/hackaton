import random
import requests


def generador(pass_length):
    characts = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    contra = ""

    for i in range(pass_length):
        contra += random.choice(characts)

    return contra


def gen_emoji():
    emoji = ["\U0001f600", "\U0001f642", "\U0001F606", "\U0001F923", ":sunglasses:", ":grapes:", ":partying_face:", ":metal:"]
    return random.choice(emoji)


def gira_una_moneda():
    giro = random.randint(0, 2)
    if giro == 0:
        return "Cara"
    else:
        return "Sello"


def dados():
    giorodado = random.randint(1, 6)
    return giorodado


def ayudas():
    uno = "Necesitas ayuda? , este bot tiene las siguientes disponibilidades:$emogi(para generar un emogi al azar) $moneda(para tirar una moneda) $gen(para generar una contraseña) $joined @el usuario (para poder saber cuanto tiempo va esa persona en el servidor) $repeat (es para que el bot repita lo que ti digas) $heh (es para que repita heh las veces que digas) $dado (para que gire un dado)"
    return uno


def chistes():
    mems = ["¿Qué le dice un jardinero a otro? Nos vemos cuando podamos.", "¿Y cómo se llama un boomerang que no vuelve? Palo.", "El otro día vendí mi aspiradora. Lo único que hacía era acumular polvo."]
    return random.choice(mems)


def get_duck_image_url():
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


def get_dog_image_url():
    url = 'https://random.dog/woof.json'
    res = requests.get(url)
    data = res.json()
    return data['url']


def get_fox_image_url():
    url = 'https://randomfox.ca/floof/'
    res = requests.get(url)
    data = res.json()
    return data['image']
