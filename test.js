const test = require("ava")
const theModule = require(".")

test("main", (t) => {
	t.is(theModule(), "Hello World!")
})
