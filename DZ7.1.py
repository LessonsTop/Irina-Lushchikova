
import psycopg2
def main():
    connection = psycopg2.connect('host=localhost port=5432 dbname=test1 user=postgres password=postgres')
    cursor = connection.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS city (id serial PRIMARY KEY, city varchar, street varchar, number_home int4);')
    cursor.execute('CREATE TABLE IF NOT EXISTS country (id serial PRIMARY KEY, country varchar, city varchar);')
    connection.commit()
    cursor.execute("INSERT INTO city (city, street, number_home) VALUES ('Moscow','Lenina', '18'), ('Moscow','Ul`yanova', '145'), ('Izhevsk','Kirova', '144'), ('Izhevsk', 'Svobodi', '5')")
    cursor.execute("INSERT INTO country (country, city) VALUES ('Russia','Moscow'), ('Russia', 'Moscow'), ('Russia','Izhevsk'), ('Russia','Izhevsk')")
    connection.commit()
    cursor.execute('SELECT * FROM city;')
    print(cursor.fetchmany(3))
    cursor.execute('SELECT * FROM country;')
    print(cursor.fetchmany(3))
if __name__ == '__main__':
    main()

