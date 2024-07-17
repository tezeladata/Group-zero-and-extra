'use strict';

const request = require('request-promise');

const getSearchUrl = require('./urls').search;
const debug = require('./debug')('search');
const parse = require('./parser/search');
const format = require('./formatter/search');

module.exports = (term) => {
  debug(`Searching ${term}`);

  return request(getSearchUrl(term))
    .then(parse)
    .then(format);
};
