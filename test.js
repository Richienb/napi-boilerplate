import test from "ava"
import theModule from "."

test("main", (t) => {
	t.is(theModule(), "Hello World!")
})
