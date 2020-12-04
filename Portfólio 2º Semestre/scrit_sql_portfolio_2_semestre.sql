/* CRIANDO BANCO DE DADOS */
create database fazenda_db
default character set utf8
default collate utf8_general_ci;

/* UTILIZANDO BANCO DE DADOS */
use fazenda_db;

/* TABELA PESSOAS */
create table pessoas (
id int not null auto_increment,
nome varchar (100) not null,
documento int not null,
endereco varchar (150) not null,
cidade varchar (50) not null,
estado varchar (2) not null,
primary key (id)
);

/* INSERINDO AS DIFERENTES PESSOAS */
insert into pessoas values
(default, 'João Maria', '1', 'FazendaTech', 'Uberaba', 'MG'),
(default, 'Pedro José', '1', 'FazendaTech', 'Uberaba', 'MG'),
(default, 'Ana Clara', '1', 'FazendaTech', 'Uberaba', 'MG'),
(default, 'Maria Beatriz', '1', 'FazendaTech', 'Uberaba', 'MG'),
(default, 'Antônio Carlos', '1', 'FazendaTech', 'Uberaba', 'MG'),
(default, 'Valquiria Sanchez', '1', 'Av Central, 1', 'Uberaba', 'MG'),
(default, 'Ronaldo Batista', '1', 'Av Geral, 34', 'Uberaba', 'MG'),
(default, 'Máquinas Agricolas', '2', 'Av Comércio, 10', 'Uberaba', 'MG'),
(default, 'Cooperativa Coperar', '2', 'Av Comércio, 20', 'Uberaba', 'MG'),
(default, 'Sementes SA', '2', 'Av Comércio, 30', 'Uberaba', 'MG'),
(default, 'Posto BR', '2', 'Av Comércio, 40', 'Uberaba', 'MG'),
(default, 'Ferramentas Agricolas', '2', 'Av Comércio, 50', 'Uberaba', 'MG'),
(default, 'AgroFertil Fert', '2', 'Av Comércio, 60', 'Uberaba', 'MG'),
(default, 'Mêcanica Agricola', '2', 'Av Comércio, 70', 'Uberaba', 'MG');

/* EXIBINDOS OS DADOS INSERIDOS */
select * from pessoas;

/* EXIBINDO OS DADOS DE PESSOAS CADASTRADOS COMO 1
PESSOAS FÍSICAS */
select * from pessoas
where documento = 1;

/* TABELA PESSOAS FÍSICA */
create table pessoa_fisica (
id int not null,
cpf varchar (20) not null,
nascimento date not null,
primary key (cpf),
foreign key (id) references pessoas (id)
);

insert into pessoa_fisica values
('1', '00011122233', '1984-12-05'),
('2', '11122233344', '1985-06-26'),
('3', '22233344455', '1990-09-11'),
('4', '33344455566', '1993-10-24'),
('5', '44455566677', '1994-06-11'),
('6', '55566677788', '1998-03-28'),
('7', '66677788899', '2000-04-18');

/* EXIBINDOS OS DADOS INSERIDOS */
select * from pessoa_fisica;

/* 	QUERY DE CONSULTA
RETORNA O ID DA TABELA PESSOA COMPARADO COM O ID DA TABELA PESSOA_FISICA,
O NOME DA TABELA PESSOA E O NÚMERO DO CPF DA TABELA PESSOA_FISICA */
select p.nome, p.id, pf.cpf from pessoas as p
join pessoa_fisica as pf
on p.id = pf.id
order by p.id;

/* TABELA FUNCIONÁRIOS */
create table funcionarios (
id int not null,
ctps varchar (20) not null,
primary key (id),
foreign key (id) references pessoa_fisica (id)
);

insert into funcionarios values
('1', '11223344556677889900'),
('2', '22334455667788990011'),
('3', '33445566778899001122'),
('4', '44556677889900112233'),
('5', '55667788990011223344'),
('6', '66778899001122334455'),
('7', '77889900112233445566');

