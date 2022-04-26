CREATE TABLE Films.Filmes (
	id integer PRIMARY KEY,
    nomeFilme varchar(200) NOT NULL,
    anoFilme varchar(10)
);

CREATE TABLE Films.Diretores (
    idDiretor integer NOT NULL,
    nomeDiretor varchar(100)
);

CREATE TABLE Films.Atores (
	idAtor integer NOT NULL,
	nomeAtor varchar(100)
);


