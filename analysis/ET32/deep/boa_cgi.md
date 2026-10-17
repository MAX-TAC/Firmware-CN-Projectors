# ET32 test.cgi static inspection
No program execution.
## file
/tmp/et32-test.cgi: POSIX shell script, ASCII text executable
## strings
#!/bin/sh
# Remember that CGI programs have to close out the HTTP header
# (with a pair of newlines), after giving the Content-type:
# and any other relevant or available header information.
# Unlike CGI programs running under Apache, CGI programs under Boa
# should understand some simple HTTP options.  The header (and the
# double-newline) should not be echo -need if the incoming request was
# in HTTP/0.9.  Also, we should stop after the header if
# REQUEST_METHOD == "HEAD".  Under Apache, nph- programs also have
# to worry about such stuff.
# Feb 3, 2000 -- updated to support POST, and avoid passing
# Malicious HTML Tags as described in CERT's CA-2000-02 advisory.
echo -ne "Content-type: text/html; charset=ISO-8859-1\r\n\r\n";
echo -ne "<html><head><title>Boa CGI test</title></head><body>\n";
echo -ne "<H2>Boa CGI test</H2>\n\n";
now=`date`
echo -ne "Date: ${now}\n";
echo -ne "<p>\n";
echo -ne "Method: ${REQUEST_METHOD}\n";
echo -ne "<p>\n";
echo -ne "<table border=1>\n";
echo -ne "<tr><td>Basic GET Form:<br>";
echo -ne " <form method=\"get\">\n\
  <input type=\"text\" name=\"parameter_1\" size=5 maxlength=5>\
    <select name=\"select_1\">\
      <option>foo</option>\
      <option>bar</option>\
    </select>\
  <input type=\"submit\" NAME=SUBMIT VALUE=\"Submit\">\
 </form>";
echo -ne "</td>";
echo -ne "<td>Basic POST Form:<br>";
echo -ne "<form method=\"post\">\n\
  <input type=\"text\" name=\"parameter_1\" size=5 maxlength=5>\
    <select name=\"select_1\">\
      <option>foo</option>\
      <option>bar</option>\
    </select>\
  <input type=\"submit\" NAME=SUBMIT VALUE=\"Submit\">\
  </form>";
echo -ne "</td>";
echo -ne "</tr>\n";
echo -ne "<tr><td colspan=2>Sample ISINDEX form:<br>\n";
echo -ne "<a href=\"${SCRIPT_NAME}?param1+param2+param3\">${SCRIPT_NAME}?param1+param2+param3</a>\n";
echo -ne "</td></tr>";
echo -ne "</table>\n";
echo -ne "<p>Query String: ${QUERY_STRING}\n";
# arguments list
echo -ne "<p>\nArguments:\n<ol>\n";
if [ $# -ge 0 ] ; then
echo "$@" | awk '{
        gsub(/&/,"\\&amp;");
        gsub(/</,"\\&lt;");
        gsub(/>/,"\\&gt;");
        for (i=1;i<=NF;i++) {
            printf "<li>%s\n", $i
        }
    }';
echo -ne "</ol>\n";
# environment list
echo -ne "<P>\nEnvironment:\n<UL>\n";
echo "`env`" | awk -F '=' '{
        gsub(/&/,"\\&amp;");
        gsub(/</,"\\&lt;");
        gsub(/>/,"\\&gt;");
        sub(/=/," = ");
        printf "<li>%s\n", $0
    }';
echo -ne "</UL>\n";
if [ "${REQUEST_METHOD}" == "POST" ] ; then
    echo -ne "Input stream:<br><hr><pre>\n";
    awk -F '=' '{
        gsub(/&/,"\\&amp;");
        gsub(/</,"\\&lt;");
        gsub(/>/,"\\&gt;");
        print $0
    }';
    echo -ne "</pre><hr>\n";
else
    echo -ne "No input stream: (not POST)<p>";
echo -ne "id: ", `id`, "\n<p>\n";
if [[ -n "`echo ${QUERY_STRING} | grep ident`" ]] && [ -n "${REMOTE_PORT}" ] ; then
# Uses idlookup-1.2 from Peter Eriksson  <pen@lysator.liu.se>
# ftp://coast.cs.purdue.edu/pub/tools/unix/ident/tools/idlookup-1.2.tar.gz
# Could use modification to timeout and trap stderr messages
	a="idlookup ".
      ${REMOTE_ADDR}." ".${REMOTE_PORT}." ".${SERVER_PORT};
	b=$(${a});
	echo -ne "ident output:<br><pre>\n${b}</pre>\n";
