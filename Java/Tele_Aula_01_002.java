public class Robo {
    String nome;
    String cor;
    float velocidadeMax;
    float pesoCargaMax;
    int nivelBateriaAtual;
    boolean temAntena;
    public static void main (String[] args) {
        Robo obj1 = new Robo();
        obj1.nome = "Roboken";
        obj1.cor = "Azul";
        obj1.velocidadeMax = 6;
        obj1.pesoCargaMax = 50;
        obj1.nivelBateriaAtual = 90;
        obj1.temAntena = true;
            System.out.println("Nome do Robô: "+obj1.nome);
            System.out.println("Cor do Robô: "+obj1.cor);
            System.out.println("Velocidade Máxima: "+obj1.velocidadeMax);
            System.out.println("Bateria está em: "+obj1.nivelBateriaAtual);
            System.out.println("Carga Máxima suportada: "+obj1.pesoCargaMax);
            System.out.println("Possui antema? "+obj1.temAntena);
    }
}