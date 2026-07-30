import numpy as np
import matplotlib.pyplot as plt
import sqlite3
import random

def create_and_populate_db():
    #Connects to 'population_NL.db'
    try:
        with sqlite3.connect("population_NL.db") as conn:
            cursor = conn.cursor()

            #Cleans the slate so old data does not stack up
            cursor.execute("DROP TABLE IF EXISTS population")

            #Creates the table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS population (
                    city TEXT,
                    year INTEGER,
                    population INTEGER
                )
            """)

            #List of cities and 2023 population:
            cities_data = [
                ('Archer', 2023, 1140),
                ('Boca Raton', 2023, 97422),
                ('Campbellton', 2023, 191),
                ('Eustis', 2023, 23189),
                ('Frostproof', 2023, 3273),
                ('Jacksonville', 2023, 949611),
                ('Orlando', 2023, 307573),
                ('Pensacola', 2023, 54312),
                ('St. Augustine', 2023, 14329),
                ('Wewahitchka', 2023, 2074)
        ]

            #Populates population table with city and 2023 population
            for city, year, pop in cities_data:
                cursor.execute("INSERT INTO population (city, year, population) VALUES (?, ?, ?)", (city, year, pop))
            print("Initial 2023 data inserted successfully!")

    except sqlite3.OperationalError as e:
        print("Failed to open database:", e)

def simulate_population_growth():
    cities_starting_pop = {
        'Archer': 1140,
        'Boca Raton': 97422,
        'Campbellton': 191,
        'Eustis': 23189,
        'Frostproof': 3273,
        'Jacksonville': 949611,
        'Orlando': 307573,
        'Pensacola': 54312,
        'St. Augustine': 14329,
        'Wewahitchka': 2074
        }

    try:
        #Open the database connection using with sqlite3
        with sqlite3.connect("population_NL.db") as conn:
            cursor = conn.cursor()

            for city, starting_pop in cities_starting_pop.items():
                #Sets tracker to 2023 baseline population
                current_population = starting_pop

                #Runs through the years 2024 to 2044
                for year in range(2024, 2044):
                    #Generate a random rate of decline or growth
                    rate = random.uniform(-0.02, 0.05)

                    #Calculates and updates the tracker
                    current_population = int(current_population * (1 + rate))

                    #Execute the SQL INSERT query for the specific city, year, and new population
                    cursor.execute("INSERT INTO population (city, year, population) VALUES (?, ?, ?)",
                                    (city, year, current_population))
            #Prints success or error message
            print("20-year simulation data generated and saved successfully!")
    except sqlite3.OperationalError as e:
        print("Database error during simulation:", e)

def display_population_growth():
    #Defines the cities in Florida
    cities = ['Archer', 'Boca Raton', 'Campbellton', 'Eustis', 'Frostproof', 
              'Jacksonville', 'Orlando', 'Pensacola', 'St. Augustine', 'Wewahitchka']

    print("Available cities:")
    for i, city in enumerate(cities, 1):
        print(f"{i}. {city}")
    choice = input("Enter the name of the city you want to view: ")
    #Validation check to ensure city name is typed correctly
    if choice not in cities:
        print("City not found. Please check your spelling and capitalization.")
        return

    #Initializes database
    try:
        with sqlite3.connect("population_NL.db") as conn:
            cursor = conn.cursor()

            #Retrieves data for the chosen city ordered by year
            cursor.execute("SELECT year, population FROM population WHERE city = ? ORDER BY year", (choice,))
            rows = cursor.fetchall()

            #Separates data into two distinct lists using list comprehension
            years = [row[0] for row in rows]
            populations = [row[1] for row in rows]

            #Defines chart title, axes and plot line
            plt.plot(years, populations, marker='d', color='r')
            plt.title(f"Population Growth for {choice}")
            plt.xlabel('Year')
            plt.xticks(range(min(years), max(years) + 1, 2))
            plt.ylabel('Population')
            plt.grid(True)
            plt.show()
    except sqlite3.OperationalError as e:
        print("Database error during plotting:", e)

#Execution block
if __name__ == "__main__":
    create_and_populate_db()
    simulate_population_growth()
    display_population_growth()