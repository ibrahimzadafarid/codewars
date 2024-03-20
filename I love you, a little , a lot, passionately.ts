// ! I love you, a little , a lot, passionately ... not at all https://www.codewars.com/kata/57f24e6a18e9fad8eb000296
// ! 8KYU

export function howMuchILoveYou(petals: number): string {
    const phrases = [
        "I love you",
        "a little",
        "a lot",
        "passionately",
        "madly",
        "not at all",
    ];

    return phrases[(petals - 1) % phrases.length]

  }