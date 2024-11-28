console.log(process)

console.log(process.env)

console.log(process.memoryUsage())

console.log(process.argv[3])

const os = require('os');
console.log(os.type())
console.log(os.arch())
console.log(os.homedir())
console.log(os.hostname())
console.log(os.uptime())
console.log(os.networkInterfaces().Ethernet)
console.log(os.networkInterfaces())