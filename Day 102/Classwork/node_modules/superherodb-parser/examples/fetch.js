'use strict';

const shdb = require('superherodb-parser');

const heroId = '/iron-man/10-85/';

shdb.fetch(heroId).then((res) => {
  console.log('Your hero stats: ', JSON.stringify(res, null, 2) );
});
