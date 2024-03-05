#include<iostream>
#include<Mascota.hpp>
#include<Alimento.hpp>
#include<list>



int main(int argc, char const *argv[])
{
    std::list<Mascota>mascotas;
    
    Mascota m1("Firulais");
    Mascota m2("Coraje");

    mascotas.push_back(m1);
    mascotas.push_back(m2);

    Alimento a1(5);
    Alimento a2(2);

    m1.Comer(a1);
    m2.Comer(a2);

    for (auto &&mascota : mascotas)
    {
        std::cout
            << mascota.LeerNombre()
            <<" : "
            << mascota.LeerEnergia()
            << std::endl;
    }

    return 0;
}
