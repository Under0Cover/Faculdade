/* TELE AULA 03 - PARTE 01
### EXCEÇÕES, CLASSES ABSTRATAS E INTERFACES ORIENTADA O OBJETOS
## DEFINIÇÃO E TRATAMENTO DE EXCEÇÕES
    -> EXCEÇÕES EM JAVA:
    * SE REFEREM AOS ERROS QUE PODEM SER GERADOS DURANTE A EXECUÇÃO DE UM PROGRAMA
    * COMO O NOME SUGERE, TRATA-SE DE ALGO QUE INTERROMPE A EXECUÇÃO NORMAL DO PROGRAMA
    * O TRATAMENTO DA EXCEÇÃO SERVE JUTAMENTE PARA QUE O PROGRAMA POSSA CONTINUAR SENDO EXECUTADO EM VEZ DE SER ENCERRADO REPETINAMENTE, O QUE CONFERE CONFIABILIDADE E
ROBUSTEZ ÀS APLICAÇÕES.
    
    -> SEQUÊNCIA DE ESCAPE DA LINGUAGEM JAVA
    */  public class Classe {
            public static void main(String[] args) {
            
    /*
        Sequência de Escape         Descrição                                                   Exemplo de utilização
        \n                          Insere nova linha.                                      */System.out.print("Introdução\na\nProgramação\ncom\nJava");                    System.out.print("\n---------------------------------------------------------------\n");
    /*  \t                          Insere tabulação na horizontal.                         */System.out.print("Col A\tCol B\tCol C\tCol D");                               System.out.print("\n---------------------------------------------------------------\n");
    /*  \                           Insere barra invertida.                                 */System.out.print("C:\\Windows\\system32");                                    System.out.print("\n---------------------------------------------------------------\n");
    /*  \”                          Insere aspa dupla.                                      */System.out.print("Nome do livro \"Dom Quixote\" de Miguel de Cervantes");     System.out.print("\n---------------------------------------------------------------\n");
    /*  \r                          Realiza retorno do carro.                               */System.out.print("Texto Não Mostrado\rEsseTexto Aparece\n");                 System.out.print("---------------------------------------------------------------\n");

    }
}
/*
## DUAS CATEGORIAS DE EXCEÇÕES EM JAVA
    -> UNCHECKED EXCEPTION:
        * SIGNIFICA "EXCEÇÃO NÃO VERIFICADA". O JAVA NÃO VERIFICA O CÓDIGO-FONTE PARA DETERMINAR SE A EXCEÇÃO ESTÁ SENDO CAPTURADA.
        * POR ISSO, O TRATAMENTO AQUI É OPCIONAL.
        * FAZEM PARTE DESTAS EXCEÇÕES DE TRATAMENTO OPCIONAL, POR EXEMPLO, A VERIFICAÇÃO DE ACESSO A UM ÍNDICE INEXISTENTE NUM VETOR NÃO INSTANCIADO E A CONVERSÃO DE UM STRING EM INTEIRO.
    -> CHECKED EXCEPTION:
        * SIGNIFICA "EXCEÇÃO VERIFICADA". NESTE TIPO DE EXCEÇÃO O COMPILADOR JAVA OBRIGA O PROGRAMADOR A TRATÁ-LA.
        * O JAVA VERIFICA O CÓDIGO-FONTE COM A FINALIDADE DE DETERMINAR SE A EXCEÇÃO ESTÁ SENDO CAPTURADA.

                                    Linhas de Código                                                            Tipo de Exceção Lançada 
    1                               int divPor0 = 5/0;                                                         ArithmeticException
    2                               int valorStr = Integer.parseInt("A");                                      NumberFormatException
    3                               int refNull = Integer.parseInt(null);                                      NullPointerException
    4                               String indiceNegativo = args[-1];                                          ArrayIndexOutOfBoundsException
    5                               System.out.printf("%d", "5");                                              IllegalFormatConversionException
    6                               Scanner sc = new Scanner(System.in); int vFloat = sc.nextInt();ler 3.5   InputMismatchException
*/