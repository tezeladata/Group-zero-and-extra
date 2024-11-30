// current working directory
console.log(process.cwd())

const os = require("os");
//os object
console.log(os)

// arch
console.log(os.arch())

// Memory usage
console.log(process.memoryUsage())

// Environment variables
console.log(process.env)




// events
let events = require("events");

// instance of eventEmitter class
const myEmitter = new events.EventEmitter();

myEmitter.on("registration", (name) => {console.log(`Hello ${name}`)})

// Call this method
myEmitter.emit("registration", process.argv[2]);