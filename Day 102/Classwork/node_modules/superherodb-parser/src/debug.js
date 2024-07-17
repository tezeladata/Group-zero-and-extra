'use strict';

const debug = require('debug');

module.exports = (module) => debug(`shdb:${module}`);
