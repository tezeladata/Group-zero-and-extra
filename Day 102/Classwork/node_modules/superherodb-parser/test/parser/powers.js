'use strict';

const assert = require('chai').assert;

const parser = require('../../src/parser/powers');

describe('Bio parser', () => {

  it('Returns a promise', () => {
    assert.instanceOf(parser(), Promise);
  });

  it('Parse an empty HTML', (done) => {
    const rawHTML = `<div></div>`;

    parser(rawHTML).then(res => {
      assert.deepEqual(res, {
        powers: [],
        weaknesses: []
      });
      done();

    }).catch(done);

  });

  it('Parse an HTML', (done) => {
    const rawHTML = `<div>
    <div class="cblock">
      <h3>SUPERHERO Powers</h3>
      <div class="content copy">
          <p>CONTENT </p>
          <h4>Supertesting</h4>
      </div>

    </div>
    <div class="cblock">

      <h3>SUPERHERO Weaknesses</h3>
      <div class="content copy">
        <h4>Super slowness</h4>

      </div>
    </div>`;

    parser(rawHTML).then(res => {
      assert.deepEqual(res, {
        powers: [{
          abilities: [],
          powers: [
            'Supertesting'
          ]
        }],
        weaknesses: ['Super slowness']
      });
      done();

    }).catch(done);

  });
});