/* EXIBINDO OS DADOS INSERIDOS */
select * from funcionarios;

/* QUERY DE CONSULTA
RETORNA O ID DAS TABELAS PESSOAS, PESSOA_FISICA E FUNCIONARIOS; QUE SÃO OS MESMOS
DA TABELA PESSOAS RETORNA O NOME
DA TABELA PESSOA_FISICA RETORNA O CPF
DA TABELA FUNCIONARIOS RETORNA A CTPS */
select p.id, p.nome, pf.cpf, func.ctps from pessoas as p
join funcionarios as func
on p.id = func.id
join pessoa_fisica as pf
on pf.id = func.id
order by p.id;

/* TABELA ADMINISTRADOR
A TABELA LEVARÁ EM CONTA A PERMISSÃO TOTAL OU PARCIAL DOS ADMINISTRADORES */
create table administrador (
id int not null,
permissao varchar (20) not null,
primary key (id),
foreign key (id) references pessoa_fisica (id)
);

insert into administrador values
('6', 'PARCIAL'),
('7', 'TOTAL');

/* EXIBINDO OS DADOS INSERIDOS */
select * from administrador;

/* QUERY COM CONSULTA
O RETORNO SERÃO TODOS OS DADOS DOS ADMINISTRADORES
ID GERAL, NOME, CPF, CTPS, ENDEREÇO, CIDADE E GRAU DE PERMISSÃO */
select p.id, p.nome, pf.cpf, func.ctps, p.endereco, p.cidade, adm.permissao from pessoas as p
join administrador as adm
join pessoa_fisica as pf
join funcionarios as func
where pf.id = adm.id and p.id = adm.id and func.id = adm.id;

/* TABELA PESSOA JURÍDICA 
TABELA PARA COMPRA E VENDAS DENTRO DA FAZENDA */
create table pessoa_juridica (
id int not null,
cnpj varchar (20) not null,
data_compra date,
data_venda date,
valor_compra float,
valor_venda float,
primary key (id),
foreign key (id) references pessoas (id)
);

/* EXIBINDO AS PESSOAS QUE ESTÃO CADASTRADAS COMO "2"
PESSOA JURÍDICA */
select * from pessoas
where documento = 2;

/* AQUI TEM-SE O CUIDADO DE CONSIDERAR O ID PRINCIPAL E SEGUIR ESSE ÍNDICE */
insert into pessoa_juridica values
('8', '00.111.222/3333-44', '2020-11-01', null, '615000', null), /* COMPRA */
('9', '11.222.333/4444-55', null, '2020-01-01', null, '7948355'), /* VENDA */
('10', '22.333.444/5555-66', '2020-10-15', null, '88000', null), /* COMPRA */
('11', '33.444.555/6666-77', '2020-11-01', null, '4567', null), /* COMPRA */
('12', '44.555.666/7777-88', '2020-11-01', null, '80000', null), /* COMPRA */
('13', '55.666.777/8888-99', '2020-10-01', null, '100000', null), /* COMPRA */
('14', '66.777.888/9999-00', '2020-09-01', null, '500000', null); /* COMPRA */

/* EXIBINDO OS DADOS INSERIDOS */
select * from pessoa_juridica;

/* QUERY COM CONSULTA
O RETORNO SERÃO TODOS OS NOMES, CNPJ, DATA DA COMPRA E VALOR DA COMPRA
DE APENAS PESSOAS JURÍDIC
AS E QUE A FAZENDA TENHA FEITO COMPRAS */
select p.nome, pj.cnpj, pj.data_compra, pj.valor_compra from pessoas as p
join pessoa_juridica as pj
where p.documento = 2 and p.id = pj.id and pj.valor_compra is not null;

