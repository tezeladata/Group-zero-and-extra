'use strict';

const assert = require('chai').assert;
const formatter = require('../../src/formatter');

describe('Formatter module', () => {

  it('Exports all features', () => {
    assert.sameMembers(Object.keys(formatter), ['bio', 'equipment', 'powers', 'search']);
  });

});


