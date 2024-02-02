db = db.getSiblingDB('db_facts');

db.facts.insertMany([
  {
    fact: 'Stevie Wonder scored his first Billboard Hot 100 hit at just 13 years old with "Fingertips."',
    tags: ['music']
  },
  {
    fact: 'Pele scored a total of 1,283 first-class goals, including 77 for Brazil.',
    tags: ['sports', 'soccer']
  },
  {
    fact: 'The world\'s oldest cat lived to 38 years and three days old. Creme Puff',
    tags: ['animals']
  },
]);