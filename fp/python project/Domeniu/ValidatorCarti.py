class ValidatorCarti:
    def validate(self, carte):
        errors = ""
        if carte.id_carte == "":
            errors += "ID can not be empty;"
        if carte.titlu == "":
            errors += "Titlu can not be empty;"
        if carte.descriere == "":
            errors += "Descriere can not be empty;"
        if carte.autor == "":
            errors += "Autor can not be empty"
        if errors:
            raise ValueError(errors)