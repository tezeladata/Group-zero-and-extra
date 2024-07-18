# SuperheroDB Parser

[![Build Status](https://travis-ci.org/guumaster/superherodb-parser.svg)](https://travis-ci.org/guumaster/superherodb-parser)
[![Coverage Status](https://coveralls.io/repos/guumaster/superherodb-parser/badge.svg?branch=master&service=github)](https://coveralls.io/github/guumaster/superherodb-parser?branch=master)

This project is only an example of how to create a parser/API based on web scrapping. Its only purpose is to show/learn 
a more functional/promise-friendly way of scrapping the web. 

It retrieves basic information, if you need a complete profile of every superhero known, go to the original 
site [SuperHeroDB](http://www.superherodb.com/).



## Usage 

* Install the package
```sh
npm install superherodb-parser
```

### Search for a superhero by name: 

```js
// search.js
'use strict';

const shdb = require('superherodb-parser');

const heroName = 'hulk';

shdb.search(heroName).then((res) => {
  console.log('Search result : ');
  console.log(JSON.stringify(res, null, 2));
});
```

### Fetch a superhero by ID: 

```js
// fetch.js
'use strict';

const shdb = require('superherodb-parser');

const heroId = '/iron-man/10-85/';

shdb.fetch(heroId).then((res) => {
  console.log('Your hero stats: ');
  console.log(JSON.stringify(res, null, 2) );
});
```


## TODO

* [ ] Improve the ID fetch parameters
* [ ] Add a group search
* [ ] Add more examples
* [ ] Create a CLI package


## Disclaimer

This project is not affiliated with SuperHeroDB.com site. All the credits for a great site is theirs.
