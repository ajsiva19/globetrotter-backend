def default_data(db,schema):
    data = [
        {
            "city": "London",
            "country": "United Kingdom",
            "clues": [
                "This city has a famous clock tower that people mistakenly call 'Big Ben'.",
                "Known for its red double-decker buses and black cabs."
            ],
            "fun_facts": [
                "Big Ben is actually the name of the bell inside the tower, not the tower itself!",
                "London has more than 170 museums, including the British Museum, which is free to visit."
            ],
            "trivia": [
                "This city is home to the world's oldest underground railway, opened in 1863.",
                "The Tower of London used to house the Royal Menagerie, a collection of exotic animals."
            ]
        },
        {
            "city": "Rome",
            "country": "Italy",
            "clues": [
                "This city is famous for an ancient amphitheater where gladiators once fought.",
                "The headquarters of the Catholic Church, Vatican City, is located here."
            ],
            "fun_facts": [
                "The Colosseum had a retractable awning system to shade spectators from the sun.",
                "Rome has a museum dedicated to pasta!"
            ],
            "trivia": [
                "This city has more fountains than any other in the world, with over 1,500!",
                "The Trevi Fountain collects around €3,000 in coins daily, which is donated to charity."
            ]
        },
        {
            "city": "Sydney",
            "country": "Australia",
            "clues": [
                "This city is home to a famous opera house with sail-like roofs.",
                "Known for its massive New Year's Eve fireworks at the Harbour Bridge."
            ],
            "fun_facts": [
                "Sydney’s Harbour Bridge is the world’s largest steel arch bridge.",
                "The Sydney Opera House took 14 years to build and was completed in 1973."
            ],
            "trivia": [
                "There are over 100 beaches within this city’s metropolitan area!",
                "The first European settlers arrived in 1788 at what is now Sydney Cove."
            ]
        },
        {
            "city": "Rio de Janeiro",
            "country": "Brazil",
            "clues": [
                "Famous for its massive carnival celebrations with samba dancers.",
                "A giant statue of Jesus Christ overlooks the city from a mountain."
            ],
            "fun_facts": [
                "Christ the Redeemer was struck by lightning in 2014 but suffered only minor damage.",
                "Rio’s Copacabana Beach was named after a religious figure from Bolivia."
            ],
            "trivia": [
                "This city was the capital of Brazil until 1960, when Brasília was built.",
                "Sugarloaf Mountain offers one of the best views of the city."
            ]
        },
        {
            "city": "Dubai",
            "country": "United Arab Emirates",
            "clues": [
                "This city has the tallest building in the world.",
                "Famous for its artificial islands shaped like a palm tree."
            ],
            "fun_facts": [
                "Dubai has a police force that drives luxury sports cars like Lamborghinis.",
                "The Burj Khalifa is so tall that people on the top floors see the sunset later than those on the ground."
            ],
            "trivia": [
                "This city has the world's largest shopping mall by total area.",
                "The Palm Jumeirah is visible from space!"
            ]
        },
        {
            "city": "Moscow",
            "country": "Russia",
            "clues": [
                "This city is home to a colorful cathedral with onion-shaped domes.",
                "Its underground metro system is one of the most beautiful in the world."
            ],
            "fun_facts": [
                "The Kremlin has a secret underground bunker used during the Cold War.",
                "Moscow’s Metro stations are so ornate they look like palaces."
            ],
            "trivia": [
                "This city has the largest number of billionaires in Europe.",
                "Red Square was once used as a marketplace before becoming a symbol of the country."
            ]
        },
        {
            "city": "Istanbul",
            "country": "Turkey",
            "clues": [
                "This city is the only one in the world that spans two continents.",
                "Famous for a grand market that sells spices, carpets, and jewelry."
            ],
            "fun_facts": [
                "Istanbul was once called Constantinople and was the capital of the Byzantine Empire.",
                "The Bosphorus Strait connects Europe and Asia within the city."
            ],
            "trivia": [
                "The Grand Bazaar has over 4,000 shops and attracts millions of visitors each year.",
                "The city’s Hagia Sophia has been a church, a mosque, and now a museum."
            ]
        },
        {
            "city": "Cape Town",
            "country": "South Africa",
            "clues": [
                "A flat-topped mountain towers over this coastal city.",
                "Once the home of Nelson Mandela’s prison on Robben Island."
            ],
            "fun_facts": [
                "Table Mountain has more plant species than the entire UK!",
                "Penguins live on the beaches near this city."
            ],
            "trivia": [
                "The Cape of Good Hope is nearby and was once thought to be the southernmost point of Africa.",
                "This city was the first in South Africa to host the FIFA World Cup (2010)."
            ]
        },
        {
            "city": "Bangkok",
            "country": "Thailand",
            "clues": [
                "This city is home to a golden reclining Buddha statue.",
                "Famous for its floating markets and street food culture."
            ],
            "fun_facts": [
                "Bangkok’s official name is the longest city name in the world—it has 169 characters!",
                "The city is known for its tuk-tuks, three-wheeled motorized rickshaws."
            ],
            "trivia": [
                "Bangkok has the world's largest Chinatown outside of China.",
                "The city's Grand Palace was built in 1782 and is still used for royal ceremonies."
            ]
        },
        {
            "city": "Toronto",
            "country": "Canada",
            "clues": [
                "This city has one of the tallest free-standing towers in the world.",
                "Known for its multicultural diversity and vibrant arts scene."
            ],
            "fun_facts": [
                "Toronto is home to over 200 ethnic groups and more than 140 languages are spoken here.",
                "The PATH is the world’s largest underground shopping complex."
            ],
            "trivia": [
                "This city’s name comes from a Mohawk word meaning 'place where trees stand in the water'.",
                "Toronto’s CN Tower was the tallest freestanding structure in the world until 2009."
            ]
        }
    ]
    for entry in data:
        destination = schema(**entry)
        db.add(destination)
    db.commit()
    db.close()
    print("suceessfully created data")

