'use strict';
const assert = require('chai').assert;

const search = require('../../src/urls/search');

describe('Search URLs', () => {
  it('Exports a function', () => {
    assert.isFunction(search);
  });

  it('Throws without a search term', () => {
    assert.throws(() => {
      search();
    }, 'Missing search term');
  });

  it('Return an URL for a given search term', () => {
    const url = search('hulk');
    const expected = 'http://www.superherodb.com/search_query.php?q=hulk';
    assert(url === expected);
  });

  it('Return an encoded URL for a given search term', () => {
    const url = search('iron man');
    const expected = 'http://www.superherodb.com/search_query.php?q=iron%20man';
    assert(url === expected);
  });

  it('Return a clean URL for a given search term', () => {
    const url = search('$%&$iron$%&$ man$%&$');
    const expected = 'http://www.superherodb.com/search_query.php?q=iron%20man';
    assert(url === expected);
  });

});
