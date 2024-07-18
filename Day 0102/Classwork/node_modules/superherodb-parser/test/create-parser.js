'use strict';

const assert = require('chai').assert;

const parser = require('../src');

describe('Create parser', () => {

  it('Creates a new parser without options', () => {
    assert.isObject(parser, 'Parser should be an object');
  });

  //it('Accepts creation options', () => {
  //  const parser = shParser({});
  //  assert.isObject(parser, 'Parser should be an object');
  //
  //});

});
