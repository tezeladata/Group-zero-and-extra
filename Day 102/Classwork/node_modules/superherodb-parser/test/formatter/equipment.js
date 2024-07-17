'use strict';

const assert = require('chai').assert;
const formatter = require('../../src/formatter/equipment');

describe('Equipment formatter', () => {

  it('Doesnt do nothing yet', () => {
    assert.deepEqual(formatter({ nothing: 1000}), { nothing: 1000});
  });
});
