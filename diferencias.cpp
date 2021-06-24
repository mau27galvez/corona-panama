#include <iostream>

using namespace std;

void printArray(int array[], int n)
{
    for(int i = 0; i < n - 1; i++)
    {
        cout << array[i] << endl;
    }
}

int *getDailyGrow(int array[], int n)
{
    int aumento_de_casos_al_dia[] = {};

    for(int i = 0; i < n - 1; i++)
    {
        int aumento;

        aumento = array[i + 1] - array[i];

        aumento_de_casos_al_dia[i] = aumento;

        // cout << "del dia " << i+1 << " al dia " << i+2  << " aumento: " << aumento << endl;
    }

    return aumento_de_casos_al_dia;
}

void porcentajeDeAumentoDeCasos()
{

}

int main()
{
    int numero_de_casos_por_dia[] = {1, 8, 14, 27, 36, 43, 55, 69, 86, 109, 137, 200};
    int n = sizeof(numero_de_casos_por_dia) / sizeof(numero_de_casos_por_dia[0]);

    int *aumento_de_casos_al_dia;

    aumento_de_casos_al_dia = getDailyGrow(numero_de_casos_por_dia, n);

    for(int i = 0; i < n - 1; i++)
    {
        cout << *aumento_de_casos_al_dia[i] << endl;
    }

    return 0;
}

/*
    int *getDailyGrow(int array[], int n)
{
    int aumento_de_casos_al_dia[] = {};

    for(int i = 0; i < n - 1; i++)
    {
        int aumento;

        aumento = array[i + 1] - array[i];

        aumento_de_casos_al_dia[i] = aumento;

        cout << "del dia " << i+1 << " al dia " << i+2  << " aumento: " << aumento << endl;
    }

    return aumento_de_casos_al_dia;
}
*/