/* QUERY COM CONSULTA
O RETORNO SERÃO TODOS OS NOMES, CNPJ, DATA DA VENDA E VALOR DA VENDA
DE APENAS AS PESSOAS JURÍDICAS E QUE A FAZENDA TENHA FEITO VENDAS */
select p.nome, pj.cnpj, pj.data_venda, pj.valor_venda from pessoas as p
join pessoa_juridica as pj
where p.documento = 2 and p.id = pj.id and pj.valor_venda is not null;

/* QUERY COM CONSULTA
RETORNA O VALOR TOTAL DE VENDA DE TODAS AS EMPRESAS */
select sum(valor_venda) as valor_final_venda from pessoa_juridica
where valor_venda is not null;

/* QUERY COM CONSULTA
RETORNA O VALOR TOTAL DE COMPRAS DE TODAS AS EMPRESAS */
select sum(valor_compra) as valor_final_compra from pessoa_juridica
where valor_compra is not null;

/* TABELA VAREJISTAS 
TABELA PARA CADASTRO DE FORNECEDORES */
create table varejistas (
id int not null auto_increment,
id_pj int not null,
nome_produto varchar (150) not null,
valor_produto float not null,
primary key (id),
foreign key (id_pj) references pessoas (id)
);

insert into varejistas values
('1', '8', 'Trator', '5500'),
('2', '8', 'Colhedeira', '7000'),
('3', '8', 'Arado', '3000'),
('4', '9', 'Leite', '3'),
('5', '9', 'Gado', '1300'),
('6', '9', 'Café', '7000'),
('7', '10', 'Semente Café', '300'),
('8', '11', 'Gasolina', '5'),
('9', '12', 'Enxada', '25'),
('10', '12', 'Rastelo', '35'),
('11', '12', 'Facão', '100'),
('12', '12', 'Chave', '10'),
('13', '13', 'Fertilizante', '250'),
('14', '13', 'Adubo', '150'),
('15', '14', 'Manutenção', '500'),
('16', '14', 'Serviços', '100'),
('17', '14', 'Troca', '1000'),
('18', '14', 'Visita', '350');

/* EXIBINDO OS DADOS INSERIDOS */
select * from varejistas;

/* QUERY CONSULTA 
CONSULTA TODOS OS PRODUTOS VINDO DO ID 8 DE PESSOAS
ID PODE SER MUDADO PARA DIFERENTES LOJAS */
select var.id, p.nome, var.nome_produto, var.valor_produto from varejistas as var
join pessoas as p
where var.id_pj = 8 and p.id = 8;

/* TABELA DE EQUIPAMENTOS */
create table equipamentos (
id int not null auto_increment,
codigo_varejista int not null,
nome_equipamento varchar (100) not null,
estado_equipamento varchar (50) not null,
primary key (id),
foreign key (codigo_varejista) references pessoas (id)
);

insert into equipamentos values
(default, '8', 'Trator', 'Bom Estado'),
(default, '8', 'Colhedeira', 'Bom Estado'),
(default, '8',  'Arado', 'Bom Estado'),
(default, '12', 'Enxada', 'Novo'),
(default, '12', 'Rastelo', 'Bom Estado'),
(default, '12', 'Facão', 'Conservado'),
(default, '12', 'Chave', 'Troca');

/* EXIBINDO OS DADOS INSERIDOS */
select * from equipamentos;

/* QUERY COM CONSULTA
CONSULTA TODOS OS EQUIPAMENTOS NA FAZENDA,
ID, NOME DO EQUIPAMENTO E ESTADO DO EQUIPAMENTOS SÃO DA TABELA EQUIPAMENTOS
O NOME, VEM DA TABELA PESSOAS USANDO A REFERÊNCIA CÓDIGO DO VAREJISTA */
select eq.id, p.nome, eq.nome_equipamento, eq.estado_equipamento from equipamentos as eq
join pessoas as p
where eq.codigo_varejista = p.id;

