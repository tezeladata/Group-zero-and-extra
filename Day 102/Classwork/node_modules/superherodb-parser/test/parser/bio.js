'use strict';

const assert = require('chai').assert;

const parser = require('../../src/parser/bio');

describe('Bio parser', () => {

  it('Returns a promise', () => {
    assert.instanceOf(parser(), Promise);
  });

  it('Parse Hero HTML', (done) => {
    const rawHTML = `<div class="titlehome">
    <h1>HERO NAME</h1>
    <h2>REAL NAME</h2>
    </div>
    <div class="cblock">
      <h3>Powerstats</h3>
      <div class="gridbarlabel">Intelligence</div>
      <div class="gridbarvalue color_red">100</div>
    </div>
    <div class="cblock linkunderline">
      <h3>Biography</h3>
      <div class="content">
        <table class="table">
          <tr>
            <td class="table-label td-wide">Full name</td>
            <td class="td-wide">HERO FULL NAME</td>
          </tr>
        </table>
      </div>
    </div>`;

    parser(rawHTML).then(res => {
      assert.deepEqual(res, {
        name: 'HERO NAME',
        real: 'REAL NAME',
        stats: [{ skill: ['Intelligence'], val: ['100']}],
        bio: [{ label: ['Full name'], val: ['HERO FULL NAME']}]
      });
      done();

    }).catch(done);

  });
});
