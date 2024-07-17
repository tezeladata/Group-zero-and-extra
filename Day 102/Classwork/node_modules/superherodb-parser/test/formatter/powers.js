'use strict';

const assert = require('chai').assert;
const formatter = require('../../src/formatter/powers');

describe('Powers formatter', () => {

  it('Format parsed object', () => {
    const unformatted = {
      weaknesses: ['a', 'b', 'c'],
      powers: [
        {
          powers: ['a', 'b', 'c'],
          abilities: ['a', 'b', 'c']
        },
        {
          powers: ['d', 'e', 'f'],
          abilities: ['d', 'e', 'f']
        }
      ]
    };

    const expected = {
      weaknesses: ['a', 'b', 'c'],
      powers: ['a', 'b', 'c', 'd', 'e', 'f'],
      abilities: ['a', 'b', 'c', 'd', 'e', 'f']
    };

    assert.deepEqual(formatter(unformatted), expected);
  });

});
