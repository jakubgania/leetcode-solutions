// https://leetcode.com/problems/generate-fibonacci-sequence/

function* fibGenerator(): Generator<number, any, number> {
  const fib_0 = 0
  yield fib_0
  const fib_1 = 1
  yield fib_1

  let previous_value = fib_0, current_value = fib_1
  let next_value = 0;

  while(true) {
      next_value = previous_value + current_value
      previous_value = current_value
      current_value = next_value
      yield current_value
  }
};

/**
* const gen = fibGenerator();
* gen.next().value; // 0
* gen.next().value; // 1
*/