'use strict';

module.exports = (input) => {
  return (input || '')
    .trim()
    .replace(/[^a-z0-9,\-'. ]/ig, '');
};
