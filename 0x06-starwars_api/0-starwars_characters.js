#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];

if (!movieId) {
  console.log('Usage: ./0-starwars-characters.js <movie_id>');
  process.exit(1);
}

// Function to fetch character names
function fetchCharacterNames (characterUrls) {
  const promises = characterUrls.map(url => {
    return new Promise((resolve, reject) => {
      request(url, (err, response, body) => {
        if (err) {
          reject(err);
        } else if (response.statusCode === 200) {
          const characterData = JSON.parse(body);
          resolve(characterData.name);
        } else {
          reject(new Error(`Failed to retrieve character data: ${response.statusCode}`));
        }
      });
    });
  });

  return Promise.all(promises);
}

// Fetch movie data and then character names
request(`https://swapi.dev/api/films/${movieId}/`, (error, response, body) => {
  if (error) {
    console.error('Failed to retrieve movie data:', error);
    process.exit(1);
  }

  if (response.statusCode === 200) {
    const movieData = JSON.parse(body);
    const characterUrls = movieData.characters;

    fetchCharacterNames(characterUrls)
      .then(names => {
        names.forEach(name => {
          console.log(name);
        });
      })
      .catch(err => {
        console.error('Error fetching character names:', err);
      });
  } else {
    console.log(`Failed to retrieve movie data: ${response.statusCode}`);
  }
});
