#!/usr/bin/node

const request = require('request');

if (process.argv.length !== 3) {
  console.log('Usage: ./0-starwars-characters.js <movie_id>');
  process.exit(1);
}

const movieId = process.argv[2];
const baseUrl = 'https://swapi.dev/api/films/';
const url = `${baseUrl}${movieId}/`;

request(url, (error, response, body) => {
  if (error) {
    console.error('Failed to retrieve data:', error);
    process.exit(1);
  }

  if (response.statusCode === 200) {
    const movieData = JSON.parse(body);
    const characters = movieData.characters;
    characters.forEach((characterUrl) => {
      request(characterUrl, (charError, charResponse, charBody) => {
        if (charError) {
          console.error('Failed to retrieve character data:', charError);
          return;
        }
        if (charResponse.statusCode === 200) {
          const charData = JSON.parse(charBody);
          console.log(charData.name);
        }
      });
    });
  } else {
    console.log(`Failed to retrieve data: ${response.statusCode}`);
  }
});
