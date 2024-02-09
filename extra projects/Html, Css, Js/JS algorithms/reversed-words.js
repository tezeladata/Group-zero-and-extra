// str input here
function reverseWords(str) {
    let words = str.split(" ");
    let reversedWords = [];
    for (let i = 0; i < words.length; i++) {
        let reversed = "";
        for (let j = words[i].length - 1; j >= 0; j--) {
            reversed += words[i][j];
        }
        reversedWords.push(reversed);
    }
    return reversedWords.join(" ");
}