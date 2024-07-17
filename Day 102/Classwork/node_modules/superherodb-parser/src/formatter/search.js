'use strict';

const aliasRe = / \(alias\)/;
const groupRe = / fa-users/;
module.exports = (searchResult) => {
  const formatted = searchResult.results.map(result => {
    const name = result.match.split(' --- ');
    const isGroup = groupRe.test(result.type);
    const isAlias = aliasRe.test(name[0]);

    if (isGroup) {
      return {
        groupPath: result.heroPath,
        groupName: name[0].replace(' (alias)', ''),
        isAlias: isAlias,
        isGroup: true
      };
    }

    return {
      heroPath: result.heroPath,
      heroName: name[0].replace(' (alias)', ''),
      realName: name[1],
      isAlias: isAlias,
      isGroup: false
    };
  });

  return {
    total: Number(searchResult.total.match(/([0-9]+)/)[1]),
    results: formatted
  };
};
