// https://leetcode.com/problems/calculator-with-method-chaining/

class Calculator {
  private calc: number
  
  constructor(value: number) {
      this.calc = value
  }
  
  add(value: number): Calculator {
      this.calc += value
      return this
  }
  
  subtract(value: number): Calculator {
      this.calc -= value
      return this
  }
  
  multiply(value: number): Calculator {
      this.calc *= value
      return this
  }
  
  divide(value: number): Calculator {
      if (value === 0) {
          throw new Error("Division by zero is not allowed")
      }

      this.calc /= value
      return this
  }
  
  power(value: number): Calculator {
      this.calc **= value
      return this
  }
  
  getResult(): number {
      return this.calc
  }
}