// url module

const url = require("url");

const urlToParse = 'https://fakestoreapi.com/products/1'
const url1 = new URL(urlToParse);

const url2 = new URL(urlToParse);
url2.protocol = "http:";
url2.host = "facebook.com";
url2.hostname = "facebook.com";
url2.pathname = "accounts/david";
url2.origin = "http://www.facebook.com";
url2.href = "http://www.facebook.com/accounts/david";

console.log(url1);
console.log(url2.toString());