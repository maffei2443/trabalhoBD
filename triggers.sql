DELETE FROM Partido WHERE id IN (
    SELECT * FROM (
        SELECT Partido.id FROM Candidato, Partido WHERE Candidato.id = Partido.id GROUP BY Partido.id HAVING ( COUNT(Candidato.id) = 0 )
    ) AS p
)