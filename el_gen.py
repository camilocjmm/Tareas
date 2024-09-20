import random
def gen_pass(password):
    letras = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    password_result = ""
    for i in range(password):
        password_result += random.choice(letras)
    return(password_result)
