'use strict';

const BASE_URL = 'http://www.superherodb.com';
const SEARCH_URL = `${BASE_URL}/search_query.php?q=`;
const BIO_URL = `${BASE_URL}{{HERO_PATH}}`;
const POWERS_URL = `${BASE_URL}{{HERO_PATH}}powers/`;
const EQUIPMENT_URL = `${BASE_URL}{{HERO_PATH}}equipment/`;

module.exports = {
  URLS: {
    bio: BIO_URL,
    powers: POWERS_URL,
    equipment: EQUIPMENT_URL,
    search: SEARCH_URL
  }
};
