'use strict';

const parser = require('x-ray')();

const searchParser = html => {
  return new Promise((resolve, reject) => {

    parser(html, {
      equipment: parser('h3:contains("Equipment") + div.content', ['h4']),
      armor: parser('h3:contains("Armor") + div.content', ['h4']),
      weapons: parser('h3:contains("Weapons") + div.content', ['h4'])
    })(function(err, obj) {
      if (err) return reject(err);

      return resolve(obj);
    });
  });

};

module.exports = searchParser;
