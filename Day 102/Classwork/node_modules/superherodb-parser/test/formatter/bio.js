'use strict';

const assert = require('chai').assert;

const formatter = require('../../src/formatter/bio');
const unparsed = require('./example-bio.json');
const expected = require('./example-bio-formatted.json');

describe('Bio formatter', () => {

  it('Format parsed object', () => {
    const actual = formatter(unparsed);
    assert.isObject(actual);
    assert.deepEqual(expected, actual);
  });

});
