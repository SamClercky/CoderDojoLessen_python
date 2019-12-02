import sys

levens = 6
woord = "pythonp"
te_raden = list(woord)
geraden = list("_"*len(woord))


def antwoord():
    result = ""
    while result == "_" or len(result) != 1 or result.isdecimal():
        result = input("Geef mij een letter: ")
    return result


while levens > 0:
    print("Geraden woord: ", "".join(geraden))
    gekozen_letter = antwoord()
    if gekozen_letter in te_raden:
        index = te_raden.index(gekozen_letter)
        geraden[index] = gekozen_letter
        te_raden[index] = "_"
        print("Goed zo")
    else:
        levens -= 1
        print("Fout, levens: ", levens)

    if geraden == list(woord):
        print("Gewonnen :-)")
        sys.exit(0)

print("Verloren :-(")
