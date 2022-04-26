update Films.Atores SET nomeAtor = TRIM(TRAILING '\n' FROM nomeAtor);
update Films.Diretores SET nomeDiretor = TRIM(TRAILING '\n' FROM nomeDiretor)
