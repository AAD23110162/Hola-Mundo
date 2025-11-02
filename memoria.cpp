#include<iostream>

using namespace std;

class Enano
{
    int tamano;
    bool vivo;
};

int main(int arg, char const *argv[])
{
    cout<<"int  :"<<sizeof(int)<<endl;
    cout<<"bool :"<<sizeof(bool)<<endl;
    cout<<"char :"<<sizeof(char)<<endl;
    cout<<"float:"<<sizeof(float)<<endl;
    cout<<"double:"<<sizeof(double)<<endl;
    cout<<"Direccion de memoria: "<<endl;
    int a = 5;
    cout<<"Direccion :"<<&a<<endl;

    return 0;
}