#include <iostream>

template <typename T>

class Rectangulo
{
private:
	T ancho_;
	T alto_;

public:
	Rectangulo(T ancho, T alto) : ancho_(ancho), alto_(alto) {}
	T area() const
	{
		return ancho_ * alto_;
	}
};

int main()
{
	Rectangulo<int> rect(5, 3);
	std::cout << "El área del rectángulo es: " << rect.area() << std::endl;

	return 0;
}
