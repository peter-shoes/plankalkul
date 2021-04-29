package com.peter_shoes_.plankalkul;

enum TokenType {
  // Single-character tokens.
  LEFT_PAREN, RIGHT_PAREN, LEFT_BRACE, RIGHT_BRACE,
  COMMA, DOT,
  PLUS, MULTIPLY,
  BANG, CONJUNCTION, DISCONJUNCTION,
  GREATER, LESS,
  ITERATOR,//iterator as i

  // two character tokens.
  MINUS, GUARD,
  EQUAL, ASSIGNMENT,
  DIVIDE, XOR,

  // Literals.
  VARIABLEN_V, VARIABLEN_Z, VARIABLEN_R, CONSTANT,
  PROGRAM_ID, PROGRAM_NAME,//PID as Pn, where n is the number of the program
  WHILE,//while as Wn where n is the number of the while


  // Keywords.
  END,

  EOF
}
