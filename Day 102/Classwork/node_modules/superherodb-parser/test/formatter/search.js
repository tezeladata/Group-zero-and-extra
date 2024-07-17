'use strict';

const assert = require('chai').assert;

const formatter = require('../../src/formatter/search');
const unformatted = require('./example-search.json');
const expected = require('./example-search-formatted.json');

describe('Search formatter', () => {

  it('Format a search result', () => {
    assert.deepEqual(formatter(unformatted), expected);
  });

});
