'use strict';

const assert = require('chai').assert;

const sanitizer = require('../../src/terms/index');


describe('Term sanitation', () => {

  it('Should return empty with an empty input', () => {
    assert(sanitizer('') === '');
    assert(sanitizer() === '');
    assert(sanitizer(null) === '');
  });

  it('Should return a clean input with an empty input', () => {
    const cleaned = sanitizer('%·$""·$%iron man!"·!!');
    assert(cleaned === 'iron man');
  });

});
