package com.peter_shoes_.plankalkul;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import static com.peter_shoes_.plankalkul.TokenType.*;

class Scanner {
  private final String source;
  private final List<Token> tokens = new ArrayList<>();
  private int start = 0;
  private int current = 0;
  private int line = 1;

  Scanner(String source) {
    this.source = source;
  }
  List<Token> scanTokens() {
    while (!isAtEnd()) {
      // We are at the beginning of the next lexeme.
      start = current;
      scanToken();
    }

    tokens.add(new Token(EOF, "", null, line));
    return tokens;
  }
  private void scanToken() {
    char c = advance();
    switch (c) {
      case '(': addToken(LEFT_PAREN); break;
      case ')': addToken(RIGHT_PAREN); break;
      case '[': addToken(LEFT_BRACE); break;
      case ']': addToken(RIGHT_BRACE); break;
      case ',': addToken(COMMA); break;
      case '.': addToken(DOT); break;
      case '+': addToken(PLUS); break;
      case '*': addToken(MULTIPLY); break;
      case '!': addToken(BANG); break;
      case '&': addToken(CONJUNCTION); break;
      case '|': addToken(DISCONJUNCTION); break;
      case '>': addToken(GREATER); break;
      case '<': addToken(LESS); break;
      case 'i': addToken(ITERATOR); break;
      case '-': addToken(match('>') ? GUARD : MINUS); break;
      case '=': addToken(match('>') ? ASSIGNMENT : EQUAL); break;
      case '/': addToken(match('~') ? XOR : DIVIDE); break;

      case ' ':
      case '\r':
      case '\t':
        // Ignore whitespace.
        break;

      case '\n':
        line++;
        break;
        // now here we gotta add the cases for variables and all that other shit
      default:
        Plankalkul.error(line, "Unexpected character.");
        break;
    }
  }
  // pretty obvious boolean return metch method for finding double lexemes
  private boolean match(char expected) {
    if (isAtEnd()) return false;
    if (source.charAt(current) != expected) return false;

    current++;
    return true;
  }
  // like advance, but doesn't consume the character
  private char peek() {
    if (isAtEnd()) return '\0';
    return source.charAt(current);
  }
  private boolean isAtEnd() {
    return current >= source.length();
  }
  private char advance() {
    current++;
    return source.charAt(current - 1);
  }

  private void addToken(TokenType type) {
    addToken(type, null);
  }
  private void addToken(TokenType type, Object literal) {
    String text = source.substring(start, current);
    tokens.add(new Token(type, text, literal, line));
  }
}
