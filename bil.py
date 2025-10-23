import json
class Bilregister:
    def __init__(self, file_name='bilar.json'):
        self.file_name = file_name
        self.bilar: dict[str, Bil] = {}
        self.load_bil_info()
 
    def save_bil_info(self):
        bilar = {}
        for bil_id, bil_obj in self.bilar.items():
            bilar[bil_id] = {"regnummer": bil_obj.regnummer,
                              "märke": bil_obj.märke,
                              "modell": bil_obj.modell,
                              "år" : bil_obj.år,
                              "mil": bil_obj.mil}
 
        with open(self.file_name, "w") as f:
            json.dump(bilar, f, indent=4)
 
    def load_bil_info(self):
        try:
            with open(self.file_name, "r") as f:
                bil_info = json.load(f)
                for bil_regnummer, info in bil_info.items():
                    bil = Bil(
                        info["regnummer"], info["märke"], info["modell"],info["år"],info["mil"], bil_regnummer)
                    self.bilar[bil_regnummer] = bil
 
        except:
            pass
 
    def skriv_ut_regnummer(self):
        for bil in self.bilar.values():
            print(f"\033[32m{bil.regnummer}\033[0m")

            
 
    def skriv_ut_märke(self):
        for bil in self.bilar.values():
            print(f"\033[32m{bil.märke}\033[0m")
 
    def skriv_ut_modell(self):
        for bil in self.bilar.values():
           print(f"\033[32m{bil.modell}\033[0m")
 
    def skriv_ut_år(self):
        for bil in self.bilar.values():
            print(f"\033[31m{bil.år}\033[0m")
 
    def skriv_ut_mil(self):
        for bil in self.bilar.values():
            print(f"\033[31m{bil.mil}\033[0m")
 
    def skriv_ut_bilar(self):
        for bil in self.bilar.values():
           print(f"\033[35m{bil}\033[0m")
 
    def lägg_till_bil(self, bil: "Bil"):
        if bil.bil_id in self.bilar:
            ...
        else:
            self.bilar[bil.bil_id] = bil
 
 
class Bil:
    def __init__(self, regnummer: str, märke: str, modell: int, år: str,mil: str, bil_id:str ):
 
        self.regnummer = regnummer
        self.märke = märke
        self.modell = modell
        self.år = år
        self.mil = mil
        self.bil_id = bil_id
 
    def __str__(self):
        return f"{self.regnummer}\n{self.märke}\n{self.modell}\n{self.år}\n{self.mil}\n{self.bil_id}"
 


def main_menu():
    register = Bilregister()
    register.load_bil_info()
 
    while True:
        print("1. Skapa bil")
        print("2. Skriv ut alla regnummer")
        print("3. Skriv ut alla märke")
        print("4. Skriv ut alla modell")
        print("5. Skriv ut alla år")
        print("6. Skriv ut alla mil")
        print("7. Skriv ut alla bilar")
        print("8. Avsluta")
 
        choice = input("Ange val --> ")
 
        if choice == "1":
            regnummer, märke, modell, år, mil, bil_id = input(
                "Ange info om bilen (regnummer, märke, modell, år, mil,bil_ID )").strip().split(",")
            ny_bil = Bil(regnummer, märke, modell , int(år), int(mil), bil_id)
            register.lägg_till_bil(ny_bil)
            register.save_bil_info()
 
        elif choice == "2":
           register.skriv_ut_regnummer()
 
        elif choice == "3":
            register.skriv_ut_märke()
 
        elif choice == "4":
            register.skriv_ut_modell()
 
        elif choice == "5":
            register.skriv_ut_år()
        elif choice == "6":
            register.skriv_ut_mil()
        elif choice == "7":
            register.skriv_ut_bilar()
        else:
            print("Felaktigt val")
            break
 
        
 
 
if __name__ == "__main__":
    main_menu()
 