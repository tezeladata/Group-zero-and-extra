const os = require("os")
const events = require("events")

// 1
console.log(os.type(), os.release(), os.totalmem(), os.freemem())

// 2
const seconds = Number(os.uptime())
const hours = parseInt(seconds / 3600 )
console.log(`Pc's uptime is ${hours}h`)

// 3
console.log(process.argv)
console.log(process.env)

// 4
console.log(process.getActiveResourcesInfo())
console.log(process.resourceUsage())

// 5, 6
const event1 = new events.EventEmitter();
event1.on("greet", (name) => console.log(`Hello ${name}`))

event1.emit("greet", "David")

// 7
const start = new events.EventEmitter();
const stop = new events.EventEmitter();

// Extra function
const handler = () => {
    stop.on("stopped", () => console.log(`Stopped`));
    setTimeout(() => {console.log("Timed out")}, 3000)
    stop.emit("stopped");
}

start.on("starting", handler)
start.emit("starting");

// 8
start.removeListener("starting", handler);
console.log(start)