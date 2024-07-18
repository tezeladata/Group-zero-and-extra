'use strict';

const search = require('./search');
const hero = require('./hero');

const heroUrls = (heroPath) => {
  return {
    bio: hero('bio', heroPath),
    powers: hero('powers', heroPath),
    equipment: hero('equipment', heroPath)
  };
};

module.exports = {
  search,
  heroUrls
};
