'use strict';

const _ = require('lodash');

const cleanValue = (val) => {
  if ( _.isString(val) ) return val.trim();
  return val;
};

const cleanProps = (obj) => {
  if (_.isArray(obj)) {
    return _.map(obj, cleanValue);
  }

  return _.keys(obj).reduce((final, prop) => {
    final[prop] = _.isObject(obj[prop]) ? cleanProps(obj[prop]) : cleanValue(obj[prop]);
    return final;
  }, {});
};

module.exports = cleanProps;
