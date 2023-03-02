CREATE TABLE Distributor (
    id_distributor INT AUTO_INCREMENT ,
    name_distributor TEXT, 
    Rating_stores TINYINT UNSIGNED NOT NULL CHECK(Rating_stores BETWEEN 0 AND 5 ),
    Rating_costumers TINYINT UNSIGNED NOT NULL CHECK (Rating_costumers BETWEEN 0 AND 5 ),

    PRIMARY KEY (id_distributor)
);

CREATE TABLE Shift (
   date_shift DATE,
   ID_distributor_shift INT,
   acceptance_rate FLOAT(9),
   active BOOLEAN,
   hours_expected FLOAT(20),
   hours_worked FLOAT(20),
   Sinepeia FLOAT (20),
   Total_aitimata_per_shift INT,
   PRIMARY KEY (date_shift, ID_distributor_shift),
   FOREIGN KEY(ID_distributor_shift) REFERENCES Distributor(id_distributor)
);
CREATE TABLE Aitima (
    id_aitimatos INT AUTO_INCREMENT,
    id_distr INT,
    dmin FLOAT,
    accepted BOOLEAN,
    declined BOOLEAN,
    PRIMARY KEY (id_aitimatos),
    FOREIGN KEY (id_distr) REFERENCES Distributor (id_distributor)
);


CREATE TABLE RatingFromStore (
 id_di INT, 
 dat_shift DATE,
 id_aitim INT,
 Rating_store TINYINT UNSIGNED NOT NULL CHECK(Rating_store BETWEEN 0 AND 5 ),
FOREIGN KEY (id_di) REFERENCES Distributor (id_distributor),
FOREIGN KEY (dat_shift) REFERENCES Shift (date_shift),
FOREIGN KEY (id_aitim) REFERENCES Aitima (id_aitimatos)
);

CREATE TABLE RatingFromCostumer (
 id_rating_costumer INT, 
 dat_shif_costumer DATE,
 id_aitimatos_costumer INT,
 Rating_costumer TINYINT UNSIGNED NOT NULL CHECK(Rating_costumer BETWEEN 0 AND 5 ),
FOREIGN KEY (id_rating_costumer ) REFERENCES Distributor (id_distributor),
FOREIGN KEY (dat_shif_costumer) REFERENCES Shift (date_shift),
FOREIGN KEY (id_aitimatos_costumer) REFERENCES Aitima (id_aitimatos)
);




CREATE TABLE WorstDistributors (
    hmera_worst DATE,
    Id_worst_distributor INT,
    Ranking_worst_costumer TINYINT UNSIGNED NOT NULL CHECK(Ranking_worst_costumer BETWEEN 0 AND 10),
    Ranking_worst_store TINYINT UNSIGNED NOT NULL CHECK(Ranking_worst_store BETWEEN 0 AND 10),
    Ranking_worst_AccepRate TINYINT UNSIGNED NOT NULL CHECK(Ranking_worst_AccepRate BETWEEN 0 AND 10),
    Ranking_worst_Sinepeia TINYINT UNSIGNED NOT NULL CHECK(Ranking_worst_Sinepeia BETWEEN 0 AND 10),
    FOREIGN KEY (Id_worst_distributor) REFERENCES Distributor(id_distributor),
    FOREIGN KEY (hmera_worst) REFERENCES Shift(date_shift)
);

CREATE TABLE BestDistributors (
    hmera_best DATE,
    Id_best_distributor INT,
    Ranking_best_from_costumer TINYINT UNSIGNED NOT NULL CHECK(Ranking_best_from_costumer BETWEEN 0 AND 10),
    Ranking_best_from_store TINYINT UNSIGNED NOT NULL CHECK(Ranking_best_from_store BETWEEN 0 AND 10),
    Ranking_best_AccepRate TINYINT UNSIGNED NOT NULL CHECK(Ranking_best_AccepRate BETWEEN 0 AND 10),
    Ranking_best_Sinepeia TINYINT UNSIGNED NOT NULL CHECK(Ranking_best_Sinepeia BETWEEN 0 AND 10),
    FOREIGN KEY (Id_best_distributor) REFERENCES Distributor(id_distributor),
    FOREIGN KEY (hmera_best) REFERENCES Shift(date_shift)
);
