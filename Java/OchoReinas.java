public class OchoReinas {

    // Tamaño del tablero (8x8 en este caso)
    static final int N = 8;

    // Función para imprimir el tableron 8x8
    static void imprimirTablero(int tablero[][]) {
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                System.out.print(tablero[i][j] + " ");
            }
            System.out.println();
        }
    }

    // Función para verificar si una reina puede ser colocada en la posición (fila, columna)
    static boolean esSeguro(int tablero[][], int fila, int columna) {
        int i, j;

        // Verificar la fila en la izquierda
        for (i = 0; i < columna; i++) {
            if (tablero[fila][i] == 1) {
                return false;
            }
        }

        // Verificar la diagonal superior izquierda
        for (i = fila, j = columna; i >= 0 && j >= 0; i--, j--) {
            if (tablero[i][j] == 1) {
                return false;
            }
        }

        // Verificar la diagonal inferior izquierda
        for (i = fila, j = columna; i < N && j >= 0; i++, j--) {
            if (tablero[i][j] == 1) {
                return false;
            }
        }

        return true;
    }

    // Función principal para resolver el problema de las 8 reinas utilizando backtracking
    static boolean resolver8Reinas(int tablero[][], int columna) {
        // Caso base: Si todas las reinas están colocadas, entonces hemos resuelto el problema
        if (columna >= N) {
            return true;
        }

        // Intentar colocar esta reina en todas las filas una por una
        for (int i = 0; i < N; i++) {
            if (esSeguro(tablero, i, columna)) {
                tablero[i][columna] = 1; // Colocar la reina

                // Recursivamente intentar colocar las reinas restantes
                if (resolver8Reinas(tablero, columna + 1)) {
                    return true;
                }

                // Si colocar la reina en (i, columna) no lleva a una solución, entonces retroceder (backtrack)
                tablero[i][columna] = 0;
            }
        }

        // Si no se puede colocar la reina en ninguna fila en esta columna, entonces no hay solución
        return false;
    }

    public static void main(String args[]) {
        int tablero[][] = new int[N][N];

        if (!resolver8Reinas(tablero, 0)) {
            System.out.println("No hay solución");
        } else {
            imprimirTablero(tablero);
        }
    }
}