echo -ne "\n<EM>Boa http server</EM>\n";
echo -ne "</body></html>\n";
exit 0;
## Script content
#!/bin/sh

# Remember that CGI programs have to close out the HTTP header
# (with a pair of newlines), after giving the Content-type:
# and any other relevant or available header information.

# Unlike CGI programs running under Apache, CGI programs under Boa
# should understand some simple HTTP options.  The header (and the
# double-newline) should not be echo -need if the incoming request was
# in HTTP/0.9.  Also, we should stop after the header if
# REQUEST_METHOD == "HEAD".  Under Apache, nph- programs also have
# to worry about such stuff.

# Feb 3, 2000 -- updated to support POST, and avoid passing
# Malicious HTML Tags as described in CERT's CA-2000-02 advisory.

echo -ne "Content-type: text/html; charset=ISO-8859-1\r\n\r\n";
echo -ne "<html><head><title>Boa CGI test</title></head><body>\n";
echo -ne "<H2>Boa CGI test</H2>\n\n";
now=`date`
echo -ne "Date: ${now}\n";
echo -ne "<p>\n";
echo -ne "Method: ${REQUEST_METHOD}\n";
echo -ne "<p>\n";
echo -ne "<table border=1>\n";
echo -ne "<tr><td>Basic GET Form:<br>";
echo -ne " <form method=\"get\">\n\
  <input type=\"text\" name=\"parameter_1\" size=5 maxlength=5>\
    <select name=\"select_1\">\
      <option>foo</option>\
      <option>bar</option>\
    </select>\
  <input type=\"submit\" NAME=SUBMIT VALUE=\"Submit\">\
 </form>";
echo -ne "</td>";
echo -ne "<td>Basic POST Form:<br>";
echo -ne "<form method=\"post\">\n\
  <input type=\"text\" name=\"parameter_1\" size=5 maxlength=5>\
    <select name=\"select_1\">\
      <option>foo</option>\
      <option>bar</option>\
    </select>\
  <input type=\"submit\" NAME=SUBMIT VALUE=\"Submit\">\
  </form>";
echo -ne "</td>";
echo -ne "</tr>\n";
echo -ne "<tr><td colspan=2>Sample ISINDEX form:<br>\n";
echo -ne "<a href=\"${SCRIPT_NAME}?param1+param2+param3\">${SCRIPT_NAME}?param1+param2+param3</a>\n";
echo -ne "</td></tr>";
echo -ne "</table>\n";

echo -ne "<p>Query String: ${QUERY_STRING}\n";

# arguments list
echo -ne "<p>\nArguments:\n<ol>\n";
if [ $# -ge 0 ] ; then
echo "$@" | awk '{
        gsub(/&/,"\\&amp;");
        gsub(/</,"\\&lt;");
        gsub(/>/,"\\&gt;");
        for (i=1;i<=NF;i++) {
            printf "<li>%s\n", $i
        }
    }';
fi
echo -ne "</ol>\n";

# environment list
echo -ne "<P>\nEnvironment:\n<UL>\n";
echo "`env`" | awk -F '=' '{
        gsub(/&/,"\\&amp;");
        gsub(/</,"\\&lt;");
        gsub(/>/,"\\&gt;");
        sub(/=/," = ");
        printf "<li>%s\n", $0
    }';
echo -ne "</UL>\n";

if [ "${REQUEST_METHOD}" == "POST" ] ; then
    echo -ne "Input stream:<br><hr><pre>\n";
    awk -F '=' '{
        gsub(/&/,"\\&amp;");
        gsub(/</,"\\&lt;");
        gsub(/>/,"\\&gt;");
        print $0
    }';
    echo -ne "</pre><hr>\n";
else
    echo -ne "No input stream: (not POST)<p>";
fi

echo -ne "id: ", `id`, "\n<p>\n";

if [[ -n "`echo ${QUERY_STRING} | grep ident`" ]] && [ -n "${REMOTE_PORT}" ] ; then

# Uses idlookup-1.2 from Peter Eriksson  <pen@lysator.liu.se>
# ftp://coast.cs.purdue.edu/pub/tools/unix/ident/tools/idlookup-1.2.tar.gz
# Could use modification to timeout and trap stderr messages
	a="idlookup ".
      ${REMOTE_ADDR}." ".${REMOTE_PORT}." ".${SERVER_PORT};
	b=$(${a});
	echo -ne "ident output:<br><pre>\n${b}</pre>\n";
fi

echo -ne "\n<EM>Boa http server</EM>\n";
echo -ne "</body></html>\n";

exit 0;


