'use strict';

const parser = require('x-ray')();

const searchParser = html => {
  return new Promise((resolve, reject) => {
    parser(html, {
      total: '.searchresulthead:first-child',
      results: parser('.searchresultrow', [{
        heroPath: 'a@href',
        match: 'a',
        type: 'i@class'
      }])
    })((err, obj) =>{
      if (err) return reject(err);

      return resolve(obj);
    });
  });

};

module.exports = searchParser;
