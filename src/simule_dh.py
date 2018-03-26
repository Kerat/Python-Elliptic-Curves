#coding: utf8
from .DiffieHellman import DiffieHellman

def echange_de_clef():
    """
    Simulation d'une génération de clef secrète entre
    Alice et Bob via Diffie Hellman sur une courbe
    elliptique.
    """
    alice = DiffieHellman()
    bob = DiffieHellman()
    print("On travaille sur une courbe elliptique\
 connue (recommandée par l'ANSSI).")
    print("On choisi un point P (recommandé par l'ANSSI\
 également) :")
    print(str(alice.P))
    print("(Le dernier elément du tuple est une représentation\
du point à l'infini,\ns'il est égal à 1 alors il s'agit du point\
à l'infini)\n\n")
    print("Alice choisi une clef privée 'a'...")
    print("a = " + str(alice.pre_key))
    print("Bob choisi une clef privée 'b'...")
    print("b = " + str(bob.pre_key))
    print("\n\nAlice calcule aP...")
    print("aP = " + str(alice.get_shared_key()))
    print("Bob calcule bP...")
    print("bP = " + str(bob.get_shared_key()))
    print("\nAlice envoie aP à Bob qui calcule abP...")
    bob.compute_secret(alice.get_shared_key())
    print("abP (calculé par Bob) : " + str(bob.shared_secret))
    print("\nBob envoie bP à Alice qui calcule abP...")
    alice.compute_secret(bob.get_shared_key())
    print("abP (calculé par Alice) : " + str(alice.shared_secret))
    print("On vérifie que Alice et Bob ont bien calculer les mêmes abP...")
    print("abP (Alice) = abP (Bob) ? : " + str(alice.shared_secret==bob.shared_secret))
    if alice.shared_secret == bob.shared_secret :
        print("\n\nAlice et Bob partagent un secret commun !")
        print("Secret commun (abP) : " + str(alice.shared_secret))
    else:
        # Ca ne devrait pas arriver
        print("Oula ! Quelque chose s'est mal passé on dirait !")
        print("Alice et Bob n'ont pas le même abP...")

if __name__ == '__main__':
    echange_de_clef()
