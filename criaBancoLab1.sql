DROP TABLE IF EXISTS FILME_ATOR;
DROP TABLE IF EXISTS ATOR;
DROP TABLE IF EXISTS LOC_FITA;
DROP TABLE IF EXISTS FITA;
DROP TABLE IF EXISTS FILME;
DROP TABLE IF EXISTS CATEGORIA;
DROP TABLE IF EXISTS LOCACAO;
DROP TABLE IF EXISTS CLIENTE;

CREATE TABLE  CLIENTE	(codCli INTEGER UNSIGNED PRIMARY KEY AUTO_INCREMENT, nome varchar(65) NOT NULL, endereco varchar(150) NOT NULL,	fone INTEGER);



CREATE TABLE LOCACAO (
	codLoc INTEGER UNSIGNED PRIMARY KEY AUTO_INCREMENT,
	codCli INTEGER UNSIGNED references Cliente(codCli),
	dtInicio date,
	dtFim	date
);


CREATE TABLE  CATEGORIA(
	 codCat		INTEGER UNSIGNED PRIMARY KEY AUTO_INCREMENT,
	 descricao	varchar(30) NOT NULL
);



CREATE TABLE FILME
	(codFilme	INTEGER UNSIGNED PRIMARY KEY AUTO_INCREMENT,
	 titulo		varchar(65) NOT NULL,
	 codCat		INTEGER UNSIGNED,
	 FOREIGN KEY(codCat) references CATEGORIA(codCat));


CREATE TABLE FITA
	(codFita	INTEGER UNSIGNED PRIMARY KEY AUTO_INCREMENT,
	 codFilme	INTEGER UNSIGNED references Filme(codFilme),
	 parte		char(1) );



CREATE TABLE LOC_FITA
	(codFita	INTEGER UNSIGNED references Fita(CodFita),
	 codLoc		INTEGER UNSIGNED references Locacao(codLoc),
	PRIMARY KEY (codFita, codLoc));



CREATE TABLE ATOR
	(codAtor	INTEGER UNSIGNED PRIMARY KEY AUTO_INCREMENT,
	 nreal		varchar(65) NOT NULL,
	 nFan		varchar(65) NOT NULL,
	 dtNasc		date);


CREATE TABLE FILME_ATOR
	(codFilme	INTEGER UNSIGNED references Filme(codFilme),
	 codAtor	INTEGER UNSIGNED references Ator(codAtor));


-- ALTER TABLE FILME_ATOR
-- ADD PRIMARY KEY (codFilme, codAtor);



-- insert into CLIENTE(codCli, nome, endereco, fone) values(1, 'Maria da Silva', 'BSB', '12341234');
-- insert into CLIENTE(codCli, nome, endereco, fone) values(2, 'Jose Geraldo', 'Sao Paulo', '13243647');
-- insert into CLIENTE(codCli, nome, endereco, fone) values(3, 'Marcos da Silva', 'Rio de Janeiro', '34678923');
-- insert into CLIENTE(codCli, nome, endereco, fone) values(4, 'Marcelo Oliveira', 'Belem', '13579323');
-- insert into CLIENTE(codCli, nome, endereco, fone) values(5, 'Marcos Antonio', 'Para', '73839581');



-- insert into LOCACAO(codLoc, codCli, dtInicio, dtFim) values(1, 1, '2009-02-02', '2009-02-05');
-- insert into LOCACAO(codLoc, codCli, dtInicio, dtFim) values(2, 1, '2009-02-02', '2009-02-05');
-- insert into LOCACAO(codLoc, codCli, dtInicio, dtFim) values(3, 2, '2009-05-02', '2009-05-05');
-- insert into LOCACAO(codLoc, codCli, dtInicio, dtFim) values(4, 3, '2009-02-10', '2009-02-12');
-- insert into LOCACAO(codLoc, codCli, dtInicio, dtFim) values(5, 3, '2009-02-15', '2009-02-17');


-- insert into FITA(codFita, codFilme, parte) values(1, 1, '1');
-- insert into FITA(codFita, codFilme, parte) values(2, 1, '1');
-- insert into FITA(codFita, codFilme, parte) values(3, 2, '1');
-- insert into FITA(codFita, codFilme, parte) values(4, 2, '2');
-- insert into FITA(codFita, codFilme, parte) values(5, 3, '1');

-- insert into LOC_FITA(codLoc, codFita) values(1, 1);
-- insert into LOC_FITA(codLoc, codFita) values(2, 2);
-- insert into LOC_FITA(codLoc, codFita) values(3, 3);
-- insert into LOC_FITA(codLoc, codFita) values(4, 4);
-- insert into LOC_FITA(codLoc, codFita) values(5, 5);

-- insert into CATEGORIA(codCat, descricao) values(1, 'Acao');
-- insert into CATEGORIA(codCat, descricao) values(2, 'Comedia');
-- insert into CATEGORIA(codCat, descricao) values(3, 'Desenho');
-- insert into CATEGORIA(codCat, descricao) values(4, 'Terror');
-- insert into CATEGORIA(codCat, descricao) values(5, 'Romance');

-- insert into FILME(codFilme, titulo, codCat) values(1, 'Titanic', 5);
-- insert into FILME(codFilme, titulo, codCat) values(2, 'Se eu fosse voce', 3);
-- insert into FILME(codFilme, titulo, codCat) values(3, 'Poderoso Chefao', 1);
-- insert into FILME(codFilme, titulo, codCat) values(4, 'Os Vagabundos Trapalhoes', 2);
-- insert into FILME(codFilme, titulo, codCat) values(5, 'Massaropi', 2);


-- insert into ATOR(codAtor, nreal, nFan, dtNasc) values(1, 'Leonardo DiCaprio', 'Leonardo DiCaprio', '1980-03-19');
-- insert into ATOR(codAtor, nreal, nFan, dtNasc) values(2, 'Kate Winslet', 'Kate Winslet', '1983-12-19');
-- insert into ATOR(codAtor, nreal, nFan, dtNasc) values(3, 'Antonio de Carvalho Barbosa', 'Toni Ramos', '1956-03-01');
-- insert into ATOR(codAtor, nreal, nFan, dtNasc) values(4, 'Antonio Rentao Aragao', 'Didi', '1980-05-20');
-- insert into ATOR(codAtor, nreal, nFan, dtNasc) values(5, 'Gloria Pires', 'Gloria Pires', '1980-07-19');


-- insert into FILME_ATOR(codFilme, codAtor) values(1, 1);
-- insert into FILME_ATOR(codFilme, codAtor) values(1, 2);
-- insert into FILME_ATOR(codFilme, codAtor) values(2, 3);
-- insert into FILME_ATOR(codFilme, codAtor) values(2, 5);
-- insert into FILME_ATOR(codFilme, codAtor) values(4, 4);
