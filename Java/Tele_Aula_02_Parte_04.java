/* # TELE AULA 02 - PARTE 04
## REUTILIZAÇÃO DE CLASSES
# REAPROVEITAMENTO DE ESTRUTURAS
-> MODIFICADORES DE ACESSO: 
    CARACTERÍSTICA DE ORIENTAÇÃO A OBJETO QUE PERMITE AO PROGRAMADOR OCULTAR CLASSES E SEUS MEMBROS, TORNANDO CONTROLADA SUA UTILIZAÇÃO POR OUTROS PROGRAMADORES.
    SÃO ELES:
    -> PUBLIC:
        PODERÁ SER ACESSADO OU EXECUTADO A PARTIR DE QUALQUER OUTRA CLASSE;
    -> PRIVATE:
        SÓ PODEM SER ACESSADOS, MODIFICADOS OU EXECUTADOS POR MÉTODOS DA MESMA CLASSE, SENDO COMPLETAMENTE OCULTOS PARA OUTROS PROGRAMADORES;
    -> PROTECTED:
        FUNCIONA COMO O PRIVATE, MAS HERDEIRAS TAMBÉM TENHAM ACESSO AO CAMPO OU MÉTODO DECLARADO;
    -> SEM MODIFICADORES:
        SERÃO CONSIDERADOS COMO PERTENCENTES À CATEGORIA PACKAGE OU FRIENDLY. SEUS CAMPOS E MÉTODOS PODEM SER ACESSADOS EM TODAS AS CLASSES DE UM MESMO PACOTE.
-> HERANÇA:
    MECANISMO QUE PERMITE A CRIAÇÃO DE UMA NOVA CLASSE QUE ESTENDE UMA OUTRA JÁ DEFINIDA PELO PROGRAMADOR, O QUE TORNA POSSÍVEL A REUTILIZAÇÃO DE DADOS E COMPORTAMENTOS
DA CLASSE ANCESTRAL.
    HERANÇA É UMA FORMA DE REUTILIZAÇÃO DE SOFTWARE NA QUAL UMA NOVA CLASSE É CRIADA, ABSORVENDO MEMBROS DE UMA CLASSE EXISTENTE E APRIMORADA COM CAPACIDADES NOVAS 
OU MODIFICADAS.
    A UTILIZAÇÃO DA HERANÇA PERMITE QUE CLASSES MAIS GENÉRICAS SEJAM REAPROVEITADAS PARA COMPOR CLASSES MAIS ESPECÍFICAS, O QUE CONFERE A SEGURANÇA E RACIONALIDADE
AO PROCESSO DE DESENVOLVIMENTO DE APLICAÇÕES.
-> POLIMORFISMO:
    POR MEIO DO POLIMORFISMO, UM OBJETO PODE SER REFERENCIADO DE VÁRIAS FORMAS, O QUE CONFERE FLEXIBILIDADE AO DESENVOLVIMENTO DA SOLUÇÃO.
    É A CAPACIDADE DE UM OBJETO PODE SER REFERENCIADO DE VÁRIAS FORMAS, O QUE NÃO QUER DIZER QUE O OBJETO FICA SE TRANSFORMANDO. AO CONTRÁRIO DISSO, UM OBJETO NASCE
DE UM TIPO E MORRE DAQUELE TIPO. O QUE PODE MUDAR É A MANEIRA COMO NOS REFERIMOS A ELE. POLIMORFISMO PERMITE A MANIPULAÇÃO DE INSTÂNCIAS DE CLASSES QUE HERDAM DE UMA
MESMA CLASSE ANCESTRAL DE FORMA UNIFICADA: PODEMOS RECEBER MÉTODOS QUE RECEBAM INSTÂNCIAS DE UMA CLASSE C, E OS MESMOS MÉTODOS SERÃO CAPAZES DE PROCESSAR INSTÂNCIAS
DE QUALQUER CLASSE QUE HERDE DA CLASSE C, JÁ QUE QUALQUER CLASSE QUE HERDE DE C É-UM-TIPO-DE-C.
# CONCEITO
    -> POLIMORFISMO COM SOBRECARGA:
        # PERMITE TER FUNÇÕES COM O MESMO NOME, FUNCIONALIDADES SIMILARES E EM CLASSES DISTINTAS.
    -> POLIMORFISMO PARAMÉTRICO:
        # PERMITE TER FUNÇÕES COM O MESMO NOME, PORÉM COM PARÂMETROS DIFERENTES.
    -> POLIMORFISMO DE HERANÇA:
        # PERMITE A REDEFINIÇÃO DE UM MÉTODO EM CLASSES HERDEIRAS DE UMA CLASSE BÁSICA (ESPECIALIZAÇÃO).
-> ENCAPSULAMENTO:
    CARACTERÍSTICA QUE PERMITE QUE AS VARIÁVEIS DA CLASSE E SEUS MÉTODOS SEJAM AGRUPADOS EM CONJUNTOS, SEGUNDO O SEU GRAU DE RELAÇÃO.
    OCULTAR DADOS ATRÁS DE MÉTODOS DE MODO QUE SEJAM INACESSÍVEIS A OUTROS OBJETOS É A BASE FUNDAMENTAL DO ENCAPSULAMENTO DE DADOS.
*/

public class Matematica {
    static int mult(int a, int b) {
        return a * b;
    }
    static double mult(double a, double b) {
        return a * b;
    }
    static double mult(double a, double b, double c){
        return a * b * c;
    }
    public static void main(String[] args) {
        System.out.println("Multiplicação: " +Matematica.mult(5, 3));
        System.out.println("Multiplicação: " +Matematica.mult(3.2, 4.1));
        System.out.println("Multiplicação: " +Matematica.mult(1.4, 2));
        System.out.println("Multiplicação: " +Matematica.mult(4.5, 5.5, 2.5));
    }
}