/* TABELA DE PRODUTOS */
create table produtos (
id int not null auto_increment,
codigo_varejista int not null,
codigo_produto int not null,
quantidade_produto int,
primary key (id),
foreign key (codigo_varejista) references pessoas (id),
foreign key (codigo_produto) references varejistas (id)
);

insert into produtos values
(default, '9', '4', '5000'),
(default, '9', '5', '2459'),
(default, '9', '6', '2000'),
(default, '10', '7', null),
(default, '11', '8', null),
(default, '13', '14', null);

/* EXIBINDO DADOS INSERIDOS */
select * from produtos;

/* QUERY COM CONSULTA 
CONSULTA O NOME DO VAREJISTA, O NOME DO PRODUTO E SUA QUANTIDADE
QUANTIDADE RECEBEU VALORES DO TIPO NULL QUANDO NÃO SÃO POSSÍVEIS DE SEREM CONTABILIZADOS
EXEMPLO: QUANTOS LITROS DE GASOLINA TEM DE ESTOQUE? OU NO POSTO? */
select p.nome, v.nome_produto, prod.quantidade_produto from produtos as prod
join pessoas as p
join varejistas as v
where p.id = prod.codigo_varejista and v.id = prod.codigo_produto;

/* TABELA PLANTIO */
create table plantio (
id int not null auto_increment,
funcionario int not null,
produto int,
data_plantio date,
data_manutencao date,
data_colheita date,
primary key (id),
foreign key (funcionario) references pessoas (id),
foreign key (produto) references varejistas (id)
);

insert into plantio values
(default, '1', '7', '2020-11-01', null, '2021-05-01'),
(default, '1', '14', '2020-11-02', null, null),
(default, '2', '1', null, '2020-10-25', null),
(default, '2', '3', null, '2020-10-31', null),
(default, '2', '2', null, '2021-05-01', null);

/* EXIBINDO DADOS INSERIDOS */
select * from plantio;

/* QUERY COM CONSULTA
RETORNA O ID DE PLANTIO, O NOME DO FUNCIONÁRIO RESPONSÁVEL, O NOME DO PRODUTO UTILIZADO 
A DATA DO PLANTIO, A DATA DA MANUTENÇÃO E A DATA DA COLHEITA */
select pl.id, p.nome, var.nome_produto, pl.data_plantio, pl.data_manutencao, pl.data_colheita from plantio as pl
join pessoas as p join varejistas as var
where pl.funcionario = p.id and pl.produto = var.id;

/* TABELA LEITE */
create table leite (
id int not null auto_increment,
funcionario int not null,
raca_vaca varchar (50),
data_ordenha date,
temperatura_leite float,
inseminacao float,
data_inseminacao date,
estimativa_parto date,
primary key (id),
foreign key (funcionario) references pessoas (id)
);

insert into leite values
(default, '3', 'Nelore', '2020-11-02', '33.5', false, null, null),
(default, '3', 'Zebu', '2020-11-02', '33.7', false, null, null),
(default, '4', 'Gir', '2020-11-02', '34.1', false, null, null),
(default, '4', 'Girolando', '2020-11-02', '33.9', true, '2020-10-01', '2021-08-30'),
(default, '5', 'Holandesa', '2020-11-02', '33.6', true, '2020-10-01', '2021-08-30'),
(default, '5', 'Holandesa', '2020-11-02', '33.8', false, null, null);

/* EXIBINDO OS DADOS INSERIDOS */
select * from leite;

/* QUERY COM CONSULTA
RETORNA O ID DO LEITE, O NOME DO FUNCIONÁRIO DA TABELA PESSOA E TODOS OS ATRIBUTOS DA TABELA LEITE */
select l.id, p.nome, l.raca_vaca, l.data_ordenha, l.temperatura_leite, l.inseminacao, l.data_inseminacao, l.estimativa_parto from pessoas as p
join leite as l
where l.funcionario = p.id;
