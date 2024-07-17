'use strict';

const _ = require('lodash');
const camelCase = require('camelcase');

module.exports = (obj) => {
  return _.keys(obj)
    .reduce((clean, key) => {
      clean[camelCase(key.toLowerCase())] = obj[key];
      return clean;
    }, {});
};
