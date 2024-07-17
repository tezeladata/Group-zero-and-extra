'use strict';

const _ = require('lodash');

module.exports = (stats) => {
  return _.zipObject(stats[0].skill, _.map(stats[0].val, (str) => Number(str)) );
};
