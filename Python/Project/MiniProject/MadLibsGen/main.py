# coding = UTF-8

print("Du wirst heute Geschichte schreiben, bist du bereit?")
bereit = input()

if bereit in ("Nein", "n", "no", "N"):
    print("Dann nicht!")
    quit()

print("Na dann, lass uns beginen!")
print("Wie ist Ihr Name?")
name = input()
print("Ihr Name lautet", name, "Stimmt das?")
ask = input()
if ask in ("Nein", "n", "no", "N"):
    print("Wie ist Ihr richtiger Name?")
    name = input()

print("Wie alt sind Sie?")
old = input()
print("Sie sind", old, "Jahre alt. Stimmt das?")
if ask in ("Nein", "n", "no", "N"):
    print("Wie alt sind Sie wirklich?")
    old = input()

print("An wenn richtet sich die Geschichte?")
dic = input()

print("Wir sind so weit, möchten Sie die Geschichte höhren?")
ask2 = input()
if ask2 in ("Nein", "n", "no", "N"):
    print("Blöde entscheidung...")
    quit()

print("Liebe Frau/Herr", dic, "\n""mein Name ist", name,
      "und ich wollte Sie darum bitten, meine Pornografie zu löschen, da mein Alter erst", old, "beträgt.""\n""Danke für Ihr Verständinss.""\n" "MfG", "\n", name)
