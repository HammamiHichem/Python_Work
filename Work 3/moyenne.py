def main() : 
    note =float(input("Entrez la prémiére note : \n"))
    note2 =float(input("Entrez la deuxième note : \n"))
    note3 =float(input("Entrez la troisième note : \n"))
    result = (note+note2+note3)/3
    print(f"Le résultat est : {result}")
if __name__ == "__main__":
    main()
