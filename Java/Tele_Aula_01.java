/* =====================================================================
PARADIGMA = MODELO - PADRÃO
PARADIGMA DE ORIENTAÇÃO A OBJETOS = ESTILO DE SE PROGRAMAR 
SANTOS (2003) PARADIGMA DE PROGRAMAÇÃO ORIENTADA A OBJETOS CONSIDERA OS DADOS
(NOMES, VALORES, FÓRMULAS E TEXTOS) A SEREM PROCESSADOS E OS MECANISMOS DE 
PROCESSAMENTO DESSES DADOS DEVEM SER CONSIDERADOS EM CONJUNTO 
=======================================================================
A POO É UM PARADIGMA DE PROGRAMAÇÃO QUE UTILIZA == ABSTRAÇÕES == PARA 
REPRESENTAR MODELOS BASEADOS NO MUNDO REAL. UMA FORMA DE ENTENDER A OO
É PENSAR NELA COMO UMA EVOLUÇÃO DA PROGRAMAÇÃO PROCEDURAL 
=======================================================================
CLASSE - OBJETO - ATRÍBUTO - MÉTODO
CLASSE E OBJETO ->
UM DOS ELEMENTOS MAIS BÁSICOS DA OO É A IDEIA DE ORGANIZAR O CÓDIGO
EM == CLASSES == QUE REPRESENTAM ALGO DO MUNDO REAL OU IMAGINÁRIO.
UM OUTRO ELEMENTO BÁSICO DENTRO DA OO É A IDEIA DE == OBJETO == QUE
NADA MAIS É DO QUE A MANIFESTAÇÃO CONCRETA, TAMBÉM CHAMADA DE
INSTÂNCIA DA CLASSE.
===============================================================================
A FIM DE ENTENDER MELHOR O CONCEITO DE CLASSE, VAMOS PENSAR NA ENTIDADE ROBÔ.
CASO VOCÊ TENHA APENAS IMAGINADO UM ROBÔ ABSTRATO, SEM FORMA FÍSICA, QUE É UMA
MÁQUINA CAPAZ DE TOMAR DECISÕES POR SI MESMA, ENTÃO VOCÊ AGIU CORRETAMENTE
SE VOCÊ IMAGINOU UM ROBÔ FÍSICO, COMO UM ROBÔ NA COR AZUL QUE ANDA SOBRE ESTEIRA,
COM DOIS BRAÇOS E UMA ANTENA, ENTÃO VOCÊ NÃO PENSOU NO CONCEITO DE ROBÔ, MAS SIM
EM UMA MANIFESTAÇÃO FÍSICA POSSÍVEL DE ROBÔ.
===============================================================================
LEMBRE-SE: A IDEIA DE ROBÔ É ABSTRATA, ASSIM COMO SÃO AS CLASSES EM JAVA.
UMA BOA FORMA DE COMPREENDER UMA == CLASSE == É PENSAR NELA COMO O PROJETO OU
A MODELAGEM DE ALGO.
CASO TENHA IMAGINADO ALGO CONCRETO, ENTÃO VOCÊ PENSOU EM UM == OBJETO == 
QUE É UMA MANIFESTAÇÃO POSSÍVEL DA IDEIA DE ROBÔ, SEMELHANTE À IDEIA DE OBJETO
EM JAVA. ESSES OBJETOS SÃO INSTÂNCIAS DA CLASSE ROBÔ 
===============================================================================
OS PRINCIPAIS ELEMENTOS QUE COMPÕEM UMA CLASSE SÃO OS == ATRIBUTOS == E OS 
== MÉTODOS ==. UM ATRIBUTO É UM ELEMENTO QUE REPRESENTA AS == CARACTERÍSTICAS ==
INTRÍNSECAS DA CLASSE.
O ROBÔ: SUPONHAMOS QUE, PARA CARACTERIZARMOS ALGUNS ROBÔS, OS SEGUINTES == ATRIBUTOS ==
POSSAM SER CRIADOS: == NOME, COR, VELOCIDADE MÁXIMA, NÍVEL ATUAL DA BATERIA, 
PESO DA CARGA MÁXIMA SUPORTADA, TIPO DE TRAÇÃO E PRESENÇA OU NÃO DE ANTENA.
===============================================================================
== ATRIBUTO ==
A IDEIA DE == CLASSE == É SEMELHANTE À IDEIA DE REGISTRO (STRUCUT) NA LINGUAGEM C,
UMA VEZ QUE ESSES ATRIBUTOS DA CLASSE SÃO SEMELHANTES AOS CAMPOS (VARIÁVEIS) DE UM
REGISTRO. OS DIVERSOS CAMPOS SÃO ACESSADOS POR UM == ÚNICO PONTEIRO == ASSIM COMO
OS ATRIBUTOS DA CLASSE SÃO ACESSADOS POR UM == ÚNICO OBJETO ==
==================================================================================
== MÉTODO ==
IM OUTRO ELEMENTO IMPORTANTE DE UMA CLASSE SÃO OS MÉTODOS. UM MÉTODO DÁ AO OBJETO
DA CLASSE A CAPACIDADE DE EXECUTAR ALGUM TIPO DE AÇÃO, COMPORTAMENTO OU PROCESSAMENTO.
UM ROBÔ É CAPAZ DE EXECUTAR UMA SÉRIE DE AÇÕES --- O NOSSO ROBÔ MODELADO É CAPAZ DE 
SE MOVER, PEGAR CAIXAS, ENTREGAR AS CAIXAS E ATÉ MESMO FALAR.
======================================================================================
IMPRESSÃO:
-> SYSTEM.OUT.PRINTLN -> IMPRIME E PULA DE LINHA
-> SYSTEM.OUT.PRINT   -> IMPRIME
-> SYSTEM.OUT.PRINTF  -> RECEBE DOIS ARGUMENTOS: O PRIMEIRO, UM LITERAL, PARA
FORMATAÇÃO DA IMPRESSÃO E OUTRO, UMA LISTA COM OS OBJETOS A SEREM IMPRESSOS.
-> SYSTEM.OUT.PRINTF  -> UTILIZADO NA CONCATENAÇÃO DE STRINGS COM O OPERADOR '+'
=================================================================================


MODELAGEM DO ROBÔ */
public class Robo {
    String nome = "R-ATM";
    float peso = 70;
    float velocidadeMax = 5;
    float pesoCargaMax = 20;
    String tipoTracao = "esteira";
    float localizacaoX = 50;
    float localizacaoY = 50;
    public void move(float x, float y){
        localizacaoX = x;
        localizacaoY = y;
    }
    public void printStatus(){
        System.out.println("-----------Info R-ATM-----------");
        System.out.println("Nome do Robô: " +nome);
        System.out.println("Peso do Robô: " +peso);
        System.out.println("Velocidade Máxima: " +velocidadeMax);
        System.out.println("Carga Máxima: " +pesoCargaMax);
        System.out.println("Tipo de Tração: " +tipoTracao);
        System.out.println("Posição X do Robô: " +localizacaoX);
        System.out.println("Posição Y do Robô: " +localizacaoY);
        System.out.println("----------------------------------");
    }
    public static void main(String[] args){
        Robo objRobo = new Robo();
        objRobo.printStatus();
        objRobo.move(60, 50);
        objRobo.printStatus();
        objRobo.move(65, 55);
        objRobo.printStatus();
    }
}

// MODELAGEM DA PESSOA 
public class Pessoa {
int idade;
String sexo;
String nome;
        public static void main(String[] args){
            Pessoa qualquer = new Pessoa();
                qualquer.nome = "Maria";
                qualquer.idade = 22;
                qualquer.sexo = "F";
            System.out.println("O nome é: " +qualquer.nome);
            System.out.println("A idade é: "+qualquer.idade);
            System.out.println("O sexo é: "+qualquer.sexo);
        }
}