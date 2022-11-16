import re

regex_tag = re.compile(r"\\displaystyle\s*")
regex_match_two_sides = re.compile(r"{(.+)}")
regex_repl_two_sides = r"<math-expression>\1</math-expression>"

def generate_latex_math_expression(text: str):
   pure_latex = regex_tag.sub('', text)
   latex_with_math_tag = regex_match_two_sides.sub(regex_repl_two_sides, pure_latex)
   return latex_with_math_tag