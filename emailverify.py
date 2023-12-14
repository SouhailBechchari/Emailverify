import re

def verifie_format_email_regex(email):
    pattern = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
    return bool(pattern.match(email))

# Exemple d'utilisation
email_test = "becharisouhail@gmail.com"
resultat = verifie_format_email_regex(email_test)
print(resultat) 
