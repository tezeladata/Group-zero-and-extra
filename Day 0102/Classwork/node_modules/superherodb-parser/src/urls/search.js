'use strict';

const config = require('../config');
const sanitize = require('../terms');

module.exports = (term) => {
  const searchTerm = sanitize(term);

  if (!searchTerm) {
    throw new Error('Missing search term');
  }
  return config.URLS.search + encodeURIComponent(searchTerm);
};
