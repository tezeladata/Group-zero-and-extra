//useful string methods
let UserName="David Tezelashvili"
console.log(UserName.length)

// indexing:
console.log(UserName.charAt(7))
console.log(UserName.indexOf("a"))
console.log(UserName.lastIndexOf("a"))

//removing spaces like py's strip();
let a="     abcdefg       ";
console.log(a.trim());

//uppercase, lowercase:
console.log(a.toUpperCase());
console.log(UserName.toLowerCase());

//changing chars:
let PhoneNumber="123-456-7890";
console.log(PhoneNumber.replaceAll("-", "/"))
console.log(PhoneNumber.replaceAll("-", "   "))