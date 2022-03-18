#include <stdio.h>
#include <math.h>

typedef struct point{
	int X;
	int Y;
} Point;


int main ()
{
	Point p1, p2, p3, p4;
    int i=0;
    double r1, r2, r3, r4, r5, r6, lista[6], maior=0;

    scanf("%d ", &p1.X);
    scanf("%d ", &p1.Y);
    scanf("%d ", &p2.X);
    scanf("%d ", &p2.Y);
    scanf("%d ", &p3.X);
    scanf("%d ", &p3.Y);
    scanf("%d ", &p4.X);
    scanf("%d", &p4.Y);

    r1 = sqrt(pow(p1.X - p2.X, 2) + pow(p1.Y - p2.Y, 2));
    lista[0] = r1;
    r2 = sqrt(pow(p1.X - p3.X, 2) + pow(p1.Y - p3.Y, 2));
    lista[1] = r2;
    r3 = sqrt(pow(p1.X - p4.X, 2) + pow(p1.Y - p4.Y, 2));
    lista[2] = r3;
    r4 = sqrt(pow(p2.X - p3.X, 2) + pow(p2.Y - p3.Y, 2));
    lista[3] = r4;
    r5 = sqrt(pow(p2.X - p4.X, 2) + pow(p2.Y - p4.Y, 2));
    lista[4] = r5;
    r6 = sqrt(pow(p3.X - p4.X, 2) + pow(p3.Y - p4.Y, 2));
    lista[5] = r6;

    do{
        if (lista[i]>maior)
            maior = lista[i];
        i++;
    }while(i<6);

    printf("A maior distancia entre os pontos foi: %.2lf\n", maior);


	return 0;
}