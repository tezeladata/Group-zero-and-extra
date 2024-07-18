'use strict';

const _ = require('lodash');

module.exports = (obj) => {
  return {
    powers: _.reduce(obj.powers, (final, actual) => final.powers.concat(actual.powers)),
    abilities: _.reduce(obj.powers, (final, actual) => final.abilities.concat(actual.abilities)),
    weaknesses: obj.weaknesses
  };
};
