// https://leetcode.com/problems/debounce/

type F = (...p: any[]) => any

function debounce(fn: F, t: number): F {
    // in VSC, null gives an error
    // let timer = null
    let timer = 0
    return function(...args) {
        clearTimeout(timer)
        timer = setTimeout(() => fn(...args), t)
    }
};

/**
 * const log = debounce(console.log, 100);
 * log('Hello'); // cancelled
 * log('Hello'); // cancelled
 * log('Hello'); // Logged at t=100ms
 */