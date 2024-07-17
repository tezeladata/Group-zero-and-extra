'use strict';

const assert = require('chai').assert;
const camelizer = require('../../src/util/camelize-props');

describe('Utils camelize props', () => {

  it('camelize all props', () => {
    const unformatted = {
      'prop-one': 1,
      ProP2: 2,
      prop_three: 3
    };
    const expected = {
      propOne: 1,
      prop2: 2,
      propThree: 3
    };

    assert.deepEqual(camelizer(unformatted), expected);
  });

});
