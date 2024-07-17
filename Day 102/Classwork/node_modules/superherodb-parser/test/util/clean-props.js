'use strict';

const assert = require('chai').assert;
const cleaner = require('../../src/util/clean-props');

describe('Utils clean props', () => {

  it('clean all vals', () => {
    const unformatted = {
      propOne: '\n super       ',
      propTwo: {
        subProp1: '     hero',
        subProp2: [' a ', 'b', 33]
      },
      prop3: 1000
    };
    const expected = {
      propOne: 'super',
      propTwo: {
        subProp1: 'hero',
        subProp2: ['a', 'b', 33]
      },
      prop3: 1000
    };

    assert.deepEqual(cleaner(unformatted), expected);
  });

});
