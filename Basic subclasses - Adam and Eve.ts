// !  Basic subclasses - Adam and Eve https://www.codewars.com/kata/547274e24481cfc469000416
// ! 8KYU
export class Human {}

export class Man extends Human {}

export class Woman extends Human {}

export class God {
  static create(): Human[] {
    return [new Man(), new Woman()];
  }
}

console.log(God.create());
