'use strict';

const assert = require('chai').assert;
const formatter = require('../../src/util/stats');

describe('Utils merge stats', () => {

  it('merge all stats', () => {
    const unformatted = [
      {
        skill: ['a', 'b', 'c'],
        val: ['1', '2', '3']
      }
    ];
    const expected = {
      a: 1, b: 2, c: 3
    };

    assert.deepEqual(formatter(unformatted), expected);
  });

});
