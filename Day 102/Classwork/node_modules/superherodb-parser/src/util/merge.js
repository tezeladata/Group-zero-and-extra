'use strict';

const _ = require('lodash');

module.exports = (obj) => {
  return _(obj).reduce((final, actual) => _.merge(final, actual), {});
};
