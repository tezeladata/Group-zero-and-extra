'use strict';
const assert = require('chai').assert;

const hero = require('../../src/urls/hero');

describe('Hero URLs', () => {
  it('Exports a function', () => {
    assert.isFunction(hero);
  });

  it('Throws without a type', () => {
    assert.throws(() => {
      hero();
    }, 'Missing type');
  });

  it('Throws without a hero path', () => {
    assert.throws(() => {
      hero('bio');
    }, 'Missing heroPath');
  });

  it('Returns a bio URL for a given heroPath', () => {
    const url = hero('bio', '/iron-man/10-85/');
    const expected = 'http://www.superherodb.com/iron-man/10-85/';
    assert(url === expected);
  });

  it('Returns a powers URL for a given heroPath', () => {
    const url = hero('powers', '/iron-man/10-85/');
    const expected = 'http://www.superherodb.com/iron-man/10-85/powers/';
    assert(url === expected);
  });

  it('Returns a equipment URL for a given heroPath', () => {
    const url = hero('equipment', '/iron-man/10-85/');
    const expected = 'http://www.superherodb.com/iron-man/10-85/equipment/';
    assert(url === expected);
  });

});
