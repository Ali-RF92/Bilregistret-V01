import json


class Bibliotek:
    def __init__(self, file_name='böker.jason'):
        self.file_name = file_name
        self.böcker: dict[str, Bok] = {}
        self.load_bok_info()

    def save_bok_info(self, böcker):
        böcker = {}
        for bok_id, bok_obj in self.böcker.items():
            böcker[bok_id] = {"Titel": bok_obj.titel,
                              "Forfattare": bok_obj.författare,
                              "Upplaga": bok_obj.upplaga}

        with open(self.file_name, "w") as f:
            json.dump(böcker, f, indent=4)

    def load_bok_info(self):
        try:
            with open(self.file_name, "r") as f:
                bok_info = json.load(f)
                for bok_id, info in bok_info.items():
                    bok = Bok(
                        info["Titel"], info["Forfattare"], info["Upplaga"], bok_id)
                    self.böcker[bok_id] = bok

        except:
            pass

    def skriv_ut_titlar(self):
        for bok in self.böcker.values():
            print(bok.titel)

    def skriv_ut_författare(self):
        for bok in self.böcker.values():
            print(bok.författare)

    def skriv_ut_böcker(self):
        for bok in self.böcker.values():
            print(bok)

    def lägg_till_bok(self, bok: "Bok"):
        if bok.bok_id in self.böcker:
            ...
        else:
            self.böcker[bok.bok_id] = bok


class Bok:
    def __init__(self, titel: str, författare: str, upplaga: int, bok_id: str):

        self.titel = titel
        self.författare = författare
        self.upplaga = upplaga
        self.bok_id = bok_id

    def __str__(self):
        return f"{self.titel}\n{self.författare}\n{self.upplaga}\n{self.bok_id}"


def main_menu():
    bib = Bibliotek()
    bib.load_bok_info()

    while True:
        print("1. Skapa bok")
        print("2. Skriv ut alla titlar")
        print("3. Skriv ut alla författare")
        print("4. Skriv ut alla böcker")
        print("5. Avsluta")

        choice = input("Ange val --> ")

        if choice == "1":
            titel, författare, upplaga, bok_id = input(
                "Ange info om boken (titel, författare, upplaga, bok id)").strip().split(",")
            ny_bok = Bok(titel, författare, int(upplaga), bok_id)
            bib.lägg_till_bok(ny_bok)

        elif choice == "2":
            bib.skriv_ut_titlar()

        elif choice == "3":
            bib.skriv_ut_författare()

        elif choice == "4":
            bib.skriv_ut_böcker()

        elif choice == "5":
            bib.save_bok_info()
            break

        else:
            print("Felaktigt val")


if __name__ == "__main__":
    main_menu()
