/* TELE AULA 02 - PARTE 02
# COMANDO BREAK E CONTINUE
-> O PROGRAMADOR PODE QUERER INTERROMPER TODO O FLUXO DE UM LAÇO DE REPETIÇÃO A QUALQUER MOMENTO OU, EM VEZ DISSO, DESEJAR INTERROMPER PARTE DE UM TRECHO DE CÓDIGO DENTRO
DE UM LOOP E IR DIRETAMENTE PARA A ESTRUTURA DE REPETIÇÃO.
-> PARA TANTO, A PALAVRA RESERVADA BREAK E CONTINUE DEVERÃO SER UTILIZADAS, RESPECTIVAMENTE.
-> ESSES COMANDOS BREAK E CONTINUE FUNCIONAM DE FORMA IGUAL, TANTO NA LINGUAGEM JAVA QUANTO NA LINGUAGEM C.
*/

public class Robo {
    String nome;
    String cor;
    float velocidadeMax;
    int nivelBateriaAtual;
    float pesoCargaMax;
    String tipoTracao;
    boolean temAntena;
    public void printStatus() {
        System.out.println("--------------------------------------------");
        System.out.println("Nome do Robô: " +nome);
        System.out.println("Cor do Robô: "+cor);
        System.out.println("Velocidade Máxima: "+velocidadeMax);
        System.out.println("Bateria: "+nivelBateriaAtual);
        System.out.println("Carga Máxima: "+pesoCargaMax);
        System.out.println("Tipo de Tração: "+tipoTracao);
        System.out.println("Tem Antena? "+temAntena);
        System.out.println("--------------------------------------------");
    }
    public static void main(String[] args) {
        Robo objet01 = new Robo();
        objet01.nome = "R-801";
        objet01.cor = "Azul";
        objet01.velocidadeMax = 6;
        objet01.nivelBateriaAtual = 78;
        objet01.pesoCargaMax = 10;
        objet01.tipoTracao = "Esteira";
        objet01.temAntena = true;
        objet01.printStatus();
        
        Robo objet02 = new Robo();
        objet02.nome = "R-701";
        objet02.cor = "Laranja";
        objet02.velocidadeMax = 3;
        objet02.nivelBateriaAtual = 51;
        objet02.pesoCargaMax = 15;
        objet02.tipoTracao = "Esteira";
        objet02.temAntena = false;
        objet02.printStatus();
        
        Robo objet03 = new Robo();
        objet03.nome = "Oliver";
        objet03.cor = "Parda";
        objet03.velocidadeMax = 11;
        objet03.nivelBateriaAtual = 33;
        objet03.pesoCargaMax = 20;
        objet03.tipoTracao = "Rodas";
        objet03.temAntena = false;
        objet03.printStatus();
    }
}