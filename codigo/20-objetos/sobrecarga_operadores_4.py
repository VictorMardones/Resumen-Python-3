# Si x e y son de tipo distinto y x no ha implementado los métodos mágicos
x + y == y.__radd__(x)
x - y == y.__rsub__(x)
x * y == y.__rmul__(x)
x / y == y.__rtruediv__(x)
x // y == y.__rfloordiv__(x)
x % y == y.__rmod__(x)
x ** y == y.__rpow__(x)
x & y == y.__rand__(x)
x ^ y == y.__rxor__(x)
x | y == y.__ror__(x)