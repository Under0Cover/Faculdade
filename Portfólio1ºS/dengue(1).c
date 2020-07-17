//BIBLIOTECAS
#include <stdio.h>
#include <stdlib.h>
#include <locale.h>
#include <string.h>

//CONSTANTES
#define FILA_TAMANHO 20
#define ESTADO_TAMANHO 51+1
#define CIDADE_TAMANHO 51+1
#define BAIRRO_TAMANHO 51+1
#define RUA_TAMANHO 101+1

//DEFINI��O DAS STRUCUTS
typedef struct Denuncia {
	char estado[ESTADO_TAMANHO];
	char cidade[CIDADE_TAMANHO];
	char bairro[BAIRRO_TAMANHO];
	char rua[RUA_TAMANHO];
	int numero;
} Denuncia;

typedef struct FilaDenuncias {
	Denuncia denuncias[FILA_TAMANHO];
	int tamanhoDaFila;
} FilaDenuncias;

//PROTOTIPA��O
void Denuncia_Inserir(FilaDenuncias *fila);
void Denuncia_Excluir(FilaDenuncias *fila);
void Denuncia_Imprimir(FilaDenuncias *fila);
int Menu_Executar();
void Pausa();
void Remover_EOL(char* str);
	
int main(){
	// DECLARA��ES
	int op = -1;
	FilaDenuncias filaDenuncias;
	filaDenuncias.tamanhoDaFila = 0;
	
	// INCLUINDO PT-BR
	setlocale(LC_ALL, "Portuguese");
	
	printf("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n");
	printf("X                            X\n");
	printf("X         ZER@DENGUE         X\n");
	printf("X                            X\n");
	printf("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n");
	printf("\n");
	printf("\n");
	printf("------------------------------\n");
	while ((op = Menu_Executar()) != 0) {
		switch (op){
			case 1:
				Denuncia_Inserir(&filaDenuncias);
				break;
			case 2:
				Denuncia_Imprimir(&filaDenuncias);
				break;
			case 3:
				Denuncia_Excluir(&filaDenuncias);
				break;
			default:
				printf("Opcao Inv�lida \n\n");
				break;
		}
		Pausa();
	}
	return 0;
}



//ADICIONAR ELEMENTO AO FIM DA FILA
void Denuncia_Inserir(FilaDenuncias *fila){
	int i = fila->tamanhoDaFila;
	if (fila->tamanhoDaFila == FILA_TAMANHO){
		printf("Voc� atingiu a quantidade de Den�ncias em An�lise...\n");
		printf("Aguarde at� que as suas den�ncias sejam verificadas!\n");
	} else {
		while(getchar() != '\n');
		
		printf("Digite o Estado: ");
		fgets(fila->denuncias[i].estado, ESTADO_TAMANHO, stdin);
		Remover_EOL(fila->denuncias[i].estado);
		
		printf("Digite a Cidade: ");
		fgets(fila->denuncias[i].cidade, CIDADE_TAMANHO, stdin);
		Remover_EOL(fila->denuncias[i].cidade);
		
		printf("Digite o Bairro: ");
		fgets(fila->denuncias[i].bairro, BAIRRO_TAMANHO, stdin);
		Remover_EOL(fila->denuncias[i].bairro);
		
		printf("Digite a Rua: ");
		fgets(fila->denuncias[i].rua, RUA_TAMANHO, stdin);
		Remover_EOL(fila->denuncias[i].rua);
		
		printf("Digite o n�mero do Im�vel: ");
		scanf("%d", &(fila->denuncias[i].numero));

		fila->tamanhoDaFila++;

		printf("Den�ncia cadastrada!\n");
	}
}

//EXCLUIR O PRIMEIRO ELEMENTO DA FILA
void Denuncia_Excluir(FilaDenuncias *fila){
	if (fila->tamanhoDaFila == 0){
		printf("N�o h� Den�ncias cadastradas...\n");
		printf("Cadastre as suas den�ncias...\n\n");
	}else {
		int i;
		for (i = 0; i < fila->tamanhoDaFila; i++){
        		fila->denuncias[i] = fila->denuncias[i+1];
        	}
        	fila->tamanhoDaFila--;
        	
        	printf("Den�ncia exclu�da!\n");
        }      
}

//IMPRIMIR O CONTE�DO DAS DEN�NCIAS
void Denuncia_Imprimir(FilaDenuncias *fila){
	int i;
	if (fila->tamanhoDaFila == 0){
		printf("N�o h� den�ncias cadastradas.\n");
		printf("Cadastre alguma den�ncia...\n\n");
	}else {
		printf("DEN�NCIAS CADASTRADAS\n");
		for (i = 0; i < fila->tamanhoDaFila; i++){
			printf("\n");
			printf("Estado: %s \n", fila->denuncias[i].estado);
			printf("Cidade: %s \n", fila->denuncias[i].cidade);
			printf("Bairro: %s \n", fila->denuncias[i].bairro);
			printf("Rua: %s \n", fila->denuncias[i].rua);
			printf("N�mero: %d \n\n", fila->denuncias[i].numero);
		}
	}
}

int Menu_Executar(){
	int op;
	printf("Escolha uma op��o:\n");
	printf("1- Cadastrar Den�ncia\n");
	printf("2- Exibir Den�ncia\n");
	printf("3- Excluir Den�ncia\n");
	printf("0- Sair\n\n");
	printf("Digite aqui: ");
	scanf("%d", &op);
	return op;
}

void Pausa()
{
	printf("Pressione enter para continuar...\n");
	while(getchar() != '\n');
	getchar();
}

void Remover_EOL(char* str)
{
	char* posicao = strchr(str, '\n');
	if (posicao != NULL)
		*posicao = '\0';
}
