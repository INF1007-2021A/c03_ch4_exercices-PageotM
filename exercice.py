#!/usr/bin/env python
# -*- coding: utf-8 -*-


def is_even_len(string: str) -> bool:
    return not(bool(len(string)%2))


def remove_third_char(string: str) -> str:
    return string[0:2]+string[3:len(string)]


def replace_char(string: str, old_char: str, new_char: str) -> str:
    return string.replace(old_char,new_char)


def get_nb_char(string: str, char: str) -> int:
    count = 0
    for lettre in string:
        if lettre == char:
            count += 1
    return count


def get_nb_words(sentence: str) -> int:
    ### on définit un mot comme un ensemble de caracteres nons-espaces qui est délimité par des espaces
    return len(sentence.split())


def main() -> None:
    string = "Bonjour!"
    parity = 'pair' if is_even_len(string) else 'impair'
    print(f"Le nombre de caractère dans la chaine '{string}' est {parity}")

    string = "Sam est cool!"
    print(f"On supprime le 3e caratère dans la chaine '{string}'. Résultat: {remove_third_char(string)}")

    string = "hello world!"
    print(f"On remplace le caratère w par le caractère z dans la chaine: '{string}'. Résultat: {replace_char(string, 'w', 'z')}")

    print(f"Le nombre d'occurrence de l dans hello world est : {get_nb_char(string, 'l')}")
    
    string = "Baby shark doo doo doo doo doo doo"
    print(f"Le nombre de mots dans la chaine {string} est: {get_nb_words(string)}")


if __name__ == '__main__':
    main()
