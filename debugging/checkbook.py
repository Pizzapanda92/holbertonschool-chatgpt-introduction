class Checkbook:
    def __init__(self):
        self.balance = 0.0

    def deposit(self, amount):
        self.balance += amount
        print("Déposé : ${:.2f}".format(amount))
        print("Solde actuel : ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        if amount > self.balance:
            print("Fonds insuffisants pour réaliser ce retrait.")
        else:
            self.balance -= amount
            print("Retiré : ${:.2f}".format(amount))
            print("Solde actuel : ${:.2f}".format(self.balance))

    def get_balance(self):
        print("Solde actuel : ${:.2f}".format(self.balance))

def main():
    cb = Checkbook()
    while True:
        action = input("Que souhaitez-vous faire ? (déposer, retirer, solde, quitter) : ")
        if action.lower() == 'quitter':
            break
        elif action.lower() == 'déposer':
            try:
                amount = float(input("Entrez le montant à déposer : $"))
                cb.deposit(amount)
            except ValueError:
                print("Entrée invalide. Veuillez entrer un nombre.")
        elif action.lower() == 'retirer':
            try:
                amount = float(input("Entrez le montant à retirer : $"))
                cb.withdraw(amount)
            except ValueError:
                print("Entrée invalide. Veuillez entrer un nombre.")
        elif action.lower() == 'solde':
            cb.get_balance()
        else:
            print("Commande invalide. Veuillez réessayer.")

if __name__ == "__main__":
    main()

