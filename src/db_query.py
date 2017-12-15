if __name__ == '__main__':
    import sqlite3

    conn = sqlite3.connect(":memory:")
    # conn = sqlite3.connect('data/db/lab4.db')
    script = open('data/db/protdb.sqlite3', 'rU')
    conn.executescript(script.read())
    script.close()
    c = conn.cursor()

    print("what species are in the database?")
    species_query = "SELECT name FROM species;"
    c.execute(species_query)
    res = c.fetchall()
    for species in res:
        print(f"\t{species[0]}")

    sus_insert = "INSERT INTO species(abbrev, name, common) VALUES ('ss', 'Sus scrofa!', 'unknown')"
    try:
        c.execute(sus_insert)
        conn.commit()
    except sqlite3.IntegrityError:
        print("Insert failed, unique constraint not met")

    print("What proteins are longer than 1000 aa?")
    long_prots_query = "SELECT accession FROM protein WHERE length(sequence) > 1000;"

    c.execute(long_prots_query)
    res = c.fetchall()
    for tup in res:
        print(f"\t{tup[0]}")

    print("What species are present in family NHR3? Give a full list with full species names using one SQL statement")
    nhr3_species_query = """
    SELECT DISTINCT species.name, species.common 
           FROM familymembers 
		   JOIN protein 
		     ON familymembers.protein = protein.accession
		   JOIN species 
		     ON species.abbrev = protein.species
             WHERE familymembers.family = 'NHR3'; 
    """
    c.execute(nhr3_species_query)
    res = c.fetchall()
    for tup in res:
        print(f"\t{tup[0]}")

    print("How many proteins from each species are present in the database?")
    specs_query = """
    SELECT species.common, COUNT(protein.sequence) as num_sequences 
    FROM protein 
    JOIN species 
    ON protein.species = species.abbrev 
    GROUP BY protein.species;
    """
    res = c.execute(specs_query).fetchall()
    for tup in res:
        print(f"\tSpecies: {tup[0]}\n\tCount: {tup[1]}")

    print("-- How do you change the schema to add information about a protein's structure?")
    update_schema_query = """
    CREATE TABLE IF NOT EXISTS structure (
	protein VARCHAR(20),
	name VARCHAR(50),
	resolution NUMERIC,
	method VARCHAR(50),
	PRIMARY KEY(protein, name)
    );
    """
    c.execute(update_schema_query)
    conn.commit()

    struct_inserts = """
    INSERT INTO structure(protein, name, resolution, method) VALUES('NH10_CAEEL', 'xfd88', 10.8, 'X-Ray Diffraction');
    INSERT INTO structure(protein, name, resolution, method) VALUES('NH10_CAEEL', 'xfd89', 1.52, 'Solution NMR');
    INSERT INTO structure(protein, name, resolution, method) VALUES('NR21_CHICK', 'ff98', 1.99, 'X-Ray Diffraction');
    """
    c.executescript(struct_inserts)
    conn.commit()

    res = c.execute("SELECT * FROM structure;").fetchall()
    print("ACCESSION       TYPE       RESOLUTION      METHOD")
    for tup in res:
        print("{:<14}{:<11}{:<11}{}".format(tup[0], tup[1], tup[2], tup[3]))

    print("What happens when you insert Sus twice?")
    c.execute(sus_insert)
    c.close()