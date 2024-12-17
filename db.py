import sqlite3

# Fonction pour créer la table + la contrainte UNIQUE pour éviter les doublons
def create_table():
    db = sqlite3.connect('database.db')
    query = """
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT NOT NULL,
        name TEXT NOT NULL,
        age INTEGER,
        gender TEXT,
        UNIQUE(first_name, name, age, gender)
    )
    """
    cur = db.cursor()
    cur.execute(query)
    db.commit()
    db.close()

# Fonction pour ajouter un étudiant
def create_student(first_name, name, age, gender):
    try:
        db = sqlite3.connect('database.db')
        query = """
            INSERT INTO students (first_name, name, age, gender)
            VALUES (?, ?, ?, ?)
            """
        cur = db.cursor()
        cur.execute(query, (first_name, name, age, gender))
        db.commit()
        print(f"Étudiant ajouté : {first_name} {name}")
    except sqlite3.IntegrityError:
        print(f"Erreur : l'étudiant {first_name} {name} existe déjà.")
    finally:
        db.close()

# Fonction pour récupérer tous les étudiants
def select_students():
    db = sqlite3.connect('database.db')
    query = "SELECT id, first_name, name, age, gender FROM students"
    cur = db.cursor()
    cur.execute(query)
    students_lst = cur.fetchall()  # Récupère tous les résultats
    db.close()
    return students_lst

# Fonction pour mettre à jour un étudiant par ID
def update_student(student_id, new_first_name, new_name, new_age, new_gender):
    db = sqlite3.connect('database.db')
    query = "UPDATE students SET first_name = ?, name = ?, age = ?, gender = ? WHERE id = ?"
    cur = db.cursor()
    cur.execute(query, (new_first_name, new_name, new_age, new_gender, student_id))
    db.commit()
    db.close()

# Fonction pour supprimer un étudiant par ID
def delete_student(student_id):
    db = sqlite3.connect('database.db')
    query = "DELETE FROM students WHERE id = ?"
    cur = db.cursor()
    cur.execute(query, (student_id,))
    db.commit()
    db.close()

# Fonction pour afficher les étudiants de manière formatée
def print_students(students):
    print("ID | Prénom | Nom | Âge | Genre")
    print("-" * 30)
    for student in students:
        print(f"{student[0]:<3} | {student[1]:<6} | {student[2]:<8} | {student[3]:<3} | {student[4]}")
    print()

# Bloc principal pour exécuter le script
if __name__ == "__main__":
    # Création de la table
    create_table()

    # Ajout d'étudiants
    create_student("Maeva", "Duboux", 10, "female")
    create_student("Noémie", "Pierrot", 11, "female")
    create_student("Nathan", "Palot", 11, "male")

    # Affichage des étudiants après ajout
    print("Étudiants après ajout :")
    students = select_students()
    print_students(students)

    # Mise à jour d'un étudiant
    update_student(2, "Enzo", "Charrette", 12, "male")

    # Affichage des étudiants après mise à jour
    print("Étudiants après mise à jour :")
    students = select_students()
    print_students(students)

    # Suppression d'un étudiant
    delete_student(3)

    # Affichage des étudiants après suppression
    print("Étudiants après suppression :")
    students = select_students()
    print_students(students)