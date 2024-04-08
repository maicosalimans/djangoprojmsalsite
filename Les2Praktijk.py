class Persona(object):

    # __init__ staat voor constructor
    def __init__(self, naam, idnummer):
        self.naam = naam
        self.idnummer = idnummer

    def display(self):
        print(self.naam)
        print(self.idnummer)

    def details(self):
        print("Mijn naam is {}".format(self.naam))
        print("Mijn id nummer is: {}".format(self.idnummer))

class Docent(Persona):
    def __init__(self, naam, idnummer, salaris, vak):
        self.salaris = salaris
        self.vak = vak

        # het oproepen van de __init__ van parent class
        Persona.__init__(self, naam, idnummer)

    def details(self):
        print("Mijn naam is: {}".format(self.naam))
        print("Mijn id nummer is: {}".format(self.idnummer))
        print("Ik geef het vak: {}".format(self.vak))

x = Docent("Jan", "3456", "56000", "Engels")

x.details()