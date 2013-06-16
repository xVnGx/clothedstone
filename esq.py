# User Instructions
#
# Implement the function escape_html(s), which replaces:
# > with &gt;
# < with &lt;
# " with &quot;
# & with &amp;
# and returns the escaped string
# Note that your browser will probably automatically
# render your escaped text as the corresponding symbols,
# but the grading script will still correctly evaluate it.
#
import cgi

def escape_html(s):
    return cgi.escape(s, quote = True)

print esq_html("&&&& ><><z<<><><")