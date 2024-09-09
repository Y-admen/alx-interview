#!/usr/bin/node

const request = require('request');

const filmId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${filmId}`;

request(url, (error, response, body) => {
    if (error) {
        console.error(error);
    } else {
        const filmData = JSON.parse(body);
        const characters = filmData.characters;

        const fetchCharacter = (index) => {
            if (index < characters.length) {
                request(characters[index], (error, response, body) => {
                    if (error) {
                        console.error(error);
                    } else {
                        const characterData = JSON.parse(body);
                        console.log(characterData.name);
                        fetchCharacter(index + 1);
                    }
                });
            }
        };

        fetchCharacter(0);
    }
});