'use strict';

const parser = require('x-ray')();

const searchParser = html => {
  return new Promise((resolve, reject) => {

    parser(html, {
      powers: parser('.cblock:contains(" Powers")', [{
        powers: parser('h3:contains(" Powers") + div.content', ['h4']),
        abilities: parser('h3:contains("Abilities") + div.content', ['h4'])
      }]),
      weaknesses: parser('h3:contains(" Weaknesses") + div.content', ['h4'])
    })(function(err, obj) {
      if (err) return reject(err);

      return resolve(obj);
    });
  });

};

module.exports = searchParser;
