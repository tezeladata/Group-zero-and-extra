'use strict';

const assert = require('chai').assert;
const merger = require('../../src/util/merge');

describe('Utils clean props', () => {

  it('merge all keys', () => {
    const unformatted = [
      {
        prop1: 1,
        prop2: 'a',
        prop3: 'b'
      },
      {
        prop4: 1,
        prop5: 'a',
        prop6: { subProp: 1 }
      },
    ];
    const expected = {
      prop1: 1,
      prop2: 'a',
      prop3: 'b',
      prop4: 1,
      prop5: 'a',
      prop6: { subProp: 1 }
    };

    assert.deepEqual(merger(unformatted), expected);
  });

});
