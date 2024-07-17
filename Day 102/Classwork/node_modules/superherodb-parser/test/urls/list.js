'use strict';
const assert = require('chai').assert;

const heroUrls = require('../../src/urls').heroUrls;

describe('Hero URLs collection', () => {

  it('Returns all URL for a given heroPath', () => {
    const res = heroUrls('/iron-man/10-85/');
    assert.isObject(res, 'It should return a url collection');
    assert.isString(res.bio, 'It has a bio URL');
    assert.isString(res.powers, 'It has a powers URL');
    assert.isString(res.equipment, 'It has an equipment URL');
  });

});
