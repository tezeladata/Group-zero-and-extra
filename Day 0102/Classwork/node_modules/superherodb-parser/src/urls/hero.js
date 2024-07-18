'use strict';

const config = require('../config');

module.exports = (type, heroPath) => {
  if (!type) {
    throw new Error('Missing type');
  }

  if (!heroPath) {
    throw new Error('Missing heroPath');
  }

  return config.URLS[type].replace('{{HERO_PATH}}', heroPath);
};
