/* CRIANDO O DATABASE */
create database curso_faculdade;

/* USANDO O DATABASE CRIADO */
use curso_faculdade;

/* CRIANDO A TABELA ALUNO */
create table if not exists aluno (
id int (11) not null auto_increment,
nome varchar(45) not null,
profissao varchar (30) not null,
nascimento date not null,
primary key (id)
) default charset = utf8;

/* CRIANDO A TABELA CURSO */
create table if not exists curso (
idcurso int (11) not null auto_increment,
nome_curso varchar (30) not null,
descricao_curso varchar (75) not null,
carga int (3) not null,
totaulas int (3) not null,
ano year not null,
primary key (idcurso)
) default charset = utf8;

/* DEFININDO AS CHAVES ESTRANGERIAS */
/* CHAVE ESTRANGEIRA NA TABELA ALUNO */
alter table aluno
add column curso_matriculado int;

/* curso_matriculado será a chave estrangeira do ID da tabela CURSO */
alter table aluno
add foreign key (curso_matriculado)
references curso(idcurso);

desc aluno;
desc curso;

/* INSERINDO DADOS EM CURSO */
insert into curso
(nome_curso, descricao_curso, carga, totaulas, ano) values
('Lógica de Programação', 'Introdução à Lógica de Programação', '40', '35', '2020'),
('Introdução à Web','Primeiros passos no cainho da programação', '50','44','2020'),
('HTML5', 'Introdução ao HTML5', '30','20','2020'),
('CSS', 'Primeiros passos no CSS3', '30','20','2020'),
('JavaScript', 'JavaScript para iniciantes', '45','30','2020'),
('Front End','Projetos práticos em HTML, CSS e JS','70','50','2020');

select * from curso;
desc aluno;

/* INSERINDO DADOS EM ALUNO */
insert into aluno
(nome, profissao, nascimento, curso_matriculado) values
('Tatiana', 'Professora', '1985-10-22','4'),
('João Pedro', 'Estudante', '2008-01-28','1'),
('Cristian', 'Mêcanico', '1987-10-11','6'),
('Lucas', 'Estudante', '2011-12-03','3'),
('Gustavo', 'Auxiliar Administrativo', '1986-12-02','5'),
('Matias', 'Entregador', '2002-08-17','2'),
('Paulo', 'Atendente', '1996-06-03','6');

select * from aluno;
/* ---------------------- */

desc aluno;
desc curso;
select * from aluno;
select * from curso;

/* SCRIPT QUE SELECIONA O ALUNO, A PROFISSAO 
DAS TABELAS ALUNO E SELECIONA O NOME DO CURSO DA TABELA CURSO 
SERÁ MOSTRADO O NOME DO ALUNO, SUA PROFISSAO E O CURSO MATRICULADO
POR ORDEM ALFABETICA */

select a.nome, a.profissao, c.nome_curso
from aluno as a left join curso as c
on c.idcurso = a.curso_matriculado
order by a.nome;

