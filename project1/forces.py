print("Hello, this program calculates gravitational force between two objects or the amount of force between two electrically charged particles.")
decision=input("gravitational force or electrical force? gr for 1st and el for 2nd: ")
if decision=="gr" or decision=="gravitational":
    def gravitational_force(mass1, mass2, distance):
        G=6.673*(10**-11)
        GrF=(G*mass1*mass2)/(distance**2)
        calculation="When using formula of G: {}, gravitational force between this two objects will be {} newtons.".format(G, GrF)
        print(calculation)
    gravitational_force(mass1=float(input("Mass of the first object in kgs: ")), mass2=float(input("Mass of the second object in kgs: ")), distance=float(input("Distance between centers of masses in meters: ")))
elif decision=="el" or decision=="electrical":
    def electrical_force(charge1, charge2, distance2):
        K=(9*(10**9))
        ElF=(K*charge1*charge2)/(distance2**2)
        calculation2="When using Coulomb's law, electrical force between this two electrically charged particles will be {} coulombs.".format(ElF)
        print(calculation2)
    electrical_force(charge1=float(input("Charge of first particle in coulombs: ")), charge2=float(input("Charge of second particle in coulombs: ")), distance2=float(input("Distance between two particles in meters: ")))
print("Thanks for attention!")