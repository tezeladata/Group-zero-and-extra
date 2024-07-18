'use strict';

const shdb = require('superherodb-parser');

const heroName = 'hulk';

shdb.search(heroName).then((res) => {
  console.log('Search result : ');
  console.log(JSON.stringify(res, null, 2));
});
