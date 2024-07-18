'use strict';

const _ = require('lodash');

const camelize = require('./../util/camelize-props');
const formatStats = require('./../util/stats');
const merge = require('./../util/merge');

module.exports = (obj) => {
  const bio = _.map(obj.bio, (data) => _.zipObject(data.label, data.val));

  return {
    name: obj.name,
    realName: obj.real,
    level: Number(obj.level),
    bio: camelize(merge(bio)),
    stats: camelize(formatStats(obj.stats))
  };
};
