#pragma once

class Alimento
{
private:
    int Energia;
public:
    Alimento(int Energia)
    {
        this-> Energia = Energia;
    };
    int ExtraerEnergia()
    {
        return this->Energia;
    };
    ~Alimento(){};
};

