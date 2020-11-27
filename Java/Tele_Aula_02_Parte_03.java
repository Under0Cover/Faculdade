// TELE AULA 02 - PARTE 03
public class Triangulo {
    double ladoA;
    double ladoB;
    double ladoC;
    public Triangulo (double lado) {
        this.ladoA = lado;
        this.ladoB = lado;
        this.ladoC = lado;
    }
    
    public Triangulo(double a, double b, double c) {
        this.ladoA = a;
        this.ladoB = b;
        this.ladoC = c;
    }
    
    public Triangulo(double a, double b) {
        this.ladoA = a;
        this.ladoB = b;
        this.ladoC = b;
    }
    
    @Override
    public String toString() {
        return String.format("a: %.2f\nb: %.2f\nc: %.2f",
        this.ladoA, this.ladoB, this.ladoC);
    }
    public static void main(String[] args) {
        Triangulo trianEquilatero = new Triangulo(5);
        Triangulo trianIsosceles = new Triangulo(5, 10);
        Triangulo trianEscaleno = new Triangulo(3, 4, 5);
        System.out.println(trianEquilatero);
        System.out.println("-------------");
        System.out.println(trianIsosceles);
        System.out.println("-------------");
        System.out.println(trianEscaleno);
        System.out.println("-------------");
    }
}
