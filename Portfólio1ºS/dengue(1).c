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

//DEFINIÇÃO DAS STRUCUTS
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

//PROTOTIPAÇÃO
void Denuncia_Inserir(FilaDenuncias *fila);
void Denuncia_Excluir(FilaDenuncias *fila);
void Denuncia_Imprimir(FilaDenuncias *fila);
int Menu_Executar();
void Pausa();
void Remover_EOL(char* str);
	
int main(){
	// DECLARAÇÕES
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
				printf("Opcao Inválida \n\n");
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
		printf("Você atingiu a quantidade de Denúncias em Análise...\n");
		printf("Aguarde até que as suas denúncias sejam verificadas!\n");
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
		
		printf("Digite o número do Imóvel: ");
		scanf("%d", &(fila->denuncias[i].numero));

		fila->tamanhoDaFila++;

		printf("Denúncia cadastrada!\n");
	}
}

//EXCLUIR O PRIMEIRO ELEMENTO DA FILA
void Denuncia_Excluir(FilaDenuncias *fila){
	if (fila->tamanhoDaFila == 0){
		printf("Não há Denúncias cadastradas...\n");
		printf("Cadastre as suas denúncias...\n\n");
	}else {
		int i;
		for (i = 0; i < fila->tamanhoDaFila; i++){
        		fila->denuncias[i] = fila->denuncias[i+1];
        	}
        	fila->tamanhoDaFila--;
        	
        	printf("Denúncia excluída!\n");
        }      
}

//IMPRIMIR O CONTEÚDO DAS DENÚNCIAS
void Denuncia_Imprimir(FilaDenuncias *fila){
	int i;
	if (fila->tamanhoDaFila == 0){
		printf("Não há denúncias cadastradas.\n");
		printf("Cadastre alguma denúncia...\n\n");
	}else {
		printf("DENÚNCIAS CADASTRADAS\n");
		for (i = 0; i < fila->tamanhoDaFila; i++){
			printf("\n");
			printf("Estado: %s \n", fila->denuncias[i].estado);
			printf("Cidade: %s \n", fila->denuncias[i].cidade);
			printf("Bairro: %s \n", fila->denuncias[i].bairro);
			printf("Rua: %s \n", fila->denuncias[i].rua);
			printf("Número: %d \n\n", fila->denuncias[i].numero);
		}
	}
}

int Menu_Executar(){
	int op;
	printf("Escolha uma opção:\n");
	printf("1- Cadastrar Denúncia\n");
	printf("2- Exibir Denúncia\n");
	printf("3- Excluir Denúncia\n");
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
