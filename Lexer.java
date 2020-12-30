import java.util.Scanner;
import java.io.File;
import java.io.FileNotFoundException;
import java.util.Arrays;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.util.regex.PatternSyntaxException;

public class Lexer
{
  private String[] toArray(String filename)
  {
    String[] file_lines = {};
    try
    {
      Scanner scanner = new Scanner (new File(filename));
      while (scanner.hasNextLine())
      {
        String line = scanner.nextLine();
        file_lines = Arrays.copyOf(file_lines,file_lines.length +1);
        file_lines[file_lines.length-1]=line;
      }
    }
    catch (FileNotFoundException e)
    {
      e.printStackTrace();
    }
    return file_lines;
  }
  private void toToken(String[] lines)
  {
    // I do not know if this needs to be string
    // would like to use char, but then again vars are crazy
    String[] chars_in_line = {};
    for(int i=0;i<lines.length;i++)
    {
      String line_raw = lines[i];
      switch (token)
      {
        case "+":
        case "-"://match meth
        case "*":
        case "/"://match meth
        case "="://match meth
        case ">":
        case "<":
        case "&":
        case "|":
        case "!":
        // case "/~":xor(l,r),
        // "->":guard(l,r),
        // "=>":assign(l,r)
      }
    }
  }
  // this is totally unnecessary if you think about it even for a little bit
  private boolean match(char given, char expected)
  {
    if (given.equals(expected))
    {
      return True;
    }
    return False;
  }
  public static void main(String[] args)
  {
    String[] lines = toArray("code.txt");
    toToken(lines);
  }
}
